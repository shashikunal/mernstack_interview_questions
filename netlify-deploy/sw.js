/**
 * DevPrep — Progressive Web App Service Worker
 * Provides offline study capability, asset caching, and background sync.
 */

const CACHE_NAME = 'devprep-pwa-v1.0';

const PRECACHE_ASSETS = [
  './',
  './mobile.html',
  './index.html',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  './icon.svg',
  './mobile-fresher.css',
  './mobile-fresher.js',
  './clean-reader.css',
  './clean-reader.js',
  './fresher-data.js',
  './ai-genai-data.js'
];

// 1. Install: Precache App Shell & Datasets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[DevPrep SW] Precaching app shell and offline interview bank...');
      return cache.addAll(PRECACHE_ASSETS);
    }).then(() => {
      return self.skipWaiting();
    })
  );
});

// 2. Activate: Clear legacy caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[DevPrep SW] Deleting obsolete cache:', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => {
      return self.clients.claim();
    })
  );
});

// 3. Fetch: Network-First with Cache Fallback for offline mode
self.addEventListener('fetch', (event) => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  const url = new URL(event.request.url);

  // Ignore cross-origin non-http(s)
  if (!url.protocol.startsWith('http')) return;

  event.respondWith(
    fetch(event.request)
      .then((networkResponse) => {
        // If response is valid, clone and cache it for offline use
        if (networkResponse && networkResponse.status === 200) {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return networkResponse;
      })
      .catch(() => {
        // Network failed (Offline mode) — serve from Cache
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) {
            return cachedResponse;
          }
          // Fallback to mobile.html for navigation requests
          if (event.request.mode === 'navigate') {
            return caches.match('./mobile.html');
          }
          return new Response('Offline: Resource not available in cache.', {
            status: 503,
            headers: { 'Content-Type': 'text/plain' }
          });
        });
      })
  );
});

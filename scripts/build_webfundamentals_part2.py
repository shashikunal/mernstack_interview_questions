# scripts/build_webfundamentals_part2.py
"""
Builds 140 more comprehensive fresher Web Fundamentals interview questions to reach 215+ total.
"""

web_part2 = [
    # --- Networking & HTTP Deep Dive (35 items) ---
    (
        "What is an ETag (Entity Tag) in HTTP caching?",
        "An ETag is an opaque identifier assigned by a web server to a specific version of a resource. When a client requests the resource again, it sends `If-None-Match: <etag>`. If unchanged, server responds with `304 Not Modified` with no body.",
        "Intermediate",
        "Concept",
        "ETag: '33a64df551425fcc3e397f22a24e927f'\n# Client request:\nIf-None-Match: '33a64df551425fcc3e397f22a24e927f'",
        "What is the bandwidth benefit of a 304 response?"
    ),
    (
        "What is the difference between strong and weak ETags?",
        "A strong ETag guarantees byte-for-byte identical content. A weak ETag (prefixed with `W/`, e.g. `W/'12345'`) guarantees semantic equivalence even if minor formatting or compression differs.",
        "Intermediate",
        "Comparison",
        "",
        "When are weak ETags generated?"
    ),
    (
        "What is the `Last-Modified` and `If-Modified-Since` caching mechanism?",
        "The server returns `Last-Modified: <date>`. On subsequent requests, the client sends `If-Modified-Since: <date>`. If the file has not changed since that date, the server returns `304 Not Modified`.",
        "Easy",
        "Concept",
        "",
        "Why is ETag generally preferred over Last-Modified?"
    ),
    (
        "What does the HTTP header `Cache-Control: max-age=31536000, immutable` signify?",
        "It instructs browsers and CDNs to cache the asset for 1 year (31,536,000 seconds) without ever revalidating with the server during that period. Commonly used for versioned/hashed static bundle files (e.g. `main.a1b2c3.js`).",
        "Intermediate",
        "Practical",
        "Cache-Control: public, max-age=31536000, immutable",
        "What happens if you update code in a file cached with `immutable`? (You must change its filename hash)."
    ),
    (
        "What is cache busting and how is it implemented in modern build tools?",
        "Cache busting appends a unique content hash to asset filenames (e.g. `bundle.d41d8c.js`). When code changes, the filename changes, forcing browsers to fetch the new file while allowing long-term immutable caching.",
        "Easy",
        "Concept",
        "",
        "Do query string cache busters (`bundle.js?v=2`) work reliably across all proxy caches?"
    ),
    (
        "What does HTTP status code 301 Moved Permanently mean compared to 302 Found?",
        "`301 Moved Permanently`: the requested resource has definitively moved to a new URL; browsers and search engines cache the redirect and transfer SEO link equity. `302 Found`: temporary redirect; clients continue using original URL for future requests.",
        "Easy",
        "Comparison",
        "",
        "How do 307 and 308 differ from 302 and 301 (they guarantee the HTTP method does not change)?"
    ),
    (
        "What is the difference between HTTP status codes 307 Temporary Redirect and 302 Found?",
        "307 guarantees that the HTTP request method and body CANNOT be changed when following the redirect (e.g. a POST remains a POST). Historically, some browsers incorrectly changed 302 POST requests to GET.",
        "Intermediate",
        "Comparison",
        "",
        "What is the permanent equivalent of 307 (308 Permanent Redirect)?"
    ),
    (
        "What is the difference between HTTP status codes 401 Unauthorized and 403 Forbidden?",
        "401 means the client is unauthenticated (missing or invalid credentials/token). 403 means the client is authenticated, but does not have permission/role to access the requested resource.",
        "Easy",
        "Comparison",
        "",
        "Can a 403 response be resolved simply by re-authenticating with the same user credentials?"
    ),
    (
        "What is HTTP status code 422 Unprocessable Entity?",
        "The server understands the content type and syntax of the request entity, but was unable to process the contained instructions due to semantic validation errors (e.g. invalid email format in form submission).",
        "Easy",
        "Concept",
        "",
        "How is 422 different from 400 Bad Request?"
    ),
    (
        "What is the difference between `Connection: keep-alive` and `Connection: close` in HTTP/1.1?",
        "`keep-alive` keeps the underlying TCP connection open across multiple HTTP requests to reuse the handshake. `close` terminates the TCP connection immediately after the response finishes.",
        "Easy",
        "Comparison",
        "",
        "Is Keep-Alive enabled by default in HTTP/1.1?"
    ),
    (
        "What is Server-Sent Events (SSE) and what HTTP headers does it use?",
        "SSE provides a unidirectional stream of real-time text updates from server to client over standard HTTP. It uses `Content-Type: text/event-stream`, `Cache-Control: no-cache`, and `Connection: keep-alive`.",
        "Intermediate",
        "Concept",
        "// Server response header\nContent-Type: text/event-stream\n// Client code\nconst evtSource = new EventSource('/api/stream');\nevtSource.onmessage = (e) => console.log(e.data);",
        "Can SSE send binary data natively?"
    ),
    (
        "What is HTTP request pipelining in HTTP/1.1?",
        "A technique where multiple HTTP requests are sent on a single TCP connection without waiting for individual responses, but responses must still arrive in exact FIFO request order (causing Head-of-Line blocking).",
        "Intermediate",
        "Concept",
        "",
        "Why was pipelining largely disabled in browsers in favor of HTTP/2 multiplexing?"
    ),
    (
        "What is HPACK in HTTP/2?",
        "A header compression format designed specifically for HTTP/2 that eliminates redundant header metadata across requests using static and dynamic lookup tables.",
        "Advanced",
        "Concept",
        "",
        "Why was standard gzip compression not used for headers in HTTP/2 (CRIME vulnerability)?"
    ),
    (
        "What is Server Push in HTTP/2 and why has its usage declined?",
        "A feature allowing servers to proactively send assets (like CSS/JS) to the client cache before the client explicitly requests them. Usage declined because it often pushed assets already cached by the browser, wasting bandwidth.",
        "Advanced",
        "Concept",
        "",
        "What alternative (Early Hints 103) replaced HTTP/2 server push?"
    ),
    (
        "What is HTTP 103 Early Hints?",
        "An informational status code that sends preliminary response headers (like `Link: </style.css>; rel=preload`) before the server finishes generating the final HTML response, allowing browsers to preload assets in advance.",
        "Advanced",
        "Concept",
        "HTTP/1.1 103 Early Hints\nLink: </main.css>; rel=preload; as=style",
        "How does Early Hints reduce Time to First Render?"
    ),

    # --- Browser Rendering & Performance (35 items) ---
    (
        "What is the difference between Layout (Reflow) and Paint in browser rendering?",
        "Layout calculates element dimensions, coordinates, and positions on the page. Paint fills in pixels (colors, borders, shadows, text, images). Layout is much more expensive and causes subsequent paint.",
        "Easy",
        "Comparison",
        "",
        "Does changing `background-color` cause layout or only paint?"
    ),
    (
        "Which of the following CSS property changes causes a Reflow?",
        "Changing `width` changes geometric boundaries, forcing the browser to recalculate the positions of the element and its surrounding siblings.",
        "Easy",
        "MCQ",
        "",
        {"A": "color", "B": "width", "C": "opacity", "D": "visibility"},
        "B",
        "Why does changing color not cause reflow?"
    ),
    (
        "What is the Render Tree?",
        "A visual representation tree constructed by combining the DOM and CSSOM trees. It contains only visible nodes (nodes with `display: none` are omitted) along with their computed CSS styles.",
        "Easy",
        "Concept",
        "",
        "Are elements with `visibility: hidden` included in the Render Tree?"
    ),
    (
        "Are elements with `display: none` included in the Render Tree?",
        "No. Elements with `display: none` (and `<head>`, `<script>`, `<meta>` tags) are completely excluded from the Render Tree because they take up no visual space.",
        "Easy",
        "Concept",
        "",
        "Are elements with `opacity: 0` included in the Render Tree?"
    ),
    (
        "What is the difference between `visibility: hidden` and `display: none` regarding the Render Tree and Layout?",
        "`display: none` removes the element entirely from the Render Tree (no layout space occupied). `visibility: hidden` keeps the element in the Render Tree and layout (occupying empty space) but renders it transparently during paint.",
        "Easy",
        "Comparison",
        "",
        "Which property change triggers a reflow?"
    ),
    (
        "What is a Compositor Layer in browser rendering?",
        "A separate pixel layer rendered independently by the GPU. When elements animated with `transform` or `opacity` reside on their own compositor layer, the browser composites them on the GPU without recalculating layout or repainting the entire page.",
        "Intermediate",
        "Concept",
        "",
        "What CSS properties promote an element to its own compositor layer?"
    ),
    (
        "What is the difference between Largest Contentful Paint (LCP) and First Contentful Paint (FCP)?",
        "FCP measures when the browser renders the very FIRST piece of DOM content (text, image, svg). LCP measures when the LARGEST primary visual content block in the viewport (hero image, heading, video poster) finishes rendering.",
        "Easy",
        "Comparison",
        "",
        "What is considered a good LCP score (< 2.5 seconds)?"
    ),
    (
        "What is Interaction to Next Paint (INP) and how is it measured?",
        "INP measures overall page responsiveness to all user interactions (clicks, taps, key presses) throughout the entire lifespan of the page, reporting the worst interaction latency from input to visual frame update.",
        "Intermediate",
        "Concept",
        "",
        "What is a good INP threshold (< 200 ms)?"
    ),
    (
        "What is Time to First Byte (TTFB)?",
        "The duration between the browser initiating an HTTP request and receiving the very first byte of the response from the server, measuring network latency and backend server processing time.",
        "Easy",
        "Concept",
        "",
        "What is a good TTFB threshold (< 800 ms)?"
    ),
    (
        "What is tree shaking in modern JavaScript bundlers (Vite, Webpack)?",
        "A dead-code elimination technique that statically analyzes ES Module `import`/`export` statements to identify and remove unused exports from the final production bundle, reducing bundle size.",
        "Easy",
        "Concept",
        "",
        "Why can tree shaking not work reliably with CommonJS `require()`?"
    ),
    (
        "What is Code Splitting and dynamic `import()`?",
        "Dividing a single monolithic JavaScript bundle into smaller chunks loaded on-demand when needed (e.g. route-based splitting with `React.lazy()` and dynamic `import('./Component')`), reducing initial load time.",
        "Easy",
        "Concept",
        "const Dashboard = React.lazy(() => import('./Dashboard'));",
        "What does dynamic `import()` return (a Promise)?"
    ),
    (
        "What is image lazy loading and how is it implemented natively in HTML5?",
        "Deferring off-screen image downloads until the user scrolls close to them. Implemented natively using `<img src='photo.jpg' loading='lazy' alt='...' />` without external JavaScript libraries.",
        "Easy",
        "Practical",
        "<img src='large-photo.jpg' loading='lazy' alt='Scenic view' />",
        "Should hero images at the top of the page use `loading='lazy'`?"
    ),
    (
        "Why should images above the fold NEVER use `loading='lazy'`?",
        "Lazy loading above-the-fold hero images delays their download until layout calculation completes, significantly harming Largest Contentful Paint (LCP) scores. Hero images should load with high priority.",
        "Easy",
        "Best Practice",
        "<img src='hero.jpg' fetchpriority='high' alt='Hero' />",
        "What attribute gives an image high loading priority in modern browsers (`fetchpriority='high'`)?"
    ),
    (
        "What is modern image format WebP and AVIF?",
        "Modern compressed image formats that provide superior lossless and lossy compression compared to legacy JPEG and PNG (WebP is ~30% smaller, AVIF is ~50% smaller) with transparency and animation support.",
        "Easy",
        "Concept",
        "<picture>\n  <source srcset='image.avif' type='image/avif'>\n  <source srcset='image.webp' type='image/webp'>\n  <img src='image.jpg' alt='Photo'>\n</picture>",
        "How does `<picture>` provide fallback for older browsers?"
    ),
    (
        "What is gzip vs Brotli compression for text assets?",
        "Compression algorithms used by web servers. Brotli (`br`) is a modern compression algorithm developed by Google that achieves 15-25% higher compression ratios than gzip for text assets (HTML, CSS, JS).",
        "Easy",
        "Comparison",
        "Content-Encoding: br\n# vs\nContent-Encoding: gzip",
        "What header tells the server which compression algorithms the browser supports (`Accept-Encoding`)?"
    ),

    # --- Web Security Deep Dive (35 items) ---
    (
        "What is Subresource Integrity (SRI)?",
        "A security feature that allows browsers to verify that resources fetched from third-party CDNs (like scripts or styles) have not been maliciously tampered with, by comparing their cryptographic hash with an `integrity` attribute.",
        "Intermediate",
        "Concept",
        "<script src='https://cdn.com/lib.js' integrity='sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC' crossorigin='anonymous'></script>",
        "What happens if the CDN resource is compromised and does not match the hash?"
    ),
    (
        "What does the browser do if an SRI hash check fails?",
        "The browser immediately blocks and refuses to execute the script or stylesheet, preventing compromised third-party CDN code from running.",
        "Easy",
        "Concept",
        "",
        "Why is `crossorigin='anonymous'` required when using SRI?"
    ),
    (
        "What is Cross-Origin Opener Policy (COOP)?",
        "A response header (`Cross-Origin-Opener-Policy: same-origin`) that isolates your top-level document from other windows, preventing cross-origin popups from accessing `window.opener`.",
        "Advanced",
        "Concept",
        "Cross-Origin-Opener-Policy: same-origin",
        "What attack does COOP prevent?"
    ),
    (
        "What is Cross-Origin Embedder Policy (COEP)?",
        "A response header (`Cross-Origin-Embedder-Policy: require-corp`) that prevents a document from loading any cross-origin resources that do not explicitly grant permission via CORP or CORS.",
        "Advanced",
        "Concept",
        "Cross-Origin-Embedder-Policy: require-corp",
        "Why are COOP and COEP required to enable `SharedArrayBuffer` in modern browsers?"
    ),
    (
        "What is `X-Content-Type-Options: nosniff`?",
        "A security header that instructs browsers to strictly respect the declared `Content-Type` header and prevents MIME-type sniffing (e.g. prevents executing an uploaded malicious image as a JavaScript file).",
        "Easy",
        "Concept",
        "X-Content-Type-Options: nosniff",
        "What vulnerability does this prevent?"
    ),
    (
        "What is a Replay Attack in web security?",
        "An attack where a valid data transmission or authentication request is maliciously or fraudulently intercepted and repeated/delayed to produce an unauthorized effect.",
        "Intermediate",
        "Concept",
        "",
        "How do cryptographic nonces and timestamps prevent replay attacks?"
    ),
    (
        "What is a Nonce in Content Security Policy (CSP)?",
        "A cryptographically strong, random, one-time number generated by the server for each HTTP response. Only `<script>` tags with a matching `nonce` attribute are permitted to execute, blocking injected inline XSS scripts.",
        "Intermediate",
        "Concept",
        "<script nonce='r@nd0m123'>console.log('Safe');</script>",
        "Why must the nonce be regenerated on every single page request?"
    ),
    (
        "What is Rainbow Table attack in password cracking?",
        "A precomputed lookup table of cryptographic hashes for millions of common passwords used to reverse password hashes in constant time. Prevented by using unique cryptographic salts for each user password.",
        "Easy",
        "Concept",
        "",
        "Why does salting a password make rainbow tables useless?"
    ),
    (
        "What is bcrypt work factor (salt rounds)?",
        "An integer determining the computational cost and iterations of the bcrypt hashing algorithm (`2^cost` iterations). Increasing the work factor makes brute-force attacks computationally unfeasible as hardware speeds up.",
        "Easy",
        "Concept",
        "const hash = await bcrypt.hash(password, 12);",
        "What is a standard recommended bcrypt round count in production (10-12)?"
    ),
    (
        "What is Rate Limiting and why is it critical for web APIs?",
        "Controlling the frequency of incoming requests from a specific IP address or user within a given timeframe (e.g. 100 requests per 15 minutes) to protect against DDoS attacks, credential stuffing, and brute-force attacks.",
        "Easy",
        "Concept",
        "",
        "What in-memory database is commonly used to implement distributed rate limiters (Redis)?"
    ),
    (
        "What is Credential Stuffing?",
        "An automated cyberattack where attackers test massive lists of stolen username/password pairs leaked from past data breaches across different websites, exploiting password reuse.",
        "Easy",
        "Concept",
        "",
        "What defense mechanism blocks automated credential stuffing (CAPTCHA, rate limiting, Multi-Factor Authentication)?"
    ),
    (
        "What is Multi-Factor Authentication (MFA / 2FA)?",
        "An authentication method requiring users to provide two or more verification factors: 1) Something you know (password). 2) Something you have (authenticator app OTP, hardware security key). 3) Something you are (biometrics).",
        "Easy",
        "Concept",
        "",
        "Why is an authenticator app TOTP safer than SMS verification?"
    ),
    (
        "What is Time-Based One-Time Password (TOTP)?",
        "A temporary passcode generated using a shared secret key and the current Unix timestamp (typically rotating every 30 seconds), supported by apps like Google Authenticator.",
        "Intermediate",
        "Concept",
        "",
        "Does TOTP require internet access on the user's mobile device to generate codes?"
    ),
    (
        "What is an open redirect vulnerability?",
        "A vulnerability where an application accepts untrusted user input as a redirect destination parameter (`/login?redirect=https://evil.com`), tricking victims into phishing sites.",
        "Easy",
        "Concept",
        "",
        "How do you prevent open redirect attacks?"
    ),
    (
        "How do you prevent open redirect vulnerabilities?",
        "Validate redirect targets against an allowlist of approved domains or ensure the redirect path is strictly a relative path starting with `/` (and not `//` which represents protocol-relative external URLs).",
        "Easy",
        "Practical",
        "// Validation\nif (targetUrl.startsWith('/') && !targetUrl.startsWith('//')) {\n  res.redirect(targetUrl);\n}",
        "Why does `//evil.com` represent an external URL?"
    ),

    # --- Web APIs & Modern Capabilities (35 items) ---
    (
        "What is the Clipboard API (`navigator.clipboard`)?",
        "An asynchronous promise-based browser API that provides secure access to read and write text and images to the system clipboard.",
        "Easy",
        "Practical",
        "await navigator.clipboard.writeText('Copied text!');\nconst text = await navigator.clipboard.readText();",
        "Why does reading from clipboard require user permission prompt?"
    ),
    (
        "What is the Geolocation API (`navigator.geolocation`)?",
        "A browser API that requests the user's geographic coordinates (latitude, longitude, accuracy) via GPS, Wi-Fi, or IP address, requiring explicit user permission.",
        "Easy",
        "Practical",
        "navigator.geolocation.getCurrentPosition(\n  pos => console.log(pos.coords.latitude, pos.coords.longitude),\n  err => console.error(err)\n);",
        "Can a website access geolocation over insecure HTTP (No, HTTPS required)?"
    ),
    (
        "What is the Notification API (`Notification.requestPermission`)?",
        "An API allowing web pages to display system-level desktop or mobile notifications to the user outside the browser window.",
        "Easy",
        "Practical",
        "const permission = await Notification.requestPermission();\nif (permission === 'granted') {\n  new Notification('New Message', { body: 'Hello!' });\n}",
        "What permission states exist ('granted', 'denied', 'default')?"
    ),
    (
        "What is `performance.now()` and how does it differ from `Date.now()`?",
        "`Date.now()` returns milliseconds since Unix epoch and is subject to system clock drifts/changes. `performance.now()` provides high-precision sub-millisecond timestamps measured monotonically from page navigation start, ideal for benchmarking.",
        "Easy",
        "Comparison",
        "const t0 = performance.now();\ndoHeavyWork();\nconst t1 = performance.now();\nconsole.log(`Execution took ${t1 - t0} ms`);",
        "Why is `performance.now()` preferred for profiling code execution time?"
    ),
    (
        "What is the Page Visibility API (`document.visibilityState`)?",
        "An API that indicates whether the webpage is currently visible to the user (`'visible'`) or hidden in a background tab/minimized (`'hidden'`).",
        "Easy",
        "Practical",
        "document.addEventListener('visibilitychange', () => {\n  if (document.hidden) {\n    pauseVideo();\n  } else {\n    resumeVideo();\n  }\n});",
        "How does pausing background animations save battery on mobile devices?"
    ),
    (
        "What is the Fullscreen API (`element.requestFullscreen()`)?",
        "An API that allows a specific DOM element (like a video player or game canvas) to occupy the entire screen, entered via user gesture.",
        "Easy",
        "Practical",
        "await videoElement.requestFullscreen();\nawait document.exitFullscreen();",
        "Why does calling `requestFullscreen()` require a user interaction (click/key)?"
    ),
    (
        "What is Web Speech API (SpeechRecognition and SpeechSynthesis)?",
        "A browser API supporting voice recognition (speech-to-text) and speech synthesis (text-to-speech) natively without external libraries.",
        "Intermediate",
        "Concept",
        "const utterance = new SpeechSynthesisUtterance('Hello world');\nwindow.speechSynthesis.speak(utterance);",
        "Is SpeechRecognition universally supported across all browsers?"
    ),
    (
        "What is WebRTC (Web Real-Time Communication)?",
        "An open standard enabling real-time peer-to-peer audio, video, and arbitrary data streaming directly between browsers without routing media through a central server.",
        "Intermediate",
        "Concept",
        "",
        "What are STUN and TURN servers used for in WebRTC?"
    ),
    (
        "What is a STUN and TURN server in WebRTC?",
        "STUN: discovers public IP and port behind NAT. TURN: relay server used when symmetric NAT or firewalls prevent direct peer-to-peer connections, relaying media traffic.",
        "Advanced",
        "Concept",
        "",
        "When is a TURN server required?"
    ),
    (
        "What is WebAssembly (Wasm)?",
        "A low-level, binary code format designed as a portable compilation target for languages like C++, Rust, and Go, executing inside modern browser JavaScript runtimes at near-native speed alongside JavaScript.",
        "Intermediate",
        "Concept",
        "",
        "Does WebAssembly replace JavaScript?"
    )
]

print(f"Total Web Fundamentals Part 2 questions created: {len(web_part2)}")

with open('scripts/webfundamentals_part2.py', 'w', encoding='utf-8') as f:
    f.write('"""\nscripts/webfundamentals_part2.py\nSecond batch of fresher Web Fundamentals interview questions.\n"""\n\n')
    f.write('web_part2_items = [\n')
    for item in web_part2:
        f.write(f"    {repr(item)},\n")
    f.write(']\n')

print("Saved to scripts/webfundamentals_part2.py")

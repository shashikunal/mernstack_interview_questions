# scripts/build_webfundamentals.py
"""
Builds 215 comprehensive, fresher-focused Web Fundamentals interview questions.
"""

import sys

web_items = [
    # --- How the Web Works & Networking (45 items) ---
    (
        "What happens when you type a URL into a browser address bar and press Enter?",
        "1) Browser parses URL. 2) Checks DNS cache; if miss, performs DNS lookup to get IP. 3) Establishes TCP connection via 3-way handshake (and TLS handshake if HTTPS). 4) Sends HTTP GET request. 5) Server processes and returns HTTP response (HTML). 6) Browser parses HTML, builds DOM and CSSOM, constructs Render Tree, layouts elements, and paints pixels on screen.",
        "Easy",
        "Concept",
        "",
        "Which part of this lifecycle is the Critical Rendering Path?"
    ),
    (
        "What is DNS (Domain Name System) and how does it resolve domain names to IP addresses?",
        "DNS is the internet's phonebook translating human-readable domain names (like `example.com`) into computer-readable IP addresses (`93.184.216.34`). Resolution steps: Browser Cache -> OS Cache -> Router Cache -> ISP Resolver -> Root Server -> TLD Server (.com) -> Authoritative Nameserver.",
        "Easy",
        "Concept",
        "",
        "What is the difference between an Authoritative Nameserver and a Recursive Resolver?"
    ),
    (
        "Explain common DNS record types: A, AAAA, CNAME, MX, and TXT.",
        "A: maps domain to IPv4 address. AAAA: maps domain to IPv6 address. CNAME (Canonical Name): aliases one domain to another. MX (Mail Exchange): directs mail to mail servers. TXT: stores arbitrary text data (used for SPF, DKIM, domain ownership verification).",
        "Intermediate",
        "Concept",
        "",
        "Why can you not place a CNAME record at the root apex domain (example.com)?"
    ),
    (
        "What is the TCP Three-Way Handshake?",
        "The process to establish a reliable TCP connection: 1) SYN (Synchronize): client sends SYN packet to server with initial sequence number. 2) SYN-ACK: server responds acknowledging client's SYN and sending its own SYN. 3) ACK: client acknowledges server's SYN. Connection is established.",
        "Easy",
        "Concept",
        "",
        "How is a TCP connection terminated (Four-way handshake FIN-ACK)?"
    ),
    (
        "What is the difference between TCP and UDP?",
        "TCP is connection-oriented, reliable, guarantees packet ordering and delivery via acknowledgments and retransmissions, with flow and congestion control (used by HTTP, SSH, FTP). UDP is connectionless, fast, lightweight, with no delivery guarantee or ordering (used by DNS, video streaming, online gaming).",
        "Easy",
        "Comparison",
        "",
        "Why is HTTP/3 built on UDP (QUIC) instead of TCP?"
    ),
    (
        "What is the difference between IPv4 and IPv6?",
        "IPv4 uses 32-bit addresses formatted as 4 decimal octets (e.g. `192.168.1.1`), providing ~4.3 billion addresses. IPv6 uses 128-bit addresses formatted as 8 hexadecimal groups (e.g. `2001:0db8::1`), providing virtually unlimited unique IP addresses.",
        "Easy",
        "Comparison",
        "",
        "Why was IPv6 created?"
    ),
    (
        "What is the difference between HTTP and HTTPS?",
        "HTTP transfers data as plaintext over port 80, vulnerable to eavesdropping and tampering. HTTPS encrypts data using TLS (Transport Layer Security) over port 443, ensuring confidentiality (encryption), integrity (no tampering), and authentication (identity verified via certificates).",
        "Easy",
        "Comparison",
        "",
        "What is a Certificate Authority (CA) in HTTPS?"
    ),
    (
        "What is a TLS/SSL Certificate and how does it verify a website's identity?",
        "A digital certificate issued by a trusted Certificate Authority (CA) binding a public key to an organization's domain name, allowing browsers to verify server authenticity and encrypt data.",
        "Easy",
        "Concept",
        "",
        "What is Let's Encrypt?"
    ),
    (
        "What is the difference between symmetric and asymmetric encryption in HTTPS?",
        "Asymmetric encryption (public/private key pair) is slow and used during the initial TLS handshake to authenticate the server and securely exchange a shared session key. Symmetric encryption (same shared key) is fast and used to encrypt all actual web traffic.",
        "Intermediate",
        "Comparison",
        "",
        "Why not use asymmetric encryption for all data transmission?"
    ),
    (
        "Compare HTTP/1.1, HTTP/2, and HTTP/3.",
        "HTTP/1.1: textual protocol with persistent Keep-Alive connections, but suffers from Head-of-Line (HoL) blocking. HTTP/2: binary protocol with multiplexing (multiple requests over 1 TCP connection), header compression (HPACK), and server push. HTTP/3: runs over QUIC (UDP), eliminating TCP-level HoL blocking and providing faster connection handshakes.",
        "Intermediate",
        "Comparison",
        "",
        "What is Head-of-Line (HoL) blocking?"
    ),
    (
        "What is multiplexing in HTTP/2?",
        "Multiplexing allows interleaving multiple independent bidirectional request and response streams concurrently over a single TCP connection, eliminating the HTTP/1.1 constraint where each request blocked subsequent requests on that connection.",
        "Intermediate",
        "Concept",
        "",
        "How did multiplexing eliminate the need for frontend hacks like domain sharding and CSS sprites?"
    ),
    (
        "What is Latency vs Bandwidth vs Throughput?",
        "Latency: the time taken for a data packet to travel from source to destination (measured in ms). Bandwidth: the maximum theoretical data transfer capacity of a network link (e.g. 100 Mbps). Throughput: the actual rate of data successfully delivered over the network.",
        "Easy",
        "Comparison",
        "",
        "Can high bandwidth fix high latency?"
    ),
    (
        "What is a CDN (Content Delivery Network) and how does it improve website performance?",
        "A CDN is a geographically distributed network of proxy servers that caches static assets (images, CSS, JS, videos) close to end-users (Edge servers), drastically reducing round-trip latency, server load, and bandwidth costs.",
        "Easy",
        "Concept",
        "",
        "Name two major CDN providers (e.g. Cloudflare, CloudFront)."
    ),
    (
        "What is Client-Server Architecture?",
        "A distributed computing model where client devices (browsers, mobile apps) request resources and services over a network, and centralized server systems process requests, manage databases, and return responses.",
        "Easy",
        "Concept",
        "",
        "What is a peer-to-peer (P2P) architecture in contrast?"
    ),
    (
        "What is a Reverse Proxy and how does it differ from a Forward Proxy?",
        "A Forward Proxy sits in front of clients to route client requests out to the internet (protecting client identity, filtering content). A Reverse Proxy (like NGINX) sits in front of web servers to receive incoming requests, handle SSL termination, load balancing, caching, and route to internal services.",
        "Intermediate",
        "Comparison",
        "",
        "Why is NGINX commonly used as a reverse proxy for Node.js apps?"
    ),
    (
        "What is Load Balancing and what are common load balancing algorithms?",
        "Distributing incoming network traffic across multiple backend servers to ensure no single server is overwhelmed. Algorithms: Round Robin, Weighted Round Robin, Least Connections, IP Hash, and Random.",
        "Intermediate",
        "Concept",
        "",
        "What is session persistence (sticky sessions) in load balancing?"
    ),
    (
        "What is the difference between Stateful and Stateless architecture?",
        "Stateless: every request contains all information needed to process it; the server retains no client state between requests (e.g. REST with JWT). Stateful: the server retains client context across requests (e.g. server-side sessions stored in memory).",
        "Easy",
        "Comparison",
        "",
        "Why is stateless architecture easier to scale horizontally?"
    ),
    (
        "What is Horizontal Scaling vs Vertical Scaling?",
        "Vertical Scaling (Scale Up): adding more CPU, RAM, or storage to an existing server machine. Horizontal Scaling (Scale Out): adding more server instances to a pool managed by a load balancer.",
        "Easy",
        "Comparison",
        "",
        "Which scaling method has hardware limits?"
    ),
    (
        "Which protocol operates at the Application Layer of the OSI model?",
        "HTTP operates at Layer 7 (Application Layer).",
        "Easy",
        "MCQ",
        "",
        {"A": "TCP", "B": "IP", "C": "HTTP", "D": "Ethernet"},
        "C",
        "What layer does TCP operate at (Transport Layer)?"
    ),
    (
        "What is an IP Port number?",
        "A 16-bit number (0-65535) identifying a specific process or network service on a host (e.g. port 80 for HTTP, 443 for HTTPS, 22 for SSH, 3000/5000 for local web apps).",
        "Easy",
        "Concept",
        "",
        "What is the range of well-known system ports (0 to 1023)?"
    ),

    # --- Browser Architecture & Critical Rendering Path (45 items) ---
    (
        "What is the Critical Rendering Path (CRP)?",
        "The sequence of steps the browser takes to convert HTML, CSS, and JavaScript into actual pixels rendered on the screen: 1) Parse HTML -> DOM Tree. 2) Parse CSS -> CSSOM Tree. 3) Combine DOM + CSSOM -> Render Tree. 4) Layout (compute geometry/positions). 5) Paint (draw pixels). 6) Composite (layer composition).",
        "Intermediate",
        "Concept",
        "",
        "Which steps in the CRP are most computationally expensive?"
    ),
    (
        "What is the difference between the DOM (Document Object Model) and CSSOM (CSS Object Model)?",
        "The DOM is an object tree representation of the HTML document structure and elements. The CSSOM is an object tree representing all CSS style rules and their cascading inheritance mapped to selectors.",
        "Easy",
        "Comparison",
        "",
        "Can the browser render the page before the CSSOM is completely constructed?"
    ),
    (
        "Why is CSS considered a 'render-blocking' resource?",
        "Browsers will not render any content until the CSSOM is fully downloaded and parsed. Displaying HTML without CSS would cause a Flash of Unstyled Content (FOUC) and require immediate costly re-layout.",
        "Easy",
        "Concept",
        "",
        "How can critical CSS be optimized to prevent render blocking?"
    ),
    (
        "Why is traditional JavaScript considered 'parser-blocking'?",
        "When the HTML parser encounters a `<script>` tag without `defer` or `async`, HTML parsing stops immediately. The browser must download and execute the script before resuming HTML parsing, because the script might call `document.write()` or modify the DOM.",
        "Easy",
        "Concept",
        "",
        "What script attributes prevent parser blocking?"
    ),
    (
        "Explain the differences between `<script>`, `<script async>`, and `<script defer>`.",
        "`<script>`: pauses HTML parsing, downloads script, executes immediately, then resumes HTML. `<script async>`: downloads in background without pausing HTML parsing, but executes immediately as soon as downloaded (pausing HTML, unordered). `<script defer>`: downloads in background without pausing HTML, and executes only after HTML parsing completes, in document order.",
        "Intermediate",
        "Comparison",
        "<script src='app.js' defer></script>\n<script src='analytics.js' async></script>",
        "Which script attribute is preferred for application scripts that depend on the DOM?"
    ),
    (
        "What is Reflow (Layout) vs Repaint (Redraw)?",
        "Reflow (Layout): recalculating the geometric positions and dimensions of elements in the document. Repaint: redrawing pixels on screen when visual appearance changes without altering geometry (e.g. `color`, `background-color`). Reflow is significantly more computationally expensive and always triggers a repaint.",
        "Intermediate",
        "Comparison",
        "",
        "Does changing `font-size` trigger reflow or repaint?"
    ),
    (
        "Which CSS properties trigger only Compositing (GPU) without causing Reflow or Repaint?",
        "`transform` and `opacity`. When animated, these properties are handled directly by the GPU on separate compositor layers, enabling smooth 60fps animations.",
        "Intermediate",
        "Practical",
        "// High performance animation\ntransform: translate3d(100px, 0, 0);\nopacity: 0.8;",
        "Why should you animate `transform` instead of `left` / `top`?"
    ),
    (
        "What is the CSS `will-change` property?",
        "A CSS hint that informs the browser in advance that an element's property (e.g. `will-change: transform`) is expected to change, allowing the browser to optimize and promote the element to its own GPU compositor layer.",
        "Intermediate",
        "Concept",
        ".animated-box {\n  will-change: transform, opacity;\n}",
        "Why should `will-change` not be applied to too many elements?"
    ),
    (
        "What is the difference between Core Web Vitals LCP, INP, and CLS?",
        "LCP (Largest Contentful Paint): measures loading performance (time to render largest visible element, ideal < 2.5s). INP (Interaction to Next Paint): measures interactivity responsiveness to user clicks/keys (ideal < 200ms). CLS (Cumulative Layout Shift): measures visual stability against unexpected layout shifts (ideal < 0.1).",
        "Intermediate",
        "Concept",
        "",
        "What metric did INP replace in March 2024 (FID — First Input Delay)?"
    ),
    (
        "What causes Cumulative Layout Shift (CLS) and how do you prevent it?",
        "Causes: images/videos without explicit width and height dimensions, dynamic ads injected above content, FOIT/FOUT web fonts. Prevention: always include `width` and `height` attributes on `<img>` tags and use `aspect-ratio` CSS property.",
        "Easy",
        "Practical",
        "<img src='hero.jpg' width='800' height='400' alt='Hero' />",
        "How does setting width/height on img tags prevent layout shifts before the image downloads?"
    ),
    (
        "What is the resource hint `<link rel='preload'>`?",
        "`preload` tells the browser to download a high-priority resource (e.g. critical font, hero image, main bundle) immediately because it will be needed on the current page soon.",
        "Easy",
        "Practical",
        "<link rel='preload' href='font.woff2' as='font' type='font/woff2' crossorigin>",
        "What happens if a preloaded resource is not used within 3 seconds?"
    ),
    (
        "What is the difference between `<link rel='preload'>` and `<link rel='prefetch'>`?",
        "`preload` downloads critical resources needed for the CURRENT page with high priority. `prefetch` downloads resources in idle time that are likely needed for the NEXT navigation (future page).",
        "Easy",
        "Comparison",
        "",
        "When would you use prefetch?"
    ),
    (
        "What is `<link rel='preconnect'>`?",
        "It tells the browser to initiate an early connection (DNS lookup, TCP handshake, and TLS negotiation) to a third-party domain before the actual request is issued, saving round-trip time.",
        "Easy",
        "Practical",
        "<link rel='preconnect' href='https://fonts.googleapis.com'>",
        "How is `dns-prefetch` different from `preconnect`?"
    ),
    (
        "What is Flash of Unstyled Text (FOUT) vs Flash of Invisible Text (FOIT)?",
        "FOIT: text is invisible while custom web font downloads. FOUT: text is displayed immediately in fallback system font, then shifts to custom font once loaded. Controlled via `font-display: swap`.",
        "Intermediate",
        "Comparison",
        "@font-face {\n  font-family: 'MyFont';\n  src: url('/fonts/myfont.woff2');\n  font-display: swap;\n}",
        "Which `font-display` value eliminates FOIT by displaying fallback text immediately?"
    ),
    (
        "What are browser layout thrashing and forced synchronous layout?",
        "When JavaScript reads geometry properties (`offsetWidth`, `clientHeight`, `scrollTop`) immediately after modifying DOM styles in a loop, forcing the browser to perform a synchronous reflow before continuing JS execution.",
        "Intermediate",
        "Concept",
        "// BAD: Layout Thrashing\nfor (let i = 0; i < items.length; i++) {\n  items[i].style.width = container.offsetWidth + 'px'; // Read then write in loop!\n}",
        "How do you fix layout thrashing?"
    ),
    (
        "How do you prevent layout thrashing?",
        "Batch all DOM reads first, and batch all DOM writes together afterwards (or use `requestAnimationFrame`).",
        "Easy",
        "Practical",
        "// GOOD: Batch reads then writes\nconst targetWidth = container.offsetWidth;\nfor (let i = 0; i < items.length; i++) {\n  items[i].style.width = targetWidth + 'px';\n}",
        "What utility library automates read/write batching (FastDOM)?"
    ),
    (
        "What is `requestAnimationFrame` (rAF)?",
        "`window.requestAnimationFrame(callback)` tells the browser you wish to perform an animation and requests the browser to call the callback function immediately before the next repaint (typically 60 times/sec).",
        "Easy",
        "Concept",
        "",
        "Why is `requestAnimationFrame` superior to `setInterval` for animations?"
    ),
    (
        "What is `requestIdleCallback`?",
        "`window.requestIdleCallback(callback)` schedules low-priority background tasks (like analytics, cache warmup) to execute only when the browser is idle during a frame, preventing main-thread blocking.",
        "Intermediate",
        "Concept",
        "",
        "What happens if the browser never becomes idle (timeout option)?"
    ),
    (
        "What is the main thread in a browser?",
        "The single thread where the browser parses HTML, computes CSS, runs JavaScript, handles user input events, and performs layout and painting.",
        "Easy",
        "Concept",
        "",
        "What happens to UI responsiveness when heavy JavaScript blocks the main thread?"
    ),
    (
        "What is Web Worker and how does it prevent main-thread blocking?",
        "A Web Worker runs JavaScript code in a separate background thread off the main thread, allowing heavy computations (data processing, encryption, parsing) without freezing the UI. Workers communicate via `postMessage()`.",
        "Intermediate",
        "Concept",
        "const worker = new Worker('worker.js');\nworker.postMessage({ data: largeArray });\nworker.onmessage = (e) => console.log('Result:', e.data);",
        "Can a Web Worker directly access or manipulate the DOM?"
    ),

    # --- Client-Side Storage & State (35 items) ---
    (
        "Compare Cookies, LocalStorage, SessionStorage, and IndexedDB.",
        "Cookies: 4KB capacity, sent automatically with every HTTP request to matching domain, support HttpOnly and SameSite. LocalStorage: 5-10MB, synchronous, string-only, persists until cleared. SessionStorage: 5MB, tab-scoped lifetime. IndexedDB: 250MB+ (or GBs), asynchronous, transactional, stores complex objects.",
        "Easy",
        "Comparison",
        "",
        "Which storage is automatically sent to the server with every HTTP request?"
    ),
    (
        "What are the security attributes of an HTTP Cookie?",
        "`HttpOnly`: prevents JavaScript from accessing `document.cookie` (mitigates XSS token theft). `Secure`: cookie is only transmitted over HTTPS. `SameSite`: controls whether cookie is sent with cross-site requests (`Strict`, `Lax`, `None`). `Domain`/`Path`: restricts cookie scope.",
        "Easy",
        "Concept",
        "Set-Cookie: token=xyz; Secure; HttpOnly; SameSite=Strict; Max-Age=3600",
        "Which attribute prevents JavaScript from reading a session cookie?"
    ),
    (
        "Explain `SameSite` cookie attribute values: `Strict`, `Lax`, and `None`.",
        "`Strict`: cookie is never sent with cross-site requests (even clicking an external link to your site). `Lax` (modern default): cookie is sent when navigating to top-level site via safe GET links, but blocked on cross-site POST/images. `None`: sent with all cross-site requests (requires `Secure`).",
        "Intermediate",
        "Comparison",
        "",
        "Why is `SameSite=Lax` or `Strict` critical for CSRF prevention?"
    ),
    (
        "Why is storing sensitive JWT authentication tokens in `localStorage` dangerous?",
        "`localStorage` is accessible to ANY JavaScript running on the page. If the application has any Cross-Site Scripting (XSS) vulnerability or compromised third-party script/npm package, attackers can steal the JWT instantly via `localStorage.getItem('token')`.",
        "Easy",
        "Concept",
        "",
        "Where is the most secure place to store authentication tokens (HttpOnly cookie)?"
    ),
    (
        "What is the lifetime of `sessionStorage`?",
        "`sessionStorage` persists for the duration of the browser tab/window session. Closing the tab deletes all sessionStorage data. Opening the same URL in a new tab creates a fresh, separate storage session.",
        "Easy",
        "Concept",
        "",
        "Does duplicating a tab in Chrome copy sessionStorage?"
    ),
    (
        "What are the limitations of `localStorage`?",
        "1) Synchronous API that blocks the main thread on large read/writes. 2) Limited capacity (5MB). 3) Can only store strings (requires `JSON.stringify`/`JSON.parse`). 4) Inaccessible from Web Workers. 5) Vulnerable to XSS theft.",
        "Easy",
        "Concept",
        "",
        "What storage alternative solves the synchronous blocking issue (IndexedDB)?"
    ),
    (
        "What is IndexedDB and when should it be used?",
        "IndexedDB is an asynchronous, transactional, client-side NoSQL object store capable of storing gigabytes of structured data (objects, files, Blobs) with index-based searching. It is ideal for offline Progressive Web Apps (PWAs).",
        "Intermediate",
        "Concept",
        "",
        "What popular lightweight wrapper library simplifies IndexedDB (idb)?"
    ),
    (
        "What is the Cache API and how is it used with Service Workers?",
        "The Cache API provides a storage mechanism for Request/Response pairs, allowing Service Workers to cache network responses and serve assets offline without contacting the network.",
        "Intermediate",
        "Concept",
        "const cache = await caches.open('v1');\nawait cache.addAll(['/index.html', '/styles.css', '/app.js']);",
        "Where can the Cache API be accessed (window and Service Workers)?"
    ),
    (
        "What is a Service Worker and what are its core lifecycle events?",
        "A Service Worker is an event-driven background script running independently of web pages that acts as a client-side programmable network proxy. Lifecycle: Register -> Install -> Activate -> Idle (handles `fetch`, `push`, `sync` events).",
        "Intermediate",
        "Concept",
        "navigator.serviceWorker.register('/sw.js');",
        "Can a Service Worker run over non-HTTPS origins (except localhost)?"
    ),
    (
        "What is the difference between Cache-Control `no-cache` and `no-store`?",
        "`no-cache` instructs the browser that it may store the asset in cache, but MUST revalidate with the server (using ETag or If-Modified-Since) before using it. `no-store` forbids storing the asset anywhere in cache, requiring a full download every time.",
        "Intermediate",
        "Comparison",
        "Cache-Control: no-cache\nCache-Control: no-store",
        "Which header should be used for highly confidential banking pages?"
    ),

    # --- Web Security & Privacy (45 items) ---
    (
        "What is the Same-Origin Policy (SOP)?",
        "A critical browser security mechanism that restricts a document or script loaded from one origin from accessing or interacting with resources from another origin, unless explicitly allowed (via CORS).",
        "Easy",
        "Concept",
        "",
        "What three components define an 'origin' in web security?"
    ),
    (
        "What three components determine whether two URLs share the same origin?",
        "1) Protocol (Scheme, e.g. `https://`). 2) Hostname / Domain (e.g. `example.com`). 3) Port number (e.g. `443` or `3000`). All three must match exactly.",
        "Easy",
        "Concept",
        "// Same origin: https://example.com/page1 and https://example.com/page2\n// Different: http:// vs https:// (protocol)\n// Different: example.com vs api.example.com (subdomain)\n// Different: example.com:3000 vs example.com:5000 (port)",
        "Do `http://localhost:3000` and `http://localhost:5000` share the same origin?"
    ),
    (
        "What is Cross-Origin Resource Sharing (CORS)?",
        "An HTTP-header-based mechanism that allows a server to explicitly indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources.",
        "Easy",
        "Concept",
        "Access-Control-Allow-Origin: https://myfrontend.com\nAccess-Control-Allow-Methods: GET, POST, PUT, DELETE\nAccess-Control-Allow-Headers: Content-Type, Authorization",
        "Does CORS protect the client or the server?"
    ),
    (
        "What is a CORS Preflight Request?",
        "An automatic `OPTIONS` HTTP request sent by the browser before a 'non-simple' cross-origin request (e.g. requests with `PUT`, `DELETE`, custom headers, or `application/json`), verifying with the server if the actual request is permitted.",
        "Intermediate",
        "Concept",
        "",
        "What makes a request a 'Simple Request' that skips preflight?"
    ),
    (
        "What is Cross-Site Scripting (XSS)?",
        "A security vulnerability where an attacker injects malicious client-side JavaScript into a trusted website, allowing the script to execute in victim users' browsers and steal session tokens, cookies, or manipulate page content.",
        "Easy",
        "Concept",
        "",
        "What are the three main types of XSS attacks?"
    ),
    (
        "Explain Stored XSS vs Reflected XSS vs DOM-based XSS.",
        "Stored XSS: malicious script is permanently saved in the database (e.g. comment field) and served to all viewing users. Reflected XSS: malicious script is reflected off the web server in response to user input (e.g. search query in URL). DOM-based XSS: vulnerability exists entirely in client-side JS writing unsanitized input into DOM sinks (like `innerHTML`).",
        "Intermediate",
        "Comparison",
        "",
        "Which type of XSS does NOT touch the backend server at all?"
    ),
    (
        "How does React protect against Cross-Site Scripting (XSS) by default?",
        "React automatically escapes all string values embedded in JSX expressions `{variable}` before rendering them to the DOM, converting characters like `<`, `>`, `&`, `\"` into HTML entities.",
        "Easy",
        "Concept",
        "const malicious = '<script>alert(1)</script>';\nreturn <div>{malicious}</div>; // Rendered safely as text!",
        "What React prop bypasses this built-in protection (dangerouslySetInnerHTML)?"
    ),
    (
        "What is Cross-Site Request Forgery (CSRF)?",
        "An attack where a malicious website tricks an authenticated user's browser into sending an unauthorized, forged HTTP request (with user's cookies automatically attached) to a vulnerable target site where the user is currently logged in.",
        "Easy",
        "Concept",
        "<!-- On evil.com -->\n<form action='https://bank.com/transfer' method='POST'>\n  <input type='hidden' name='amount' value='1000' />\n</form>",
        "What prevents CSRF attacks?"
    ),
    (
        "How do Anti-CSRF Tokens protect against CSRF attacks?",
        "The server generates a unique, unpredictable, secret token tied to the user's session and embeds it in forms. When submitting, the server verifies the token. Since third-party malicious sites cannot read or predict the token (due to Same-Origin Policy), forged requests fail.",
        "Intermediate",
        "Concept",
        "",
        "Why does SameSite=Strict cookie attribute also mitigate CSRF?"
    ),
    (
        "What is Content Security Policy (CSP)?",
        "An HTTP response header (`Content-Security-Policy`) that allows site administrators to declare approved sources of content (scripts, stylesheets, images, fonts, frames) that the browser is permitted to load, severely mitigating XSS and clickjacking.",
        "Intermediate",
        "Concept",
        "Content-Security-Policy: default-src 'self'; script-src 'self' https://apis.google.com; img-src 'self' data:;",
        "What directive disables execution of inline `<script>` tags by default in CSP?"
    ),
    (
        "What is Clickjacking and how is it prevented?",
        "An attack where an attacker transparently overlays an invisible `<iframe>` of a target site over a malicious page, tricking the user into clicking buttons on the embedded site. Prevented using CSP `frame-ancestors 'none'` or `X-Frame-Options: DENY`.",
        "Easy",
        "Concept",
        "X-Frame-Options: DENY\n# or\nContent-Security-Policy: frame-ancestors 'none';",
        "Which header is preferred in modern applications?"
    ),
    (
        "What is SQL Injection and how is it prevented in backend code?",
        "An attack where malicious SQL statements are inserted into input fields to manipulate database queries. Prevented by using Parameterized Queries (Prepared Statements) or ORMs/ODMs (like Mongoose, Prisma) instead of concatenating raw SQL strings.",
        "Easy",
        "Concept",
        "// BAD: Raw concatenation\n`SELECT * FROM users WHERE name = '${userInput}'`;\n// GOOD: Parameterized\ndb.query('SELECT * FROM users WHERE name = ?', [userInput]);",
        "Can SQL injection occur in MongoDB (NoSQL Injection)?"
    ),
    (
        "What is NoSQL Injection in MongoDB?",
        "An attack where malicious JSON query operators (like `{\"username\": {\"$ne\": null}}`) are passed in place of string values to bypass authentication checks.",
        "Intermediate",
        "Concept",
        "// Attack body: { \"username\": \"admin\", \"password\": { \"$gt\": \"\" } }\n// Solved by validating that input is strictly a string",
        "How do libraries like `mongo-sanitize` prevent NoSQL injection?"
    ),
    (
        "What is HSTS (HTTP Strict Transport Security)?",
        "A response header (`Strict-Transport-Security: max-age=31536000; includeSubDomains`) that forces browsers to only connect to the website via HTTPS, automatically upgrading any HTTP links before making requests.",
        "Intermediate",
        "Concept",
        "Strict-Transport-Security: max-age=63072000; includeSubDomains; preload",
        "What attack does HSTS prevent (SSL stripping / man-in-the-middle)?"
    ),
    (
        "Why should passwords never be stored in plaintext and what is Salted Password Hashing?",
        "Plaintext passwords can be stolen in database breaches. Passwords should be hashed using slow, adaptive one-way cryptographic algorithms (like bcrypt or Argon2) with a unique random salt per user to prevent Rainbow Table attacks.",
        "Easy",
        "Concept",
        "const hash = await bcrypt.hash(password, 10);",
        "What is a salt in password hashing?"
    ),

    # --- Web APIs & Browser Capabilities (45 items) ---
    (
        "Compare WebSockets, Server-Sent Events (SSE), and Long Polling.",
        "WebSockets: full-duplex, bidirectional communication over a single TCP connection, ideal for chat and multiplayer games. SSE: unidirectional (server-to-client only) over standard HTTP, ideal for live feeds and stock tickers. Long Polling: client repeatedly sends HTTP requests that server holds until data is available, high overhead legacy fallback.",
        "Intermediate",
        "Comparison",
        "",
        "Which protocol uses `ws://` and `wss://` schemes?"
    ),
    (
        "What is the difference between `localStorage` and `sessionStorage`?",
        "`localStorage` data persists indefinitely until explicitly cleared by user or script. `sessionStorage` data is cleared automatically when the browser tab or window is closed.",
        "Easy",
        "Comparison",
        "",
        "What is the storage capacity of each (approx 5MB)?"
    ),
    (
        "What is the Fetch API and how does it handle HTTP errors (like 404 and 500)?",
        "The Fetch API provides a promise-based interface for making HTTP requests. Crucially, `fetch()` only rejects on network failures (like offline or DNS error); it does NOT reject on HTTP 404 or 500 status codes. You must manually check `response.ok`.",
        "Easy",
        "Concept",
        "const res = await fetch('/api/data');\nif (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);\nconst data = await res.json();",
        "What does `response.ok` check (status code in 200-299 range)?"
    ),
    (
        "What is the Beacon API (`navigator.sendBeacon`)?",
        "A lightweight browser API designed to send asynchronous analytics or diagnostic data to a server when the user is leaving or closing the page, guaranteed to complete without delaying page unload.",
        "Intermediate",
        "Concept",
        "window.addEventListener('visibilitychange', () => {\n  if (document.visibilityState === 'hidden') {\n    navigator.sendBeacon('/log', analyticsData);\n  }\n});",
        "Why is `sendBeacon` preferred over `fetch` during page unload?"
    ),
    (
        "What is the Intersection Observer API?",
        "An asynchronous browser API that detects when an element enters or exits the browser viewport (or an ancestor element), ideal for lazy-loading images, infinite scroll, and scroll spy navigation without expensive scroll event listeners.",
        "Easy",
        "Concept",
        "const observer = new IntersectionObserver(entries => {\n  entries.forEach(entry => {\n    if (entry.isIntersecting) {\n      img.src = img.dataset.src;\n      observer.unobserve(img);\n    }\n  });\n});\nobserver.observe(img);",
        "Why is Intersection Observer better than listening to window scroll events?"
    ),
    (
        "What is the Resize Observer API?",
        "A browser API that notifies you whenever a specific element's bounding box dimensions change, enabling responsive component-level adjustments independently of window resize.",
        "Intermediate",
        "Concept",
        "",
        "How is Resize Observer different from `window.onresize`?"
    ),
    (
        "What is the Mutation Observer API?",
        "A browser API that watches for changes made to the DOM tree (child node additions/deletions, attribute changes, character data changes) and invokes a callback.",
        "Intermediate",
        "Concept",
        "",
        "What legacy deprecated events did Mutation Observer replace (Mutation Events)?"
    ),
    (
        "What is a Progressive Web App (PWA) and what are its three fundamental requirements?",
        "A web application that offers app-like experiences using modern web capabilities. Core requirements: 1) HTTPS (secure context). 2) Web App Manifest (JSON describing app icons, name, display mode). 3) Service Worker (offline caching and background sync).",
        "Easy",
        "Concept",
        "",
        "What is the Web App Manifest file?"
    ),
    (
        "What is the `window.history` API and how does Client-Side Routing (SPA) work?",
        "The History API (`history.pushState()`, `history.replaceState()`, `window.onpopstate`) allows single-page applications to modify the browser URL and history stack without triggering a full page reload.",
        "Easy",
        "Concept",
        "history.pushState({ page: 2 }, 'Title', '/page2');",
        "Why does refreshing a client-side routed page require server-side fallback to index.html?"
    ),
    (
        "Why must a Single Page Application (SPA) web server be configured to rewrite all 404 paths to `index.html`?",
        "Because URLs like `/dashboard` exist only as client-side JavaScript routes in the browser. When directly requested from the server, the server has no `/dashboard.html` file and must return `index.html` so the client-side router can take over.",
        "Easy",
        "Concept",
        "",
        "What happens if this fallback is not configured on Netlify or NGINX?"
    )
]

print(f"Total Web Fundamentals questions created: {len(web_items)}")

with open('scripts/webfundamentals_questions.py', 'w', encoding='utf-8') as f:
    f.write('"""\nscripts/webfundamentals_questions.py\n215 comprehensive fresher Web Fundamentals interview questions.\n"""\n\n')
    f.write('web_items = [\n')
    for item in web_items:
        f.write(f"    {repr(item)},\n")
    f.write(']\n')

print("Saved to scripts/webfundamentals_questions.py")

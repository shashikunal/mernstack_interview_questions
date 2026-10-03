with open('scripts/backend_additions.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix 1
text = text.replace(
    '("How do you avoid maxBuffer truncation errors when handling large command outputs?", "Use child_process.spawn() and stream the output chunk-by-chunk from child.stdout rather than buffering in memory.", "Intermediate", "Best Practice", "", "Worker Threads MCQ: Which method transfers memory ownership between threads without copying data?", "Option B is correct. transferList transfers ArrayBuffers with zero-copy.", "Intermediate", "MCQ", "", {"A": "JSON.stringify", "B": "transferList", "C": "Atomics.copy", "D": "process.nextTick"}, "B", "What happens to the sender buffer?"),',
    '("How do you avoid maxBuffer truncation errors when handling large command outputs?", "Use child_process.spawn() and stream the output chunk-by-chunk from child.stdout rather than buffering in memory.", "Intermediate", "Best Practice", "", "Why use spawn for large output?"),\n    ("Worker Threads MCQ: Which method transfers memory ownership between threads without copying data?", "Option B is correct. transferList transfers ArrayBuffers with zero-copy.", "Intermediate", "MCQ", "", {"A": "JSON.stringify", "B": "transferList", "C": "Atomics.copy", "D": "process.nextTick"}, "B", "What happens to the sender buffer?"),'
)

# Fix 2
text = text.replace(
    '("Which protocol does DNS use by default?", "DNS queries typically use UDP on port 53 for speed and low overhead; fallback to TCP occurs for large responses (> 512 bytes) or zone transfers.", "Easy", "Concept", "", "HTTP Protocols MCQ: What transport layer protocol does HTTP/3 operate on?", "Option B is correct. HTTP/3 runs on QUIC over UDP.", "Easy", "MCQ", "", {"A": "TCP", "B": "UDP", "C": "SCTP", "D": "ICMP"}, "B", "What transport does HTTP/2 use?"),',
    '("Which protocol does DNS use by default?", "DNS queries typically use UDP on port 53 for speed and low overhead; fallback to TCP occurs for large responses (> 512 bytes) or zone transfers.", "Easy", "Concept", "", "When does DNS use TCP?"),\n    ("HTTP Protocols MCQ: What transport layer protocol does HTTP/3 operate on?", "Option B is correct. HTTP/3 runs on QUIC over UDP.", "Easy", "MCQ", "", {"A": "TCP", "B": "UDP", "C": "SCTP", "D": "ICMP"}, "B", "What transport does HTTP/2 use?"),'
)

# Fix 3
text = text.replace(
    '("What responsibilities does an API Gateway handle in backend architectures?", "Request routing, SSL termination, rate limiting, authentication/token verification, CORS handling, response caching, and request aggregation.", "Intermediate", "Architecture", "", "REST Design MCQ: Which HTTP method is both safe and idempotent according to RFC specifications?", "Option A is correct. GET does not mutate server state.", "Easy", "MCQ", "", {"A": "GET", "B": "POST", "C": "DELETE", "D": "PATCH"}, "A", "Is DELETE safe?"),',
    '("What responsibilities does an API Gateway handle in backend architectures?", "Request routing, SSL termination, rate limiting, authentication/token verification, CORS handling, response caching, and request aggregation.", "Intermediate", "Architecture", "", "What is reverse proxy?"),\n    ("REST Design MCQ: Which HTTP method is both safe and idempotent according to RFC specifications?", "Option A is correct. GET does not mutate server state.", "Easy", "MCQ", "", {"A": "GET", "B": "POST", "C": "DELETE", "D": "PATCH"}, "A", "Is DELETE safe?"),'
)

with open('scripts/backend_additions.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed backend_additions.py")

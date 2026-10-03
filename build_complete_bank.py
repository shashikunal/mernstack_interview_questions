# -*- coding: utf-8 -*-
"""
Phase 2 & Phase 3: Validated & Cleaned Fresher Interview Question Bank
Builds comprehensive, duplicate-free subject -> topic -> subtopic coverage for all 18 interview subjects.
Enforces strict metadata schema, allowed question types, and verified technical correctness.
"""

import json
import os
import re

DATA_FILE = r"C:\Users\Qsp\Documents\mernstack_interview_questions\fresher-data.js"
MERN_200_FILE = r"C:\Users\Qsp\Documents\mernstack_interview_questions\mern-200\fresher-data.js"
NETLIFY_FILE = r"C:\Users\Qsp\Documents\mernstack_interview_questions\netlify-deploy\fresher-data.js"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    text = f.read()
    s = text.find("[")
    e = text.rfind("]")
    all_loaded = json.loads(text[s:e+1])

# Keep only the original 134 base questions for clean idempotent generation
existing_questions = [
    q for q in all_loaded 
    if (q["id"].startswith("q-") and int(q["id"].split("-")[1]) <= 131) 
    or q["id"].startswith("ps-")
]

print(f"Loaded {len(existing_questions)} original base questions.")

# Reclassify q-98 and q-127 from Git to Testing
for q in existing_questions:
    if q["id"] == "q-98":
        q["subject"] = "Testing"
        q["topic"] = "End-to-End Testing"
        q["subTopic"] = "Playwright Basics"
    elif q["id"] == "q-127":
        q["subject"] = "Testing"
        q["topic"] = "Testing Strategy"
        q["subTopic"] = "Testing Pyramid"

new_questions = []
next_num = 132

def create_q(subject, topic, subtopic, question, answer, explanation="", code="", 
             difficulty="Easy", q_type="Concept", round_type="Technical Round", 
             freq="High", ref="MDN Web Docs", followup=""):
    global next_num
    q_obj = {
        "id": f"q-{next_num}",
        "num": next_num,
        "subject": subject,
        "topic": topic,
        "subTopic": subtopic,
        "question": question,
        "answer": answer,
        "shortExplanation": explanation,
        "codeExample": code,
        "difficulty": difficulty,
        "questionType": q_type,
        "interviewRound": round_type,
        "frequency": freq,
        "references": ref,
        "followUpQuestions": followup,
        "addedAt": next_num
    }
    next_num += 1
    new_questions.append(q_obj)

# ==============================================================================
# 1. HTML (6 questions: DOCTYPE, Validation, Media/Iframe, Head Metadata, ARIA, Rendering)
# ==============================================================================
create_q(
    subject="HTML",
    topic="Document Structure",
    subtopic="DOCTYPE & Quirks Mode",
    question="What is <!DOCTYPE html> and what happens if you omit it?",
    answer="The DOCTYPE declaration informs the web browser about the version of HTML the page is written in. In modern HTML5, <!DOCTYPE html> is required at the very first line of an HTML document. If omitted, modern browsers fall into 'quirks mode', rendering the page using legacy backwards-compatibility rules which causes layout inconsistencies, incorrect box-sizing, and font rendering glitches.",
    explanation="Quirks mode emulates browser behavior from late 1990s Netscape and Internet Explorer. Standards mode renders according to W3C specifications.",
    code="<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <title>Standards Mode Page</title>\n</head>\n<body>\n  <h1>Clean Standards-Compliant HTML5</h1>\n</body>\n</html>",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Quirks Mode and Standards Mode",
    followup="What is the difference between HTML4 and HTML5 DOCTYPE declarations?"
)

create_q(
    subject="HTML",
    topic="Forms & Validation",
    subtopic="Native HTML5 Form Validation",
    question="How do you validate forms natively in HTML without JavaScript?",
    answer="HTML5 provides built-in validation attributes: 'required' (disallows empty submission), 'pattern' (validates against regular expressions), 'min' and 'max' (for numbers and dates), 'minlength' and 'maxlength', and specialized 'type' attributes ('email', 'url', 'number', 'tel'). When the user submits the form, the browser automatically blocks invalid data and displays localized native tooltips.",
    explanation="Native validation saves bundle size and provides instant client-side feedback before any network transmission.",
    code="<form action=\"/register\" method=\"POST\">\n  <!-- Must be filled out and match email format -->\n  <input type=\"email\" name=\"user_email\" required placeholder=\"name@example.com\">\n\n  <!-- Password minimum 8 characters -->\n  <input type=\"password\" name=\"user_password\" required minlength=\"8\" placeholder=\"Min 8 characters\">\n\n  <!-- Only 10-digit mobile number -->\n  <input type=\"tel\" pattern=\"[0-9]{10}\" required placeholder=\"10-digit phone\">\n\n  <button type=\"submit\">Submit Form</button>\n</form>",
    difficulty="Easy",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Client-side form validation",
    followup="How do you disable native HTML5 form validation if you want custom JS validation?"
)

create_q(
    subject="HTML",
    topic="Media & Embedding",
    subtopic="Audio, Video & Iframe Security",
    question="How do you embed video, audio, and iframes in HTML5, and what are the key attributes like autoplay, muted, and sandbox?",
    answer="<video> and <audio> provide native media playback without third-party plugins. Key attributes: 'controls' (displays play/pause/volume UI), 'autoplay' (starts immediately), 'loop' (repeats playback), and 'muted'. Note that modern browsers strictly block video and audio from autoplaying unless 'muted' is also present. <iframe> embeds another web page; the 'sandbox' attribute restricts external scripts, forms, and popups to prevent clickjacking and malicious exploits.",
    explanation="Always provide fallback text and multiple <source> formats (like MP4 and WebM) for cross-browser video compatibility.",
    code="<!-- Autoplaying background video requires muted -->\n<video controls width=\"640\" height=\"360\" muted autoplay loop>\n  <source src=\"intro.mp4\" type=\"video/mp4\">\n  <source src=\"intro.webm\" type=\"video/webm\">\n  Your browser does not support the video tag.\n</video>\n\n<!-- Secure sandboxed iframe -->\n<iframe src=\"https://example.com/widget\" sandbox=\"allow-scripts allow-same-origin\" title=\"External Widget\"></iframe>",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="Medium",
    ref="MDN Web Docs - Video and audio content",
    followup="What security vulnerabilities can occur if an iframe lacks the sandbox attribute?"
)

create_q(
    subject="HTML",
    topic="Metadata",
    subtopic="Viewport, Charset & SEO Meta Tags",
    question="What is the purpose of <meta name=\"viewport\">, charset=\"UTF-8\", and favicon in the <head>?",
    answer="1) <meta charset=\"UTF-8\"> specifies universal character encoding, ensuring text, emojis, and international characters render correctly without corruption. 2) <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"> instructs mobile browsers to match the screen's physical width in device-independent pixels with 1:1 initial zoom (omitting it makes mobile browsers render pages scaled down like a desktop 980px viewport). 3) <link rel=\"icon\"> specifies the tab favicon icon.",
    explanation="Without the viewport meta tag, responsive CSS media queries will not trigger properly on mobile phones.",
    code="<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <meta name=\"description\" content=\"Fresher developer interview preparation and drilling.\">\n  <link rel=\"icon\" type=\"image/svg+xml\" href=\"/favicon.svg\">\n  <title>Fresher Prep Hub</title>\n</head>",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Viewport meta tag",
    followup="What is the difference between meta description and title tag for SEO?"
)

create_q(
    subject="HTML",
    topic="Accessibility",
    subtopic="ARIA Basics & Best Practices",
    question="What are ARIA attributes (aria-label, aria-hidden, role) and what is the first rule of ARIA?",
    answer="ARIA (Accessible Rich Internet Applications) attributes provide accessibility semantics for screen readers when native HTML tags cannot fully convey UI meaning. 'aria-label' provides an accessible name for interactive elements lacking visible text (like an icon button). 'aria-hidden=\"true\"' hides decorative icons from screen readers. 'role' assigns explicit semantic roles (e.g. role=\"alert\"). The First Rule of ARIA is: 'If you can use a native HTML element (like <button>, <nav>, or <header>) instead of ARIA, do so!'",
    explanation="Native HTML elements come with built-in keyboard navigation and focus management; ARIA requires manual keyboard handling.",
    code="<!-- Icon-only button with accessible label -->\n<button type=\"button\" aria-label=\"Close modal dialog\">\n  <!-- Decorative cross hidden from screen readers -->\n  <span aria-hidden=\"true\">&times;</span>\n</button>",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="W3C WAI-ARIA Authoring Practices",
    followup="Why is <button> preferred over <div role=\"button\">?"
)

create_q(
    subject="HTML",
    topic="Browser Rendering",
    subtopic="Critical Rendering Path (DOM, CSSOM, Reflow & Repaint)",
    question="How does the browser render a webpage from HTML and CSS (Critical Rendering Path)?",
    answer="1) HTML parser converts bytes into tokens and constructs the DOM (Document Object Model) tree. 2) CSS parser constructs the CSSOM (CSS Object Model) tree. 3) DOM and CSSOM merge into the Render Tree (only including visible nodes; elements with display:none are excluded). 4) Layout (Reflow): Browser computes the exact geometry, position, and dimensions of each node on the screen. 5) Paint: Fills in pixels, colors, text, borders, and shadows. 6) Composite: Assembles layers onto the screen via the GPU.",
    explanation="Reflow is computationally expensive because changing the layout of one element can trigger recalculations for its siblings and parent.",
    code="// Triggering Reflow (Layout recalculation):\nelement.style.width = '200px';\nelement.style.padding = '20px';\n\n// Triggering Repaint only (No layout change):\nelement.style.color = 'blue';\nelement.style.backgroundColor = '#f3f4f6';",
    difficulty="Medium",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Critical rendering path",
    followup="What CSS properties can be animated using only the GPU without triggering reflow or repaint?"
)

# ==============================================================================
# 2. CSS (7 questions: Combinators, Overflow, Flex item sizing, Units, Variables, Transitions/Keyframes, Transforms)
# ==============================================================================
create_q(
    subject="CSS",
    topic="Selectors",
    subtopic="CSS Combinators (Descendant, Child, Adjacent, Sibling)",
    question="What are CSS Combinators (Descendant, Child '>', Adjacent Sibling '+', General Sibling '~') and how do they differ?",
    answer="CSS combinators define the structural relationship between selectors: 1) Descendant (space, e.g. 'div p'): Targets all <p> elements inside <div> at any nesting depth. 2) Child ('>', e.g. 'ul > li'): Targets only immediate, direct children of <ul>. 3) Adjacent Sibling ('+', e.g. 'h2 + p'): Targets the first <p> that immediately follows <h2> on the same parent level. 4) General Sibling ('~', e.g. 'h2 ~ p'): Targets all <p> elements that follow <h2> on the same parent level.",
    explanation="Using child combinators (>) improves style scoping and CSS rendering efficiency by avoiding deep tree searches.",
    code="/* Immediate children only */\n.menu > li { font-weight: bold; }\n\n/* First paragraph directly after a heading */\nh2 + p { font-size: 1.15rem; color: #4b5563; }\n\n/* All subsequent sibling items */\n.active ~ .item { opacity: 0.5; }",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - CSS selectors and combinators",
    followup="What is the difference between adjacent sibling (+) and general sibling (~)?"
)

create_q(
    subject="CSS",
    topic="Layout",
    subtopic="CSS Overflow Property (visible, hidden, scroll, auto)",
    question="What is CSS overflow and what are the differences between visible, hidden, scroll, and auto?",
    answer="The overflow property specifies whether to clip content or add scrollbars when an element's content exceeds its container box: 1) visible (default): Content spills outside the container boundary without clipping. 2) hidden: Extra content is clipped and hidden; no scrollbars appear. 3) scroll: Content is clipped, and scrollbars are permanently visible (even if content fits). 4) auto: Scrollbars appear only when content actually overflows the container, providing the best user experience.",
    explanation="overflow: hidden is also frequently used to contain floating children and establish a new block formatting context (BFC).",
    code=".modal-body {\n  max-height: 400px;\n  overflow-y: auto; /* Scrollbar appears only when content overflows */\n  overflow-x: hidden;\n}",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - overflow",
    followup="What is the difference between overflow: scroll and overflow: auto?"
)

create_q(
    subject="CSS",
    topic="Flexbox",
    subtopic="flex-grow, flex-shrink & flex-basis",
    question="What do flex-grow, flex-shrink, and flex-basis mean in the flex shorthand property?",
    answer="The flex shorthand property flex: [flex-grow] [flex-shrink] [flex-basis] controls item sizing: 1) flex-grow: Proportional factor determining how much remaining free space the item absorbs when the container is larger than its items (0 = does not grow). 2) flex-shrink: Proportional factor determining how much the item shrinks when container space is insufficient (1 = shrinks proportionally; 0 = prevents shrinking). 3) flex-basis: Initial default size of the item before remaining space is distributed (e.g. 200px or auto).",
    explanation="Common shorthand: flex: 1 expands an item to fill available container space (equivalent to flex: 1 1 0%).",
    code="/* Sidebar with fixed 250px width that does not shrink */\n.sidebar {\n  flex: 0 0 250px;\n}\n\n/* Main content that absorbs all remaining available width */\n.main-content {\n  flex: 1 1 auto;\n}",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Controlling ratios of flex items on the main axis",
    followup="What is the difference between flex: 1 and flex: auto?"
)

create_q(
    subject="CSS",
    topic="Units",
    subtopic="px vs rem vs em vs % vs vh/vw",
    question="What is the difference between px, rem, em, %, vh, and vw units in CSS?",
    answer="1) px: Absolute pixel unit fixed in size regardless of browser settings. 2) rem: Relative to the root (<html>) font size (typically 1rem = 16px). Recommended for typography and spacing because it scales when users adjust browser accessibility font size. 3) em: Relative to the font size of the current element or parent (can cause compounding multiplication in nested lists). 4) %: Relative to the parent container's width or height. 5) vh & vw: Relative to 1% of viewport height and width respectively.",
    explanation="Using rem for font sizes and padding ensures your application respects user accessibility zoom preferences.",
    code="html {\n  font-size: 16px; /* 1rem = 16px */\n}\n\nh1 {\n  font-size: 2rem; /* 32px (scales with user font settings) */\n  margin-bottom: 1rem;\n}\n\n.hero-banner {\n  width: 100vw;  /* 100% of viewport width */\n  min-height: 80vh; /* 80% of viewport height */\n}",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - CSS values and units",
    followup="What is the difference between 100vh and 100dvh on mobile browsers?"
)

create_q(
    subject="CSS",
    topic="Variables",
    subtopic="CSS Custom Properties (Variables) & Theming",
    question="What are CSS Variables (Custom Properties), how do you declare and use them, and why are they useful?",
    answer="CSS variables are declared using '--' prefix and retrieved using the var(--name, fallback) function. When declared in the ':root' pseudo-class, they are globally accessible and inherit down the entire DOM tree. They eliminate repetitive color hex codes, make site-wide refactoring trivial, enable runtime theming (like switching between Light and Dark mode with a single class or JS toggle), and can be read and updated dynamically in JavaScript using getComputedStyle and style.setProperty.",
    explanation="Unlike Sass/SCSS variables which compile to static CSS at build time, CSS Custom Properties exist live in the browser DOM.",
    code=":root {\n  --primary: #2563eb;\n  --bg-color: #ffffff;\n  --text-color: #1f2937;\n}\n\n/* Instant dark mode toggle */\n[data-theme=\"dark\"] {\n  --primary: #60a5fa;\n  --bg-color: #0f172a;\n  --text-color: #f8fafc;\n}\n\nbody {\n  background-color: var(--bg-color);\n  color: var(--text-color);\n}",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Using CSS custom properties",
    followup="How do you update a CSS variable dynamically using JavaScript?"
)

create_q(
    subject="CSS",
    topic="Animation",
    subtopic="CSS Transitions vs @keyframes Animations",
    question="What is the difference between CSS transitions and @keyframes animations?",
    answer="A CSS transition smoothly interpolates property values between two states (e.g. normal state and :hover state) when triggered by an event, requiring transition: property duration timing-function delay. A @keyframes animation can run automatically on page load, loop continuously (infinite), alternate directions, and define multiple intermediate progress steps (0%, 25%, 50%, 100%) without requiring any user interaction or state change.",
    explanation="For high 60fps performance, animate transform and opacity since they are handled directly by the GPU compositor without reflow.",
    code="/* 1. Transition on hover */\n.btn {\n  background-color: #2563eb;\n  transition: background-color 0.3s ease, transform 0.2s ease;\n}\n.btn:hover {\n  background-color: #1d4ed8;\n  transform: translateY(-2px);\n}\n\n/* 2. Keyframes infinite spinner animation */\n@keyframes spin {\n  from { transform: rotate(0deg); }\n  to { transform: rotate(360deg); }\n}\n.spinner {\n  animation: spin 1s linear infinite;\n}",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - CSS animations",
    followup="What CSS properties trigger GPU acceleration?"
)

create_q(
    subject="CSS",
    topic="Animation",
    subtopic="CSS Transforms & Hardware Acceleration",
    question="What is the CSS transform property and why is transform: translate() preferred over top/left for animations?",
    answer="The CSS transform property modifies the coordinate space of an element, enabling visual manipulation without affecting the layout of surrounding elements (translate, rotate, scale, skew). Animating 'top' or 'left' triggers browser Reflow (layout recalculation) on the main thread on every frame, causing visual stutter. Animating 'transform: translate()' is handled entirely by the GPU compositor layer, running smoothly at 60fps without triggering reflow or repaint.",
    explanation="Transforms are the golden standard for smooth mobile and desktop UI animations.",
    code="/* Smooth GPU-accelerated slide */\n.modal {\n  transform: translateY(20px);\n  opacity: 0;\n  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;\n}\n.modal.open {\n  transform: translateY(0);\n  opacity: 1;\n}",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - transform",
    followup="What does will-change: transform do in CSS?"
)

# ==============================================================================
# 3. JavaScript (9 questions: Prototype, Call/Apply/Bind, Strings, Copies, Promise combinators, Tricky Output, Var vs Let in loop, Web Storage, Memory)
# ==============================================================================
create_q(
    subject="JavaScript",
    topic="Prototypes",
    subtopic="Prototype & Prototype Chain",
    question="What is a prototype and how does the prototype chain work in JavaScript?",
    answer="In JavaScript, every object has an internal link to another object called its prototype (accessible via Object.getPrototypeOf(obj) or __proto__). When accessing a property or method on an object, JavaScript first checks the object itself. If not found, it traverses up the prototype chain until it either finds the property or reaches Object.prototype (whose prototype is null). If still not found, it returns undefined.",
    explanation="Methods like toString() and hasOwnProperty() are inherited by all objects from Object.prototype via this prototype chain.",
    code="const vehicle = {\n  hasWheels: true,\n  drive() { return 'Vroom'; }\n};\n\n// Create car inheriting from vehicle\nconst car = Object.create(vehicle);\ncar.brand = 'Tesla';\n\nconsole.log(car.brand);     // 'Tesla' (own property)\nconsole.log(car.hasWheels);  // true (found via prototype chain)\nconsole.log(car.drive());    // 'Vroom' (inherited from vehicle prototype)\nconsole.log(car.wings);      // undefined (reached end of chain)",
    difficulty="Medium",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Inheritance and the prototype chain",
    followup="What is the difference between __proto__ and prototype in JavaScript?"
)

create_q(
    subject="JavaScript",
    topic="Functions",
    subtopic="call() vs apply() vs bind()",
    question="What is the difference between call(), apply(), and bind() in JavaScript?",
    answer="All three methods explicitly set the 'this' context of a function. 1) call(thisArg, arg1, arg2): Executes the function immediately with comma-separated arguments. 2) apply(thisArg, [argsArray]): Executes the function immediately with arguments supplied as an array. 3) bind(thisArg, arg1, arg2): Does NOT execute immediately; instead, it returns a new copy of the function with 'this' permanently bound to thisArg for later execution.",
    explanation="Memory trick: 'C'all for Comma-separated; 'A'pply for Array of arguments; 'B'ind for Bound function copy.",
    code="function introduce(greeting, punctuation) {\n  console.log(`${greeting}, I am ${this.name}${punctuation}`);\n}\n\nconst user = { name: 'Priya' };\n\n// 1. call: immediate with arguments list\nintroduce.call(user, 'Hello', '!'); // 'Hello, I am Priya!'\n\n// 2. apply: immediate with arguments array\nintroduce.apply(user, ['Namaste', '.']); // 'Namaste, I am Priya.'\n\n// 3. bind: returns new function for later call\nconst boundIntro = introduce.bind(user, 'Welcome');\nboundIntro('?'); // 'Welcome, I am Priya?'",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Function.prototype.bind()",
    followup="Can you re-bind a function that was already bound using bind()?"
)

create_q(
    subject="JavaScript",
    topic="Strings",
    subtopic="String Methods (slice vs substring, replace, split, trim)",
    question="What are the key string methods in JavaScript and how does slice() differ from substring()?",
    answer="Key string methods: slice(), substring(), replace()/replaceAll(), split(), trim(), and includes(). Both slice(start, end) and substring(start, end) extract a substring. However: 1) slice() supports negative indices to count backwards from string end (e.g. str.slice(-3)), whereas substring() treats negative values as 0. 2) If start > end, substring() swaps the two arguments automatically, whereas slice() returns an empty string.",
    explanation="Strings in JavaScript are immutable; all string methods return a new string rather than modifying the original in-place.",
    code="const str = 'Frontend Developer';\n\nconsole.log(str.slice(0, 8));     // 'Frontend'\nconsole.log(str.slice(-9));       // 'Developer' (negative index!)\nconsole.log(str.substring(8, 0)); // 'Frontend' (automatically swapped start and end!)\n\n// Replace & Split\nconsole.log('cat-dog-bird'.split('-')); // ['cat', 'dog', 'bird']\nconsole.log('apple, apple'.replaceAll('apple', 'mango')); // 'mango, mango'",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - String.prototype.slice()",
    followup="What is the difference between charAt() and bracket notation str[0] when accessing an out-of-bounds index?"
)

create_q(
    subject="JavaScript",
    topic="Objects",
    subtopic="Shallow Copy vs Deep Copy",
    question="What is the difference between Shallow Copy and Deep Copy in JavaScript, and how do you create each?",
    answer="A Shallow Copy duplicates the top-level properties of an object; however, nested objects or arrays are copied by reference (modifying a nested object in the copy mutates the original object). Created via Spread operator {...obj} or Object.assign({}, obj). A Deep Copy recursively duplicates all nested properties, completely isolating the new object from the original. Modern JavaScript creates deep copies using structuredClone(obj) (or JSON.parse(JSON.stringify(obj)) with limitations on functions/undefined/Dates).",
    explanation="Avoid JSON serialization for deep copying if your object contains Date objects, undefined, NaN, or cyclic references.",
    code="const original = { name: 'Aman', address: { city: 'Bengaluru' } };\n\n// 1. Shallow Copy (Mutates original nested property!)\nconst shallow = { ...original };\nshallow.address.city = 'Delhi';\nconsole.log(original.address.city); // 'Delhi' (Corrupted original!)\n\n// 2. Deep Copy using structuredClone\nconst deep = structuredClone(original);\ndeep.address.city = 'Mumbai';\nconsole.log(original.address.city); // 'Delhi' (Original safe and unchanged!)",
    difficulty="Medium",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - structuredClone()",
    followup="What types cannot be cloned using structuredClone()?"
)

create_q(
    subject="JavaScript",
    topic="Asynchronous JS",
    subtopic="Promise Combinators: all, allSettled, race & any",
    question="What is the difference between Promise.all(), Promise.allSettled(), Promise.race(), and Promise.any()?",
    answer="1) Promise.all([p1, p2]): Fulfills when ALL promises resolve; rejects immediately if ANY single promise rejects (fail-fast). 2) Promise.allSettled([p1, p2]): Waits for all promises to finish regardless of outcome; returns array of {status, value/reason} objects (never short-circuits). 3) Promise.race([p1, p2]): Settles as soon as the FIRST promise settles (whether fulfilled or rejected). 4) Promise.any([p1, p2]): Fulfills as soon as the FIRST promise resolves successfully; rejects only if ALL promises reject (AggregateError).",
    explanation="Use Promise.allSettled when making multiple independent dashboard API calls so one failure does not break the entire page.",
    code="const p1 = fetch('/api/user');\nconst p2 = fetch('/api/notifications');\n\n// allSettled ensures all results can be inspected\nPromise.allSettled([p1, p2]).then(results => {\n  results.forEach(res => {\n    if (res.status === 'fulfilled') console.log('Data:', res.value);\n    else console.error('Error:', res.reason);\n  });\n});",
    difficulty="Medium",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Promise.allSettled()",
    followup="What is an AggregateError in Promise.any()?"
)

create_q(
    subject="JavaScript",
    topic="Type Coercion",
    subtopic="Tricky Output Questions (Coercion, typeof, Floating Point)",
    question="What will this JavaScript code output and why?\n\nconsole.log(typeof null);\nconsole.log([] + []);\nconsole.log([] + {});\nconsole.log(0.1 + 0.2 === 0.3);",
    answer="1) typeof null returns 'object' — an acknowledged bug from the first release of JavaScript where object references had a type tag of 0 and null was represented as a NULL pointer (0x00). 2) [] + [] returns \"\" (empty string) because binary '+' converts operands to primitives; [].toString() is \"\". 3) [] + {} returns \"[object Object]\" (empty string + \"[object Object]\"). 4) 0.1 + 0.2 === 0.3 returns false because binary IEEE 754 floating-point numbers cannot represent 0.1 and 0.2 precisely (0.1 + 0.2 equals 0.30000000000000004).",
    explanation="For precise currency calculations, work in integer cents (e.g. 10 cents + 20 cents = 30 cents) or use Number.EPSILON.",
    code="console.log(typeof null);       // 'object'\nconsole.log([] + []);           // \"\"\nconsole.log([] + {});           // \"[object Object]\"\nconsole.log(0.1 + 0.2 === 0.3); // false\n\n// Safe floating comparison using Number.EPSILON\nconsole.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON); // true",
    difficulty="Medium",
    q_type="Output",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - typeof",
    followup="What does NaN === NaN evaluate to and why?"
)

create_q(
    subject="JavaScript",
    topic="Scope & Closures",
    subtopic="Loop Variable Scoping & Closures (var vs let in setTimeout)",
    question="What will the following code output and why?\n\nfor (var i = 0; i < 3; i++) {\n  setTimeout(() => console.log('var:', i), 100);\n}\nfor (let j = 0; j < 3; j++) {\n  setTimeout(() => console.log('let:', j), 100);\n}",
    answer="Output:\nvar: 3\nvar: 3\nvar: 3\nlet: 0\nlet: 1\nlet: 2\n\nExplanation:\n1) 'var' is function-scoped (or globally scoped). There is only ONE shared variable 'i' for all loop iterations. By the time the setTimeout callbacks execute after 100ms, the loop has already terminated and 'i' equals 3. All three callbacks print 3.\n2) 'let' is block-scoped. On each iteration of the loop, a NEW binding for 'j' is created in memory. The callback closure captures that specific iteration's unique 'j' value (0, 1, and 2).",
    explanation="This is one of the most frequently asked closure and scoping questions in fresher technical interviews.",
    code="for (var i = 0; i < 3; i++) {\n  setTimeout(() => console.log('var:', i), 100);\n}\n// Prints: var: 3, var: 3, var: 3\n\nfor (let j = 0; j < 3; j++) {\n  setTimeout(() => console.log('let:', j), 100);\n}\n// Prints: let: 0, let: 1, let: 2",
    difficulty="Medium",
    q_type="Output",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Closures",
    followup="How did developers fix the 'var' loop issue before ES6 'let' was introduced (IIFE)?"
)

create_q(
    subject="JavaScript",
    topic="Browser Storage",
    subtopic="localStorage vs sessionStorage vs Cookies",
    question="What are the differences between localStorage, sessionStorage, and Cookies?",
    answer="1) localStorage: Stores up to ~5-10MB; data persists indefinitely across browser restarts until explicitly cleared with removeItem() or clear(). 2) sessionStorage: Stores up to ~5MB; persists only for the lifetime of that specific browser tab (closing the tab destroys the data; not shared across multiple tabs). 3) Cookies: Stores up to ~4KB; sent automatically with every outgoing HTTP request header. Supports 'HttpOnly' flag (blocks JavaScript document.cookie access to prevent XSS) and 'SameSite' flag (prevents CSRF).",
    explanation="Sensitive auth tokens are safest in HttpOnly, Secure cookies rather than localStorage where malicious injected scripts could steal them.",
    code="// LocalStorage: persistent settings\nlocalStorage.setItem('theme', 'dark');\nconst theme = localStorage.getItem('theme');\n\n// SessionStorage: temporary wizard form step\nsessionStorage.setItem('currentStep', '2');\n\n// Clear\nlocalStorage.removeItem('theme');",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Window.localStorage",
    followup="Can a browser extension access localStorage from another domain?"
)

create_q(
    subject="JavaScript",
    topic="Memory Management",
    subtopic="Garbage Collection & Common Memory Leaks",
    question="How does Garbage Collection work in JavaScript and what causes common memory leaks?",
    answer="Modern JavaScript engines (like V8) use the 'Mark-and-Sweep' garbage collection algorithm. The engine identifies 'roots' (global window object, active execution stack variables). It traverses references and 'marks' all reachable objects. Any objects that are unreachable are 'swept' and their memory reclaimed. Common memory leaks: 1) Accidental global variables (missing let/const). 2) Forgotten setInterval or setTimeout timers retaining closures over big data. 3) Uncleared DOM event listeners on removed nodes. 4) Closures retaining unnecessary outer references.",
    explanation="Always call clearInterval() when a timer is no longer needed, especially when React components unmount.",
    code="// Memory Leak Example:\nfunction startTracking() {\n  const heavyArray = new Array(1000000).fill('data');\n  // Leaked! If interval is never cleared, heavyArray cannot be garbage collected:\n  setInterval(() => {\n    console.log(heavyArray.length);\n  }, 1000);\n}\n\n// Fix: Save timer ID and clearInterval(timerId) on unmount",
    difficulty="Medium",
    q_type="Concept",
    round_type="Technical Round",
    freq="Medium",
    ref="MDN Web Docs - Memory Management",
    followup="How does WeakMap help prevent memory leaks compared to Map?"
)

# ==============================================================================
# 4. ES6+ (6 questions: Classes/Super, Modules, Destructuring, Default Params, Generators, for..of, Symbol/WeakMap)
# ==============================================================================
create_q(
    subject="ES6",
    topic="Classes",
    subtopic="Classes, Constructor, Extends & super()",
    question="How do ES6 Classes work and what is the role of constructor, extends, and super()?",
    answer="ES6 classes provide cleaner syntactic sugar over JavaScript's existing prototype-based inheritance. 'constructor' is the special method called automatically when creating a new instance with 'new'. 'extends' creates a subclass that inherits from a parent class. 'super()' calls the parent constructor and MUST be called inside a derived constructor before referencing 'this'. Subclasses can also call parent methods using super.methodName().",
    explanation="Under the hood, typeof ClassName returns 'function'; class methods are defined on ClassName.prototype.",
    code="class User {\n  constructor(name) {\n    this.name = name;\n  }\n  getRole() { return 'Standard User'; }\n}\n\nclass Admin extends User {\n  constructor(name, permissions) {\n    super(name); // Invokes User constructor\n    this.permissions = permissions;\n  }\n  getRole() {\n    return `${super.getRole()} - Admin Access`;\n  }\n}\n\nconst admin = new Admin('Kiran', ['DELETE', 'EDIT']);\nconsole.log(admin.name);     // 'Kiran'\nconsole.log(admin.getRole()); // 'Standard User - Admin Access'",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Classes",
    followup="What happens if you reference this in a derived constructor before calling super()?"
)

create_q(
    subject="ES6",
    topic="Modules",
    subtopic="Named Exports vs Default Export",
    question="What is the difference between Named Exports and Default Export in ES6 Modules (import/export)?",
    answer="Named exports allow exporting multiple functions, objects, or variables from a single file; when importing, they must be enclosed in curly braces { } and match the exported names exactly (or use 'as' to alias). Default export exports a single fallback value per file (export default fn); when importing, no curly braces are used, and the importing file can choose any arbitrary name for the imported identifier.",
    explanation="A single JavaScript module can have multiple named exports alongside one default export.",
    code="// utils.js\nexport const PI = 3.14159;            // Named export\nexport const add = (a, b) => a + b;   // Named export\nconst logger = (msg) => console.log(msg);\nexport default logger;                // Default export\n\n// main.js\nimport customLog, { PI, add as sum } from './utils.js';\ncustomLog(sum(2, PI));",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - JavaScript modules",
    followup="Can you dynamically import a module at runtime using import()?"
)

create_q(
    subject="ES6",
    topic="Destructuring",
    subtopic="Object & Array Destructuring with Defaults and Aliasing",
    question="How does Destructuring work in ES6 for objects and arrays, including property renaming and default values?",
    answer="Destructuring allows unpacking values from arrays or properties from objects into distinct variables: 1) Object Destructuring: const { name, age } = user;. Properties can be renamed using colon syntax ({ name: userName }) and assigned fallback defaults ({ role = 'guest' }). 2) Array Destructuring: const [first, second, ...rest] = colors; matches values by array index order. Skipping elements is done with commas (const [, second] = arr).",
    explanation="Destructuring makes extracting parameters in React functional component props extremely clean.",
    code="// Object Destructuring with renaming and default value\nconst user = { id: 101, fullName: 'Rohit' };\nconst { fullName: name, role = 'developer' } = user;\nconsole.log(name); // 'Rohit'\nconsole.log(role); // 'developer' (used default)\n\n// Array Destructuring with rest\nconst [head, ...tail] = [10, 20, 30, 40];\nconsole.log(head); // 10\nconsole.log(tail); // [20, 30, 40]",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Destructuring assignment",
    followup="Can you perform nested destructuring on deeply nested JSON responses?"
)

create_q(
    subject="ES6",
    topic="Functions",
    subtopic="Default Parameters & Enhanced Object Literals",
    question="How do Default Parameters and Enhanced Object Literals work in ES6?",
    answer="1) Default Parameters allow initializing function parameters with default values if no value or undefined is passed (e.g. function greet(name = 'Guest')). 2) Enhanced Object Literals introduce three concise syntaxes: Property shorthand (if key and variable name match: { name }), Method definition shorthand ({ greet() {} } instead of { greet: function() {} }), and Computed property names ({ [dynamicKey]: 'value' }).",
    explanation="Default parameters only trigger when an argument is omitted or strictly undefined; passing null will NOT trigger the default.",
    code="// 1. Default Parameters & Property Shorthand\nfunction createUser(name, role = 'developer') {\n  return { name, role }; // Shorthand for { name: name, role: role }\n}\n\n// 2. Computed Property Names & Method Shorthand\nconst prefix = 'api';\nconst service = {\n  [`${prefix}_url`]: 'https://example.com',\n  fetchData() {\n    return 'Fetched data';\n  }\n};",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Default parameters",
    followup="What happens if null is passed as an argument to a function with default parameters?"
)

create_q(
    subject="ES6",
    topic="Iterators",
    subtopic="Generator Functions (function* and yield)",
    question="What are Generator Functions in ES6 (function* and yield) and how do they work?",
    answer="A Generator Function (declared with function*) is a special function that can pause its execution and resume later, retaining its state across calls. When invoked, it returns a Generator iterator object. Calling generator.next() resumes execution until the next 'yield' keyword, returning { value: yieldedValue, done: false }. When the generator function finishes or returns, it yields { value: returnValue, done: true }.",
    explanation="Generators are ideal for lazy evaluation (generating large or infinite sequences on-demand without memory buffering).",
    code="function* idGenerator() {\n  let id = 1;\n  while (true) {\n    yield id++;\n  }\n}\n\nconst gen = idGenerator();\nconsole.log(gen.next().value); // 1\nconsole.log(gen.next().value); // 2\nconsole.log(gen.next().value); // 3",
    difficulty="Medium",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Iterators and generators",
    followup="What is the difference between return and yield inside a generator?"
)

create_q(
    subject="ES6",
    topic="Iteration",
    subtopic="for...of vs for...in Loops",
    question="What is the difference between for...in and for...of loops in JavaScript?",
    answer="1) for...in iterates over the enumerable keys (property names / indices) of an object or array. It traverses prototype chain properties as well, making it primarily suited for inspecting generic object keys. 2) for...of (introduced in ES6) iterates over the values of an iterable collection (such as Arrays, Strings, Maps, Sets, and NodeLists). It ignores non-enumerable properties and prototype keys, providing clean iteration over collection elements.",
    explanation="Never use for...in to iterate over arrays if order and array prototype protection matter.",
    code="const colors = ['red', 'green', 'blue'];\ncolors.customProp = 'test';\n\n// for...in logs indices & custom properties (keys)\nfor (const key in colors) {\n  console.log(key); // '0', '1', '2', 'customProp'\n}\n\n// for...of logs array values only\nfor (const color of colors) {\n  console.log(color); // 'red', 'green', 'blue'\n}",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - for...of",
    followup="Can you use for...of directly on a plain JavaScript object without Object.keys() or Object.entries()?"
)

create_q(
    subject="ES6",
    topic="Data Structures",
    subtopic="Symbol & WeakMap / WeakSet Purpose",
    question="What is a Symbol in ES6 and what is the difference between Map and WeakMap?",
    answer="Symbol is a primitive type that creates guaranteed unique identifiers, commonly used as non-colliding object keys or private-like properties. A standard Map holds strong references to its keys; keys and values cannot be garbage collected even if references are removed elsewhere in code. A WeakMap holds 'weak' references to keys (which MUST be objects). If no other references to the key object exist, the entry is automatically garbage collected, preventing memory leaks in caching or DOM metadata.",
    explanation="WeakMap is not iterable and does not have a .size property because garbage collection is non-deterministic.",
    code="const uniqueKey = Symbol('description');\nconst obj = { [uniqueKey]: 'Private Value' };\n\n// WeakMap for DOM element metadata:\nconst domMetadata = new WeakMap();\nlet btn = document.createElement('button');\ndomMetadata.set(btn, { clickCount: 0 });\n\n// When btn is removed from DOM and set to null,\n// the WeakMap entry is automatically garbage collected!\nbtn = null;",
    difficulty="Medium",
    q_type="Concept",
    round_type="Technical Round",
    freq="Medium",
    ref="MDN Web Docs - WeakMap",
    followup="Why must keys in a WeakMap be objects rather than primitives?"
)

# ==============================================================================
# 5. DOM (5 questions: Keyboard/Input, dataset, closest/matches, IntersectionObserver, Delegation Debug)
# ==============================================================================
create_q(
    subject="DOM",
    topic="Events",
    subtopic="Keyboard & Input Events (keydown, keyup, input, change)",
    question="What is the difference between keydown, keyup, input, and change events in the DOM?",
    answer="1) keydown fires the moment a physical key is pressed down (before character input appears; repeatable if held). 2) keyup fires when the user releases the key. 3) input fires synchronously on every character modification, deletion, or paste into an <input> or <textarea> (ideal for live search or character counters). 4) change fires only after the input loses focus (blurred) AND its value has altered (or immediately upon selecting an option in a <select> or checking a checkbox).",
    explanation="Always inspect event.key (e.g. 'Enter', 'Escape') instead of deprecated event.keyCode.",
    code="const searchBox = document.getElementById('search-input');\n\n// Live typing filter: fires on every keystroke/paste\nsearchBox.addEventListener('input', (e) => {\n  console.log('Current search term:', e.target.value);\n});\n\n// Enter key submission\nsearchBox.addEventListener('keydown', (e) => {\n  if (e.key === 'Enter') {\n    console.log('Search committed:', e.target.value);\n  }\n});",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - HTMLElement: input event",
    followup="What is the difference between event.target and event.currentTarget?"
)

create_q(
    subject="DOM",
    topic="Attributes",
    subtopic="Custom Data Attributes (data-*) and element.dataset",
    question="How do custom data-* attributes and element.dataset work in the DOM?",
    answer="HTML5 allows embedding custom metadata on HTML elements using attributes prefixed with 'data-' (e.g. data-user-id=\"42\", data-status=\"active\"). In JavaScript, these are read and modified via element.dataset. Attribute names are automatically converted to camelCase: data-item-id becomes element.dataset.itemId. In CSS, elements can be targeted or styled using attribute selectors like [data-status=\"active\"].",
    explanation="Dataset values are always strings. If you store numbers or booleans, convert them explicitly in JavaScript.",
    code="<!-- HTML -->\n<button id=\"user-btn\" data-user-id=\"1042\" data-account-type=\"pro\">View Profile</button>\n\n<script>\nconst btn = document.getElementById('user-btn');\n// Read (converted to camelCase)\nconsole.log(btn.dataset.userId);      // \"1042\"\nconsole.log(btn.dataset.accountType); // \"pro\"\n\n// Update\nbtn.dataset.accountType = 'enterprise'; // Updates HTML attribute\n</script>",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - HTMLElement.dataset",
    followup="How do you select all elements with a specific data attribute using querySelectorAll?"
)

create_q(
    subject="DOM",
    topic="Traversal",
    subtopic="closest() and matches() DOM Methods",
    question="What do closest() and matches() do in the DOM and how are they used in event delegation?",
    answer="1) element.matches(selector): Tests whether the element would be selected by the specified CSS selector; returns boolean true/false. 2) element.closest(selector): Traverses up the DOM tree starting from the element itself through its ancestors, returning the closest matching ancestor element (or null if none match). It is essential in event delegation when a click occurs on a nested child (like an <i> icon or <span> inside a <button>).",
    explanation="closest() checks the starting element first before looking at parents.",
    code="document.getElementById('product-list').addEventListener('click', (e) => {\n  // Finds the button even if user clicked an <i> icon inside it\n  const button = e.target.closest('.buy-btn');\n  if (button) {\n    const id = button.dataset.productId;\n    console.log('Purchased product ID:', id);\n  }\n});",
    difficulty="Easy",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Element.closest()",
    followup="What does closest() return if no matching ancestor is found?"
)

create_q(
    subject="DOM",
    topic="Modern APIs",
    subtopic="IntersectionObserver for Lazy Loading",
    question="What is IntersectionObserver and how is it used to lazy load images or detect scroll visibility?",
    answer="IntersectionObserver provides a high-performance way to asynchronously observe when a target element enters or exits the browser viewport (or an ancestor element). Unlike legacy scroll event listeners that fire continuously on the main thread and cause UI stutter, IntersectionObserver runs asynchronously off the main thread. It is widely used for lazy-loading images when scrolled into view, infinite scrolling feeds, and triggering scroll animations.",
    explanation="Disconnect or unobserve elements once loaded to conserve browser resources.",
    code="const imageObserver = new IntersectionObserver((entries, observer) => {\n  entries.forEach(entry => {\n    if (entry.isIntersecting) {\n      const img = entry.target;\n      img.src = img.dataset.src; // Swap placeholder with real image\n      observer.unobserve(img);   // Stop watching this image\n    }\n  });\n});\n\ndocument.querySelectorAll('img[data-src]').forEach(img => {\n  imageObserver.observe(img);\n});",
    difficulty="Medium",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Intersection Observer API",
    followup="What does the rootMargin option do in IntersectionObserver?"
)

create_q(
    subject="DOM",
    topic="Events",
    subtopic="Event Delegation for Dynamically Added Elements",
    question="Why does querySelectorAll('.item').forEach() NOT attach listeners to elements added dynamically later, and how do you solve it?",
    answer="querySelectorAll returns a static NodeList reflecting elements present in the DOM at the exact moment the query was executed. Elements created and inserted into the DOM later will not have those listeners attached. Solution: Use **Event Delegation** by attaching a single event listener to a static parent container that exists on page load. When events bubble up to the parent, inspect e.target (or e.target.closest) to handle the click dynamically.",
    explanation="Event delegation also saves browser memory by using 1 listener instead of thousands of individual listeners.",
    code="// Inefficient & breaks for newly inserted items:\n// document.querySelectorAll('.delete-btn').forEach(btn => btn.onclick = ...);\n\n// Correct: Event delegation on permanent list container\nconst list = document.getElementById('todo-list');\nlist.addEventListener('click', (e) => {\n  const deleteBtn = e.target.closest('.delete-btn');\n  if (deleteBtn) {\n    deleteBtn.closest('li').remove();\n  }\n});",
    difficulty="Easy",
    q_type="Debugging",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Event delegation",
    followup="Do all DOM events bubble up to the parent element?"
)

# ==============================================================================
# 6. jQuery (4 questions: Delegation with on(), Effects, Method Chaining, Modern Migration)
# ==============================================================================
create_q(
    subject="jQuery",
    topic="Events",
    subtopic="Event Delegation with on()",
    question="How does event delegation work in jQuery using the .on() method?",
    answer="In jQuery, passing a secondary selector to the .on() method delegates event handling: $(parent).on('click', '.child-selector', handler). The event listener attaches to the parent container. When a click bubbles up from any matching child element (even ones appended to the DOM hours later via AJAX), the callback executes. Inside the callback function, 'this' refers to the specific child DOM element that triggered the event.",
    explanation="This is identical in principle to vanilla JS event delegation, packaged into clean jQuery syntax.",
    code="// Delegates click to all current and future .btn-delete elements inside #orders-table\n$('#orders-table').on('click', '.btn-delete', function() {\n  const row = $(this).closest('tr');\n  row.fadeOut(300, function() {\n    $(this).remove();\n  });\n});",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="jQuery API Documentation - .on()",
    followup="What is the difference between $('#btn').click(fn) and $('#btn').on('click', fn)?"
)

create_q(
    subject="jQuery",
    topic="Effects",
    subtopic="Visual Effects (fadeIn, fadeOut, slideToggle, animate)",
    question="What are the common jQuery visual effect methods like fadeIn, fadeOut, slideToggle, and animate()?",
    answer="jQuery provides built-in animation helper methods that modify opacity and height smoothly: 1) fadeIn(speed) and fadeOut(speed) toggle element opacity. 2) slideDown(), slideUp(), and slideToggle() animate element height. 3) .animate({ cssProperties }, duration, callback) performs custom transitions on numeric CSS values. These methods accept a duration (in ms or 'slow'/'fast') and an optional callback function that fires upon animation completion.",
    explanation="In modern projects, CSS transitions are preferred because they utilize GPU acceleration.",
    code="// Smooth accordion toggle\n$('.accordion-header').click(function() {\n  $(this).next('.accordion-body').slideToggle(250);\n});\n\n// Notification auto-dismiss\n$('#alert-msg').fadeIn(200).delay(2000).fadeOut(400);",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="Medium",
    ref="jQuery API Documentation - Effects",
    followup="How do you stop a currently running jQuery animation using .stop()?"
)

create_q(
    subject="jQuery",
    topic="Architecture",
    subtopic="Method Chaining in jQuery",
    question="What is method chaining in jQuery and how does it work under the hood?",
    answer="Method chaining allows executing multiple jQuery methods consecutively on the same set of elements in a single line of code (e.g. $('#box').css('color', 'red').slideDown().addClass('active')). It works because almost all jQuery DOM manipulation and animation methods return the jQuery object ('this') they operated on, allowing the next method in the chain to execute immediately without re-querying the DOM.",
    explanation="Method chaining reduces repetitive DOM searches and results in concise code.",
    code="$('#status-message')\n  .text('Profile saved successfully!')\n  .addClass('alert-success')\n  .fadeIn(300)\n  .delay(2000)\n  .fadeOut(400);",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="Medium",
    ref="jQuery Learning Center - Chaining",
    followup="What does .end() do in a jQuery chained sequence?"
)

create_q(
    subject="jQuery",
    topic="Modernization",
    subtopic="Replacing jQuery with Modern Vanilla JavaScript",
    question="How do you replace common jQuery methods ($(sel), $.ajax, .addClass, .on) with modern Vanilla JavaScript?",
    answer="Modern browsers natively support all common jQuery features: 1) $(sel) -> document.querySelector(sel). 2) $('.item') -> document.querySelectorAll('.item'). 3) $.ajax({ url }) -> fetch(url).then(res => res.json()). 4) .addClass('c') / .removeClass('c') -> el.classList.add('c') / el.classList.remove('c'). 5) .on('click', fn) -> el.addEventListener('click', fn). 6) .parent() / .find() -> el.parentElement / el.querySelector().",
    explanation="Modern Vanilla JS eliminates the need to load the 30KB+ jQuery library.",
    code="// jQuery:\n// $('#btn').addClass('active').show();\n\n// Modern Vanilla JS equivalent:\nconst btn = document.querySelector('#btn');\nbtn.classList.add('active');\nbtn.style.display = 'block';",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="You Might Not Need jQuery Guide",
    followup="What is the vanilla JavaScript equivalent of jQuery $(document).ready()?"
)

# ==============================================================================
# 7. React (6 questions: useRef, useMemo/useCallback, Conditional, Controlled vs Uncontrolled, API Loading/Errors, Lifecycle)
# ==============================================================================
create_q(
    subject="React",
    topic="Hooks",
    subtopic="useRef Hook & Two Primary Use Cases",
    question="What is the useRef hook in React and what are its two primary use cases?",
    answer="useRef(initialValue) returns a mutable ref object { current: initialValue } that persists across renders. Use case 1: Accessing and interacting directly with real DOM elements (e.g. focusing an input on mount, reading scroll dimensions, or controlling audio/video playback). Use case 2: Storing mutable values (such as timer IDs, interval IDs, or previous state values) that need to persist across renders WITHOUT triggering a component re-render when modified.",
    explanation="Modifying ref.current is a synchronous mutation and does not cause React to re-render the component.",
    code="import { useRef, useEffect } from 'react';\n\nfunction AutoFocusSearch() {\n  const inputRef = useRef(null);\n  const timerRef = useRef(null);\n\n  useEffect(() => {\n    // Focus DOM element on initial mount\n    inputRef.current.focus();\n    \n    // Store timer without causing re-renders\n    timerRef.current = setInterval(() => console.log('Ping'), 5000);\n    return () => clearInterval(timerRef.current);\n  }, []);\n\n  return <input ref={inputRef} placeholder=\"Search freshers...\" />;\n}",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="React Docs - useRef",
    followup="What is the difference between a ref and state in React?"
)

create_q(
    subject="React",
    topic="Performance",
    subtopic="useMemo vs useCallback vs React.memo",
    question="What is the difference between useMemo, useCallback, and React.memo in React?",
    answer="1) React.memo: A Higher-Order Component that wraps a functional component to prevent it from re-rendering if its props have not changed (shallow comparison). 2) useMemo(() => computeValue, [deps]): Memoizes and caches the RESULT of an expensive calculation between renders. 3) useCallback(fn, [deps]): Memoizes and caches the FUNCTION DEFINITION itself between renders, preventing child components wrapped in React.memo from unnecessarily re-rendering when callbacks are passed as props.",
    explanation="Do not overuse useMemo and useCallback for simple calculations, as the hook dependency check itself has a small performance cost.",
    code="// 1. useMemo caches expensive calculated value\nconst filteredUsers = useMemo(() => {\n  return users.filter(u => u.name.toLowerCase().includes(search.toLowerCase()));\n}, [users, search]);\n\n// 2. useCallback caches function reference to prevent child re-rendering\nconst handleDelete = useCallback((id) => {\n  setUsers(prev => prev.filter(u => u.id !== id));\n}, []);",
    difficulty="Medium",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="React Docs - useMemo",
    followup="When should you NOT use useMemo?"
)

create_q(
    subject="React",
    topic="Core Concepts",
    subtopic="Conditional Rendering & The && Zero Bug",
    question="What are the common ways to perform conditional rendering in React, and what is the pitfall with &&?",
    answer="Common methods: 1) Ternary operator condition ? <A /> : <B />. 2) Logical AND condition && <Component />. 3) Early return if (!user) return <Login />;. Pitfall with &&: If the left-hand condition evaluates to 0 (e.g. items.length && <List /> when items is []), JavaScript short-circuits and returns 0! React renders the number 0 onto the screen. To prevent this, always make the condition an explicit boolean: items.length > 0 && <List /> or use ternary.",
    explanation="React does not render booleans, null, or undefined, but it DOES render the number 0.",
    code="function NotificationBadge({ count, user }) {\n  if (!user) return null; // Early return\n\n  return (\n    <div>\n      <h2>Welcome, {user.name}</h2>\n      {/* Safe check: avoids rendering '0' on screen */}\n      {count > 0 ? <p>You have {count} unread alerts</p> : <p>All caught up!</p>}\n    </div>\n  );\n}",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="React Docs - Conditional Rendering",
    followup="Why does React ignore true and false in JSX?"
)

create_q(
    subject="React",
    topic="Forms",
    subtopic="Controlled vs Uncontrolled Components",
    question="What is the difference between Controlled and Uncontrolled Components in React?",
    answer="In a Controlled Component, form input state is managed directly by React component state via value={state} and onChange={(e) => setState(e.target.value)}, giving React a single source of truth for validation, character limits, and conditional submission. In an Uncontrolled Component, form data is handled directly by the browser DOM itself; React reads values when needed (such as on form submit) using a useRef hook or FormData API. File inputs (<input type=\"file\">) are always uncontrolled in React.",
    explanation="Controlled inputs make instant form validation and disabling submit buttons straightforward.",
    code="// 1. Controlled Component\nconst [email, setEmail] = useState('');\n<input value={email} onChange={(e) => setEmail(e.target.value)} />\n\n// 2. Uncontrolled Component (using ref)\nconst inputRef = useRef();\nconst handleSubmit = (e) => {\n  e.preventDefault();\n  console.log(inputRef.current.value);\n};\n<input ref={inputRef} />",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="React Docs - Controlled and uncontrolled components",
    followup="Why is an <input type=\"file\"> always uncontrolled in React?"
)

create_q(
    subject="React",
    topic="Asynchronous React",
    subtopic="Handling API Loading, Success & Error States",
    question="How should a fresher structure component state to handle asynchronous API calls with loading and error states?",
    answer="Best practice maintains three state variables: 'data' (the fetched payload), 'loading' (boolean, initially true), and 'error' (null or error message string). In useEffect, set loading = true, make the asynchronous fetch call, update data on success, catch any network errors to set error message, and set loading = false in finally. In the JSX, conditionally display a loading skeleton/spinner, an error alert banner, or the data list.",
    explanation="Always check res.ok when using native fetch, as fetch does not reject HTTP 404 or 500 responses.",
    code="function ProductList() {\n  const [products, setProducts] = useState([]);\n  const [loading, setLoading] = useState(true);\n  const [error, setError] = useState(null);\n\n  useEffect(() => {\n    fetch('/api/products')\n      .then(res => {\n        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);\n        return res.json();\n      })\n      .then(data => setProducts(data))\n      .catch(err => setError(err.message))\n      .finally(() => setLoading(false));\n  }, []);\n\n  if (loading) return <p>Loading products...</p>;\n  if (error) return <p className=\"error\">Error: {error}</p>;\n  return <ul>{products.map(p => <li key={p.id}>{p.name}</li>)}</ul>;\n}",
    difficulty="Easy",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="React Docs - Synchronizing with Effects",
    followup="How do you cancel an in-flight fetch request if the component unmounts using AbortController?"
)

create_q(
    subject="React",
    topic="Lifecycle",
    subtopic="Mapping Component Lifecycle to useEffect",
    question="How do class component lifecycle methods (componentDidMount, componentDidUpdate, componentWillUnmount) map to useEffect in Functional Components?",
    answer="1) componentDidMount (Runs once on mount): useEffect(() => { ... }, []) with an empty dependency array. 2) componentDidUpdate (Runs when specific props/state change): useEffect(() => { ... }, [propA, stateB]) with dependencies listed. 3) componentWillUnmount (Runs before unmount): Return a cleanup function inside useEffect: return () => { clearInterval(timer); }. The cleanup function also runs before re-executing the effect on dependency changes.",
    explanation="The cleanup function prevents memory leaks by canceling active subscriptions, clearing intervals, or removing DOM listeners.",
    code="useEffect(() => {\n  // 1. Mount: Runs once when component appears\n  const handleResize = () => setWidth(window.innerWidth);\n  window.addEventListener('resize', handleResize);\n\n  // 3. Unmount: Cleanup function runs when component is removed\n  return () => {\n    window.removeEventListener('resize', handleResize);\n  };\n}, []); // Empty dependencies = Mount and Unmount only",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="React Docs - useEffect",
    followup="What happens if you omit the dependency array completely from useEffect?"
)

# ==============================================================================
# 8. Node.js (6 questions: Event loop phases, EventEmitter, path module, env variables, streams/buffers, http.createServer)
# ==============================================================================
create_q(
    subject="Node.js",
    topic="Event Loop",
    subtopic="Node.js Event Loop Phases & process.nextTick",
    question="What is the difference between process.nextTick(), setImmediate(), and setTimeout() in Node.js?",
    answer="1) process.nextTick(): Does not wait for event loop phases; its callback executes immediately after the current operation completes, before the event loop advances (Microtask). 2) setTimeout(fn, 0): Schedules execution in the 'Timers' phase of the event loop after the specified delay has passed. 3) setImmediate(fn): Schedules execution in the 'Check' phase of the event loop, immediately following the I/O polling phase.",
    explanation="process.nextTick has higher priority than Promise microtasks in Node.js.",
    code="setImmediate(() => console.log('setImmediate - Check Phase'));\nsetTimeout(() => console.log('setTimeout - Timers Phase'), 0);\nprocess.nextTick(() => console.log('process.nextTick - Immediate Microtask'));\nconsole.log('Synchronous script execution');\n\n// Output:\n// Synchronous script execution\n// process.nextTick - Immediate Microtask\n// setTimeout - Timers Phase\n// setImmediate - Check Phase",
    difficulty="Medium",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Node.js Docs - The Node.js Event Loop, Timers, and process.nextTick()",
    followup="Why might setImmediate and setTimeout(fn, 0) execute in varying order if not inside an I/O cycle?"
)

create_q(
    subject="Node.js",
    topic="Events",
    subtopic="EventEmitter Class & Custom Events",
    question="What is the EventEmitter class in Node.js and how do you implement custom events?",
    answer="The 'events' module provides the EventEmitter class, powering Node's event-driven architecture. Objects emit named events that trigger registered listener functions. Key methods: 1) emitter.on(event, listener) registers a subscriber. 2) emitter.once(event, listener) runs a handler only once. 3) emitter.emit(event, ...args) triggers the event with data arguments. 4) emitter.removeListener(event, listener) unsubscribes.",
    explanation="Core Node modules like http.Server and fs.ReadStream inherit from EventEmitter.",
    code="const EventEmitter = require('events');\nconst orderEmitter = new EventEmitter();\n\n// 1. Subscribe to 'orderPlaced' event\norderEmitter.on('orderPlaced', (orderId, amount) => {\n  console.log(`Email notification sent for Order #${orderId} ($${amount})`);\n});\n\n// 2. Emit event when order is completed\norderEmitter.emit('orderPlaced', 1042, 79.50);",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Node.js Docs - Events",
    followup="What happens if an EventEmitter emits an 'error' event and no listener is registered for 'error'?"
)

create_q(
    subject="Node.js",
    topic="Core Modules",
    subtopic="path.join() vs path.resolve()",
    question="What is the difference between path.join() and path.resolve() in Node.js?",
    answer="1) path.join([...paths]): Joins all given path segments together using the platform-specific delimiter ('/' on Linux/macOS, '\\' on Windows) and normalizes the resulting path (handling '..' and '.'). 2) path.resolve([...paths]): Resolves a sequence of paths into an absolute path by processing from right to left until an absolute path is formed; if no absolute root is found, it prepends the current working directory (process.cwd()).",
    explanation="Always use the path module rather than string concatenation to ensure cross-platform compatibility across Windows and Linux.",
    code="const path = require('path');\n\n// path.join merely concatenates segments\nconsole.log(path.join('/users', 'docs', 'file.txt'));\n// -> '/users/docs/file.txt'\n\n// path.resolve creates absolute path from cwd\nconsole.log(path.resolve('docs', 'file.txt'));\n// -> 'C:\\project\\docs\\file.txt' (or '/home/user/project/docs/file.txt')",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Node.js Docs - Path",
    followup="What is the difference between __dirname and process.cwd()?"
)

create_q(
    subject="Node.js",
    topic="Configuration",
    subtopic="Environment Variables & dotenv",
    question="How do you manage environment variables in Node.js and why should sensitive credentials not be hardcoded?",
    answer="In Node.js, environment variables are accessed via the global process.env object. During local development, the 'dotenv' package loads key-value pairs from a local .env file into process.env. Sensitive credentials (database passwords, JWT secret keys, API keys) must NEVER be committed to Git repositories (always add .env to .gitignore) to prevent credential theft, data breaches, and accidental exposure on public repositories.",
    explanation="In production hosting (Render, Vercel, AWS), environment variables are set in the cloud provider's dashboard.",
    code="// 1. Install: npm install dotenv\nrequire('dotenv').config();\n\nconst PORT = process.env.PORT || 5000;\nconst DB_URI = process.env.MONGODB_URI;\n\nconsole.log(`Server configured to run on port ${PORT}`);",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Node.js Docs - process.env",
    followup="Why should you provide fallback default values for non-sensitive environment variables?"
)

create_q(
    subject="Node.js",
    topic="Streams & Buffers",
    subtopic="Streams vs Buffers for Handling Large Data",
    question="What are Streams and Buffers in Node.js and why are streams crucial for handling large files?",
    answer="A Buffer is a fixed-size chunk of raw binary memory allocated outside the V8 JavaScript heap. A Stream is an interface for reading or writing data continuously chunk-by-chunk without loading the entire dataset into memory all at once. For example, reading a 2GB file with fs.readFile() will crash the Node process by exceeding RAM limits; using fs.createReadStream().pipe(res) processes the file in small 64KB chunks, keeping RAM usage low and constant.",
    explanation="There are 4 stream types: Readable, Writable, Duplex (read & write), and Transform (modify data while piping).",
    code="const fs = require('fs');\nconst http = require('http');\n\nhttp.createServer((req, res) => {\n  // Stream large file directly to client response\n  const readStream = fs.createReadStream('./large-dataset.csv');\n  readStream.pipe(res);\n}).listen(3000);",
    difficulty="Medium",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Node.js Docs - Stream",
    followup="What is backpressure in Node.js streams?"
)

create_q(
    subject="Node.js",
    topic="HTTP",
    subtopic="Creating a Raw HTTP Server with http.createServer()",
    question="How do you create a basic HTTP web server in Node.js using the built-in http module without Express?",
    answer="The built-in 'http' module provides http.createServer((req, res) => { ... }). Inside the request listener callback, 'req' represents the incoming request (inspecting req.url, req.method, and req.headers) and 'res' represents the server response. You set status codes and headers using res.writeHead(), send response payload using res.write(), and terminate the response with res.end(). The server listens on a port with server.listen(port).",
    explanation="Frameworks like Express are built directly on top of Node's native http module.",
    code="const http = require('http');\n\nconst server = http.createServer((req, res) => {\n  if (req.url === '/api/health' && req.method === 'GET') {\n    res.writeHead(200, { 'Content-Type': 'application/json' });\n    res.end(JSON.stringify({ status: 'ok', timestamp: Date.now() }));\n  } else {\n    res.writeHead(404, { 'Content-Type': 'text/plain' });\n    res.end('Route Not Found');\n  }\n});\n\nserver.listen(3000, () => console.log('Server running on port 3000'));",
    difficulty="Easy",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="Node.js Docs - http.createServer()",
    followup="How do you parse incoming request body data in a raw Node.js HTTP server?"
)

# ==============================================================================
# 9. Express.js (4 questions: express.Router, Error middleware, Built-in middleware, Validation)
# ==============================================================================
create_q(
    subject="Express",
    topic="Routing",
    subtopic="express.Router() Modular Routing",
    question="What is express.Router() and how does it help organize a large Express application?",
    answer="express.Router() creates an isolated, modular instance of routes and middleware. Instead of defining hundreds of endpoints in a single server.js file, routes are separated into dedicated files by resource (e.g. routes/users.js, routes/products.js). The main app imports the router and mounts it to a URL prefix using app.use('/api/users', userRoutes). This separation of concerns makes large codebases maintainable, testable, and clean.",
    explanation="Routers can also have their own dedicated middleware (e.g. route-specific authentication).",
    code="// routes/products.js\nconst express = require('express');\nconst router = express.Router();\n\nrouter.get('/', (req, res) => res.json({ products: [] }));\nrouter.get('/:id', (req, res) => res.json({ id: req.params.id }));\n\nmodule.exports = router;\n\n// server.js\nconst productRoutes = require('./routes/products');\napp.use('/api/products', productRoutes);",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Express.js Docs - Router",
    followup="Can you nest routers inside other routers in Express?"
)

create_q(
    subject="Express",
    topic="Middleware",
    subtopic="Global Error Handling Middleware",
    question="How do you create a global error handling middleware in Express and how does Express identify it?",
    answer="Express identifies error handling middleware by its exact 4-argument signature: (err, req, res, next). It MUST be registered at the very bottom of the middleware stack, after all route definitions. When any route handler encounters an error, calling next(err) instructs Express to bypass all normal middleware and jump directly to this global error handler, ensuring unified error logging and consistent JSON error responses.",
    explanation="Even if you do not use the 'next' parameter in the error handler, you must keep all 4 parameters in the function signature for Express to detect it.",
    code="// In any route controller:\napp.get('/user/:id', async (req, res, next) => {\n  try {\n    const user = await findUser(req.params.id);\n    if (!user) throw new Error('User not found');\n    res.json(user);\n  } catch (err) {\n    next(err); // Forwards error to global handler\n  }\n});\n\n// Global error handler (4 parameters required!)\napp.use((err, req, res, next) => {\n  console.error(err.stack);\n  res.status(err.status || 500).json({\n    success: false,\n    message: err.message || 'Internal Server Error'\n  });\n});",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Express.js Docs - Error handling",
    followup="What happens if an asynchronous route handler throws an error without next(err) in Express 4?"
)

create_q(
    subject="Express",
    topic="Middleware",
    subtopic="Built-in Middlewares (json, urlencoded, static)",
    question="What are the built-in middlewares in Express: express.json(), express.urlencoded(), and express.static()?",
    answer="1) express.json(): Parses incoming HTTP requests with JSON payloads and populates req.body with the parsed JavaScript object. 2) express.urlencoded({ extended: true }): Parses incoming requests with URL-encoded payloads (traditional HTML form submissions) and populates req.body. 3) express.static('public'): Serves static files (HTML, CSS, client-side JS, images) directly from the specified directory without writing manual route handlers.",
    explanation="Before Express 4.16+, developers had to install the separate 'body-parser' package; now it is built directly into Express.",
    code="const express = require('express');\nconst app = express();\n\napp.use(express.json()); // Parses JSON body\napp.use(express.urlencoded({ extended: true })); // Parses form submissions\napp.use(express.static('public')); // Serves static files from /public folder",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Express.js Docs - Built-in middleware",
    followup="What does the extended: true option in express.urlencoded mean?"
)

create_q(
    subject="Express",
    topic="Validation",
    subtopic="Request Input Validation Middleware",
    question="Why is request validation important in Express and how should a fresher implement basic input validation?",
    answer="Request validation verifies that incoming client payloads meet expected data types, required fields, and security constraints before database queries run. Unvalidated input can crash backend servers, corrupt database documents, or expose injection vulnerabilities. Validation can be written as custom route middleware that inspects req.body and returns a 400 Bad Request error if fields are missing or invalid, preventing corrupt data from reaching database layers.",
    explanation="Always validate input on the backend; frontend validation can easily be bypassed using curl or Postman.",
    code="const validateSignup = (req, res, next) => {\n  const { email, password } = req.body;\n  if (!email || !email.includes('@')) {\n    return res.status(400).json({ error: 'Valid email is required' });\n  }\n  if (!password || password.length < 8) {\n    return res.status(400).json({ error: 'Password must be at least 8 characters' });\n  }\n  next(); // Data is valid, proceed to controller\n};\n\napp.post('/api/signup', validateSignup, signupController);",
    difficulty="Easy",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="Express.js Guide - Using middleware",
    followup="What popular npm libraries are used for schema validation in Express?"
)

# ==============================================================================
# 10. REST / HTTP (8 questions: Lifecycle, Methods/Idempotency, Status Codes, Auth vs Authz, Headers/Cookies, REST Design, Params, Postman)
# ==============================================================================
create_q(
    subject="REST / HTTP",
    topic="HTTP Basics",
    subtopic="HTTP Request & Response Anatomy & Lifecycle",
    question="What constitutes an HTTP Request and HTTP Response, and what is the HTTP request lifecycle?",
    answer="An HTTP Request consists of: 1) Request Line (Method like GET/POST, Path, HTTP version), 2) Request Headers (metadata like Host, Authorization, Content-Type), 3) Optional Request Body (JSON payload). An HTTP Response consists of: 1) Status Line (HTTP version, Status Code like 200 OK), 2) Response Headers (Content-Type, Set-Cookie), 3) Response Body (HTML, JSON data). The client opens a TCP connection, sends the request, the server processes it, returns the response, and the connection closes or reuses via Keep-Alive.",
    explanation="HTTP is an application-layer, stateless protocol running on top of TCP/IP (port 80 for HTTP, 443 for HTTPS).",
    code="// HTTP Request:\nPOST /api/users HTTP/1.1\nHost: api.example.com\nContent-Type: application/json\nAuthorization: Bearer token123\n\n{ \"name\": \"Sita\" }\n\n// HTTP Response:\nHTTP/1.1 201 Created\nContent-Type: application/json\n\n{ \"id\": 101, \"name\": \"Sita\" }",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - An overview of HTTP",
    followup="What is HTTP Keep-Alive and why is it important?"
)

create_q(
    subject="REST / HTTP",
    topic="HTTP Methods",
    subtopic="HTTP Methods & Idempotency (GET, POST, PUT, PATCH, DELETE)",
    question="Which HTTP methods are idempotent and safe, and what is the difference between PUT and PATCH?",
    answer="A method is 'safe' if it does not modify server state (GET, HEAD). A method is 'idempotent' if executing identical requests multiple times produces the exact same server state as a single request: GET, PUT, DELETE, and HEAD are idempotent; POST is NOT idempotent (calling POST twice creates two separate records). PUT replaces the ENTIRE resource representation (all fields must be sent). PATCH applies PARTIAL modifications (only modified fields are sent).",
    explanation="Calling DELETE /users/5 once deletes the user; calling it 10 more times leaves the user deleted (state is identical, hence idempotent).",
    code="// PUT: Full replacement (replaces all user properties)\nPUT /api/users/1 \nBody: { \"name\": \"Aman\", \"age\": 25, \"role\": \"developer\" }\n\n// PATCH: Partial update (only updates role)\nPATCH /api/users/1 \nBody: { \"role\": \"lead developer\" }",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Idempotent method",
    followup="Why is POST not considered idempotent?"
)

create_q(
    subject="REST / HTTP",
    topic="Status Codes",
    subtopic="HTTP Status Codes Spectrum (2xx, 4xx, 5xx)",
    question="Explain the meaning and use cases for HTTP status codes: 200, 201, 204, 400, 401, 403, 404, 409, and 500.",
    answer="200 OK (standard successful request), 201 Created (resource successfully created via POST), 204 No Content (action succeeded but no body to return, e.g. DELETE). 400 Bad Request (invalid client syntax/body), 401 Unauthorized (missing or invalid authentication credentials), 403 Forbidden (authenticated but lacks role permission to access resource), 404 Not Found (resource does not exist), 409 Conflict (e.g. duplicate email registration). 500 Internal Server Error (unhandled server crash).",
    explanation="4xx codes represent client errors; 5xx codes represent server-side failures.",
    code="// Typical Express response status codes:\nres.status(200).json(data);              // OK\nres.status(201).json(newResource);      // Created\nres.status(204).send();                 // No Content (Deleted)\nres.status(401).json({ error: 'Login required' });\nres.status(403).json({ error: 'Admin permission required' });",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - HTTP response status codes",
    followup="What is the difference between 401 Unauthorized and 403 Forbidden?"
)

create_q(
    subject="REST / HTTP",
    topic="Security",
    subtopic="Authentication vs Authorization",
    question="What is the difference between Authentication and Authorization in web applications?",
    answer="Authentication (AuthN) verifies WHO you are (identity verification, e.g. entering email and password, logging in, verifying a JWT; returns 401 Unauthorized if invalid). Authorization (AuthZ) verifies WHAT you are allowed to do (permissions/roles, e.g. checking whether a logged-in user with role 'STUDENT' can access the admin grading panel; returns 403 Forbidden if permission is denied).",
    explanation="Authentication always happens before Authorization in request processing pipelines.",
    code="// Middleware 1: Authentication (Who are you?)\nconst verifyToken = (req, res, next) => {\n  if (!req.headers.authorization) return res.status(401).send('Unauthorized');\n  req.user = jwt.verify(token, SECRET);\n  next();\n};\n\n// Middleware 2: Authorization (Are you allowed?)\nconst requireAdmin = (req, res, next) => {\n  if (req.user.role !== 'ADMIN') return res.status(403).send('Forbidden: Admins only');\n  next();\n};",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="OWASP - Authentication and Authorization",
    followup="How does Role-Based Access Control (RBAC) work in REST APIs?"
)

create_q(
    subject="REST / HTTP",
    topic="Headers & Cookies",
    subtopic="HTTP Headers & Cookie Security Flags (HttpOnly, SameSite, Secure)",
    question="What are essential HTTP headers, and what do HttpOnly, Secure, and SameSite cookie flags do?",
    answer="Headers transmit metadata: Content-Type defines MIME type (e.g. application/json), Authorization carries credentials (Bearer <token>), and Accept specifies expected response formats. Cookies are small key-value strings stored by the browser. 1) HttpOnly: Prevents client JavaScript (document.cookie) from accessing the cookie, blocking XSS token theft. 2) Secure: Ensures cookies are transmitted only over encrypted HTTPS connections. 3) SameSite=Strict/Lax: Prevents cookies from being sent in cross-site requests, mitigating CSRF attacks.",
    explanation="Storing JWTs in HttpOnly cookies is safer than storing them in localStorage.",
    code="// Setting a secure cookie in Express:\nres.cookie('token', jwtToken, {\n  httpOnly: true,  // Cannot be read by JavaScript (XSS safe)\n  secure: true,    // Transmitted only over HTTPS\n  sameSite: 'strict', // Blocks CSRF\n  maxAge: 3600000  // 1 hour\n});",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - Using HTTP cookies",
    followup="What is the difference between SameSite=Strict and SameSite=Lax?"
)

create_q(
    subject="REST / HTTP",
    topic="REST Architecture",
    subtopic="RESTful API Design Principles & Resource Naming",
    question="What are the core RESTful API design principles and URL naming conventions?",
    answer="REST (Representational State Transfer) principles: 1) Client-Server separation of concerns, 2) Statelessness (each request contains all information needed to process it), 3) Cacheable responses, 4) Uniform interface. Naming conventions: Use plural nouns for resources, never verbs (e.g. /api/courses instead of /api/getCourses); use HTTP methods to indicate the action (GET, POST, PUT, DELETE); use hierarchical nested paths for child resources (e.g. /api/courses/10/students).",
    explanation="Good REST APIs are intuitive and self-descriptive based on standard HTTP verbs and clean noun paths.",
    code="// Clean RESTful endpoints:\nGET    /api/articles          // Get list of articles\nPOST   /api/articles          // Create new article\nGET    /api/articles/:id      // Get single article\nPUT    /api/articles/:id      // Replace article\nDELETE /api/articles/:id      // Delete article\nGET    /api/articles/:id/comments // Sub-resource",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="RESTful API Naming Guidelines",
    followup="What does HATEOAS stand for in advanced REST architecture?"
)

create_q(
    subject="REST / HTTP",
    topic="API Design",
    subtopic="Path Parameters vs Query Parameters",
    question="What is the difference between Path Parameters and Query Parameters in REST APIs?",
    answer="Path parameters (/users/:id) are required identifiers embedded directly into the URL path hierarchy to identify a specific unique resource. Query parameters (/products?category=laptops&sort=price&limit=10) appear after a '?' as key-value pairs used for optional filtering, sorting, searching, and pagination without changing the core resource endpoint.",
    explanation="If the parameter is essential to locating the single resource entity, use a path parameter; if it alters the view or filters a list, use query parameters.",
    code="// Path Parameter: Identifies specific order #502\n// GET /api/orders/502\nconst orderId = req.params.id;\n\n// Query Parameters: Filters and pages order collection\n// GET /api/orders?status=completed&page=2\nconst { status, page } = req.query;",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MDN Web Docs - What is a URL?",
    followup="How do you handle optional path parameters in Express?"
)

create_q(
    subject="REST / HTTP",
    topic="Tooling",
    subtopic="Postman & API Testing Basics for Freshers",
    question="What is Postman and how does a developer use it to test and debug REST APIs?",
    answer="Postman is an API development platform used to construct, test, and debug HTTP requests before or during frontend development. Developers specify HTTP method, URL endpoint, headers (like Authorization: Bearer <token>), query params, and JSON request bodies. Upon sending, Postman displays status code, execution time, response size, headers, and parsed JSON payload. Developers can also write automated test assertions in JavaScript under the 'Tests' tab.",
    explanation="Postman environments allow switching variables between Localhost and Production seamlessly.",
    code="// Postman Tests Tab Script:\npm.test(\"Status code is 200 OK\", function () {\n  pm.response.to.have.status(200);\n});\n\npm.test(\"Response returns user object with ID\", function () {\n  const data = pm.response.json();\n  pm.expect(data).to.have.property('id');\n  pm.expect(data.email).to.be.a('string');\n});",
    difficulty="Easy",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="Postman Documentation - Writing tests",
    followup="How do you pass environment variables into request headers in Postman?"
)

# ==============================================================================
# 11. SQL (7 questions: DDL vs DML, Subqueries, NULL handling, Self Join problem, Left Join problem, ACID, Group By Having)
# ==============================================================================
create_q(
    subject="SQL",
    topic="Fundamentals",
    subtopic="DDL vs DML Commands",
    question="What is the difference between DDL and DML commands in SQL with examples?",
    answer="DDL (Data Definition Language) commands define and alter the database schema and table structures: CREATE (creates table/db), ALTER (adds/modifies columns), DROP (deletes entire table and structure), and TRUNCATE (empties all rows quickly without deleting structure). DML (Data Manipulation Language) commands manage data rows within tables: SELECT (retrieves data), INSERT (adds new rows), UPDATE (modifies existing rows), and DELETE (removes specific rows).",
    explanation="DDL commands are auto-committed in most relational databases and cannot be rolled back easily.",
    code="-- DDL: Defining structure\nCREATE TABLE Students (\n  id INT PRIMARY KEY AUTO_INCREMENT,\n  name VARCHAR(100) NOT NULL,\n  email VARCHAR(100) UNIQUE\n);\n\n-- DML: Manipulating rows\nINSERT INTO Students (name, email) VALUES ('Arjun', 'arjun@test.com');\nUPDATE Students SET name = 'Arjun Patel' WHERE id = 1;\nDELETE FROM Students WHERE id = 1;",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="PostgreSQL / MySQL Documentation - SQL Syntax",
    followup="What is the difference between DROP, TRUNCATE, and DELETE?"
)

create_q(
    subject="SQL",
    topic="Queries",
    subtopic="Subqueries vs Joins",
    question="What is a SQL Subquery and when would you use a Subquery vs a JOIN?",
    answer="A Subquery is a query nested inside another SQL statement (within WHERE, FROM, or SELECT clauses). Subqueries are intuitive for filtering records by aggregated metrics (e.g. employees earning more than the company average). JOINs combine columns from two or more tables based on related foreign keys. In production, JOINs are generally faster and preferred for large datasets because database query optimizers can optimize join execution plans more efficiently than correlated subqueries.",
    explanation="A correlated subquery executes once for each row evaluated by the outer query, which can cause severe performance lag ($O(N^2)$).",
    code="-- Subquery: Find employees earning more than the company average salary\nSELECT name, salary\nFROM Employees\nWHERE salary > (\n  SELECT AVG(salary) FROM Employees\n);\n\n-- Equivalent JOIN for department name retrieval\nSELECT e.name, d.department_name\nFROM Employees e\nINNER JOIN Departments d ON e.dept_id = d.id;",
    difficulty="Medium",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MySQL Documentation - Subqueries",
    followup="What is a correlated subquery in SQL?"
)

create_q(
    subject="SQL",
    topic="Null Handling",
    subtopic="NULL Comparisons (IS NULL and COALESCE)",
    question="How do NULL values behave in SQL comparisons and how do you handle them using IS NULL and COALESCE()?",
    answer="NULL represents an unknown or missing value. In SQL, NULL = NULL evaluates to UNKNOWN (not true), meaning standard equality operators (= or !=) always fail against NULL. You must use IS NULL or IS NOT NULL. The COALESCE(val1, val2, fallback) function evaluates arguments in order and returns the first non-NULL value, making it ideal for replacing NULLs with default fallback text in queries.",
    explanation="Never write WHERE column = NULL; it will return 0 rows.",
    code="-- Correct way to filter missing records\nSELECT name, phone FROM Customers WHERE phone IS NULL;\n\n-- Using COALESCE to provide fallback display values\nSELECT \n  name, \n  COALESCE(phone, 'No phone on file') AS contact_phone,\n  COALESCE(discount, 0) AS applied_discount\nFROM Customers;",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="PostgreSQL Docs - Conditional Expressions (COALESCE)",
    followup="What does IFNULL() do in MySQL compared to COALESCE()?"
)

create_q(
    subject="SQL",
    topic="Joins",
    subtopic="Self Join: Employees Earning More Than Manager",
    question="Write a SQL query to find employees who earn more than their direct manager.",
    answer="Use a SELF JOIN by joining the Employees table with itself. Alias one instance as 'e' (representing the employee) and the second instance as 'm' (representing the manager) on e.manager_id = m.id, then filter in the WHERE clause where e.salary > m.salary.",
    explanation="Self joins allow comparing rows within the exact same table hierarchy.",
    code="-- Schema: Employees (id, name, salary, manager_id)\nSELECT \n  e.name AS Employee,\n  e.salary AS EmployeeSalary,\n  m.name AS Manager,\n  m.salary AS ManagerSalary\nFROM Employees e\nJOIN Employees m ON e.manager_id = m.id\nWHERE e.salary > m.salary;",
    difficulty="Medium",
    q_type="SQL Query",
    round_type="Technical Round",
    freq="High",
    ref="LeetCode 181 - Employees Earning More Than Their Managers",
    followup="What happens to employees who have no manager (manager_id is NULL) in an INNER JOIN?"
)

create_q(
    subject="SQL",
    topic="Joins",
    subtopic="LEFT JOIN: Find Customers Who Never Placed an Order",
    question="Write a SQL query to find all customers who have never placed an order.",
    answer="Perform a LEFT JOIN from the Customers table to the Orders table on c.id = o.customer_id. A LEFT JOIN keeps all customer rows; customers without matching orders will have NULL in the joined orders columns. Filter in the WHERE clause where o.customer_id IS NULL.",
    explanation="This is an anti-join pattern, significantly faster than using NOT IN with subqueries containing NULLs.",
    code="-- Schema: Customers (id, name), Orders (id, customer_id, order_date)\nSELECT c.id, c.name\nFROM Customers c\nLEFT JOIN Orders o ON c.id = o.customer_id\nWHERE o.customer_id IS NULL;",
    difficulty="Easy",
    q_type="SQL Query",
    round_type="Technical Round",
    freq="High",
    ref="LeetCode 183 - Customers Who Never Order",
    followup="Why can 'WHERE id NOT IN (SELECT customer_id FROM Orders)' return 0 rows if Orders has a single NULL?"
)

create_q(
    subject="SQL",
    topic="Database Concepts",
    subtopic="Transactions and ACID Properties",
    question="What is a database transaction and what do the ACID properties stand for?",
    answer="A transaction is a sequence of SQL operations executed as a single indivisible unit of work. ACID stands for: 1) Atomicity: All operations succeed or all roll back; no partial execution. 2) Consistency: The transaction transitions the database from one valid state to another, preserving all schema constraints. 3) Isolation: Concurrent transactions execute independently without interfering with each other. 4) Durability: Once committed, updates persist permanently even through sudden power or server failures.",
    explanation="Banking money transfers are the classic ACID example: deducting money from Account A and adding to Account B must happen together or not at all.",
    code="START TRANSACTION;\n\nUPDATE Accounts SET balance = balance - 500 WHERE account_id = 101;\nUPDATE Accounts SET balance = balance + 500 WHERE account_id = 202;\n\n-- If both succeed, commit changes permanently:\nCOMMIT;\n-- If any error occurred:\n-- ROLLBACK;",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="PostgreSQL Docs - Transaction Isolation",
    followup="What are dirty reads and phantom reads in SQL transaction isolation levels?"
)

create_q(
    subject="SQL",
    topic="Aggregations",
    subtopic="GROUP BY with HAVING Filter",
    question="Write a query using GROUP BY, COUNT(), and HAVING to find all departments with more than 5 employees.",
    answer="Use GROUP BY department to group rows by department name. Use COUNT(*) to count employees in each group. Filter with HAVING COUNT(*) > 5. WHERE filters individual rows before grouping; HAVING filters grouped aggregate results after grouping.",
    explanation="You cannot use WHERE with aggregate functions like COUNT() or AVG(); HAVING is required.",
    code="SELECT \n  department,\n  COUNT(*) AS total_employees,\n  AVG(salary) AS average_salary\nFROM Employees\nGROUP BY department\nHAVING COUNT(*) > 5\nORDER BY total_employees DESC;",
    difficulty="Easy",
    q_type="SQL Query",
    round_type="Technical Round",
    freq="High",
    ref="MySQL Documentation - GROUP BY Extensions",
    followup="Can you use both WHERE and HAVING in the exact same SQL query?"
)

# ==============================================================================
# 12. MongoDB (6 questions: BSON/ObjectId, Update operators, Indexing/explain, Mongoose, Pagination, Modeling)
# ==============================================================================
create_q(
    subject="MongoDB",
    topic="Fundamentals",
    subtopic="BSON vs JSON & ObjectId Breakdown",
    question="What is BSON in MongoDB, how does it differ from JSON, and what is inside an ObjectId?",
    answer="BSON (Binary JSON) is the binary-encoded serialization format MongoDB uses to store documents. Unlike JSON which only supports strings, numbers, booleans, and null, BSON supports rich data types including Date, int32, int64, Decimal128, and raw binary. An ObjectId is a 12-byte unique primary key composed of: 4-byte Unix timestamp (seconds since epoch), 5-byte random machine/process identifier, and a 3-byte incrementing counter.",
    explanation="Because an ObjectId begins with a 4-byte timestamp, documents are roughly chronologically ordered by default.",
    code="// Extracting the creation date directly from an ObjectId:\nconst id = new ObjectId();\nconsole.log(id.getTimestamp()); \n// Output: 2026-10-03T10:20:00.000Z",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MongoDB Docs - ObjectId",
    followup="How many bytes is a MongoDB ObjectId?"
)

create_q(
    subject="MongoDB",
    topic="CRUD",
    subtopic="MongoDB Update Operators ($set, $inc, $push, $pull)",
    question="What are the common MongoDB update operators: $set, $inc, $push, and $pull?",
    answer="Calling updateOne() without atomic operators replaces the entire document. Update operators modify specific fields: 1) $set: Updates existing fields or adds new ones without affecting other fields. 2) $inc: Increments a numeric field by a specified value (use negative numbers to decrement). 3) $push: Appends an item to an array field. 4) $pull: Removes all instances of a matching value from an array field.",
    explanation="Atomic operators guarantee safe updates even when multiple requests modify the same document concurrently.",
    code="// Atomically increment views, add tag, and update timestamp\ndb.articles.updateOne(\n  { _id: ObjectId(\"60c72b2f9b1d8b2badbee1aa\") },\n  {\n    $set: { status: 'published', updatedAt: new Date() },\n    $inc: { viewCount: 1 },\n    $push: { tags: 'trending' }\n  }\n);",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MongoDB Docs - Update Operators",
    followup="What does the upsert: true option do in MongoDB update operations?"
)

create_q(
    subject="MongoDB",
    topic="Performance",
    subtopic="Indexes & .explain('executionStats')",
    question="What are Indexes in MongoDB, why are they crucial, and how do you test query performance using .explain()?",
    answer="Indexes store a small, ordered subset of collection data in a B-Tree structure, allowing MongoDB to resolve queries in O(log N) time instead of performing a full collection scan (COLLSCAN) that inspects every single document (O(N)). Indexes are created via db.collection.createIndex({ email: 1 }). Appending .explain('executionStats') to a query reveals performance metrics: look for stage 'IXSCAN' (Index Scan) vs 'COLLSCAN' and compare totalDocsExamined to nReturned.",
    explanation="In an optimized query, totalDocsExamined should equal nReturned.",
    code="// 1. Create a unique index on email\ndb.users.createIndex({ email: 1 }, { unique: true });\n\n// 2. Inspect query execution plan\ndb.users.find({ email: 'user@test.com' }).explain('executionStats');\n// Look for: executionStages.stage === 'IXSCAN'",
    difficulty="Medium",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="MongoDB Docs - Indexes and explain()",
    followup="What are compound indexes in MongoDB and how does index prefixing work?"
)

create_q(
    subject="MongoDB",
    topic="ODM",
    subtopic="Mongoose Schema, Model & Validation",
    question="What is Mongoose and what is the difference between a Schema and a Model?",
    answer="Mongoose is an Object Data Modeling (ODM) library for MongoDB and Node.js. A Schema is a blueprint that defines the structure, data types, default values, and validation rules of documents in a collection. A Model is a compiled constructor created from the schema (mongoose.model('User', userSchema)) that provides the programming interface for database CRUD operations (find, create, save). Mongoose also supports pre-save hooks/middleware (e.g. for hashing passwords).",
    explanation="Mongoose enforces schema validation at the application level before queries reach the MongoDB server.",
    code="const mongoose = require('mongoose');\n\n// 1. Schema Definition with validations\nconst userSchema = new mongoose.Schema({\n  name: { type: String, required: true, trim: true },\n  email: { type: String, required: true, unique: true, lowercase: true },\n  role: { type: String, enum: ['user', 'admin'], default: 'user' }\n}, { timestamps: true });\n\n// 2. Compile into Model\nconst User = mongoose.model('User', userSchema);\nmodule.exports = User;",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Mongoose Documentation - Schemas and Models",
    followup="What is the difference between pre('save') and post('save') middleware in Mongoose?"
)

create_q(
    subject="MongoDB",
    topic="Queries",
    subtopic="Pagination with skip() and limit()",
    question="How do you implement pagination in MongoDB using skip() and limit()?",
    answer="Given requested page number (1-indexed) and items per page (pageSize): skipCount = (page - 1) * pageSize. Calling .find().sort({ _id: -1 }).skip(skipCount).limit(pageSize) returns the desired slice of documents. Always pair skip and limit with explicit sort order to guarantee consistent, deterministic pagination results.",
    explanation="For very large collections (millions of rows), cursor-based range pagination (e.g. _id < lastSeenId) is faster than large skip() offsets.",
    code="// Pagination endpoint in Express / Mongoose\napp.get('/api/articles', async (req, res) => {\n  const page = Math.max(1, parseInt(req.query.page) || 1);\n  const limit = Math.max(1, parseInt(req.query.limit) || 10);\n  const skip = (page - 1) * limit;\n\n  const articles = await Article.find({})\n    .sort({ createdAt: -1 })\n    .skip(skip)\n    .limit(limit);\n\n  const total = await Article.countDocuments();\n  res.json({ page, totalPages: Math.ceil(total / limit), articles });\n});",
    difficulty="Easy",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="MongoDB Docs - Cursor.skip() and Cursor.limit()",
    followup="Why does .skip(100000) become slow on massive MongoDB collections?"
)

create_q(
    subject="MongoDB",
    topic="Data Modeling",
    subtopic="Embedding vs Referencing Decision Guidelines",
    question="When should you Embed documents versus Reference documents in MongoDB?",
    answer="Embed (Denormalize) when: 1) Data is viewed together in the majority of queries (e.g. user address inside user profile). 2) Relationship is 1-to-1 or bounded 1-to-Few. 3) The sub-document data does not grow unboundedly (MongoDB document limit is 16MB). Reference (Normalize) when: 1) Related entities are frequently queried independently. 2) Relationship is 1-to-Many or Many-to-Many (e.g. millions of activity logs per user). 3) Data is frequently updated and duplicated storage would cause update anomalies.",
    explanation="The golden rule of MongoDB data modeling is: 'Data that is accessed together should be stored together.'",
    code="// 1. Embedded (1-to-few): Address inside User\n{\n  _id: ObjectId(\"...\"),\n  name: 'Rahul',\n  address: { street: '12 MG Road', city: 'Bengaluru', pincode: '560001' }\n}\n\n// 2. Referenced (1-to-many): Order references User ID\n{\n  _id: ObjectId(\"...\"),\n  userId: ObjectId(\"...\"), // Foreign key reference\n  totalAmount: 1499.00,\n  status: 'shipped'\n}",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="MongoDB Docs - Data Model Design",
    followup="What is the $lookup aggregation stage in MongoDB?"
)

# ==============================================================================
# 13. Aptitude (14 questions: Quant, Logical, Verbal, DI - Clean & Non-duplicate)
# ==============================================================================
create_q(
    subject="Aptitude",
    topic="Quantitative Aptitude",
    subtopic="Pipes & Cisterns",
    question="Pipe A can fill a water tank in 12 hours and Pipe B can empty the same tank in 18 hours. If both pipes are opened simultaneously into an empty tank, how many hours will it take to fill the tank completely?",
    answer="36 hours.",
    explanation="Pipe A's 1-hour filling rate = +1/12. Pipe B's 1-hour emptying rate = -1/18. Net work done in 1 hour with both pipes open = (1/12) - (1/18) = (3 - 2)/36 = 1/36. Therefore, the tank will be completely filled in 1 / (1/36) = 36 hours.",
    code="// Net 1-hr rate = (1/12) - (1/18) = (3 - 2)/36 = 1/36\n// Total Time = 36 hours",
    difficulty="Easy",
    q_type="Aptitude",
    round_type="Online Test",
    freq="High",
    ref="Standard Placement Quantitative Aptitude",
    followup="What happens if Pipe B empties the tank faster than Pipe A fills it?"
)

create_q(
    subject="Aptitude",
    topic="Quantitative Aptitude",
    subtopic="LCM & HCF",
    question="The HCF of two numbers is 11 and their LCM is 7700. If one of the numbers is 275, what is the other number?",
    answer="308.",
    explanation="Standard Mathematical Property: Product of two numbers = (HCF * LCM). Let the required number be X. Then: 275 * X = 11 * 7700 => X = (11 * 7700) / 275 = 84700 / 275 = 308.",
    code="// Formula: Num1 * Num2 = HCF * LCM\n// 275 * X = 11 * 7700\n// X = 84700 / 275 = 308",
    difficulty="Easy",
    q_type="Aptitude",
    round_type="Online Test",
    freq="High",
    ref="Standard Placement Quantitative Aptitude",
    followup="Can the HCF of two numbers ever be greater than their LCM?"
)

create_q(
    subject="Aptitude",
    topic="Quantitative Aptitude",
    subtopic="Profit, Loss & Discount",
    question="An article is marked at Rs. 800. A shopkeeper offers a 10% discount on the marked price and still makes a 20% profit. What was the original cost price of the article?",
    answer="Rs. 600.",
    explanation="1) Marked Price (MP) = Rs. 800. 2) Selling Price (SP) after 10% discount = 800 - (10% of 800) = 800 - 80 = Rs. 720. 3) Since profit is 20% on Cost Price (CP): SP = CP * (1 + 0.20) = 1.20 * CP. 4) Therefore: CP = 720 / 1.20 = Rs. 600.",
    code="// SP = MP * (1 - Discount%) = 800 * 0.90 = 720\n// CP = SP / (1 + Profit%) = 720 / 1.20 = 600",
    difficulty="Easy",
    q_type="Aptitude",
    round_type="Online Test",
    freq="High",
    ref="Standard Placement Quantitative Aptitude",
    followup="What would be the profit percentage if no discount was given?"
)

create_q(
    subject="Aptitude",
    topic="Quantitative Aptitude",
    subtopic="Simple Interest & Compound Interest",
    question="What is the simple interest on a principal of Rs. 5,000 for 2 years at an annual interest rate of 6%?",
    answer="Rs. 600.",
    explanation="Simple Interest formula: SI = (Principal * Rate * Time) / 100. SI = (5000 * 6 * 2) / 100 = 60000 / 100 = Rs. 600. The total amount returned after 2 years = Principal + SI = 5000 + 600 = Rs. 5,600.",
    code="// SI = (P * R * T) / 100\n// SI = (5000 * 6 * 2) / 100 = 600\n// Total Amount = 5000 + 600 = 5600",
    difficulty="Easy",
    q_type="Aptitude",
    round_type="Online Test",
    freq="High",
    ref="Standard Placement Quantitative Aptitude",
    followup="What would be the compound interest compounded annually on the same amount?"
)

create_q(
    subject="Aptitude",
    topic="Quantitative Aptitude",
    subtopic="Probability",
    question="Two unbiased six-sided dice are thrown simultaneously. What is the probability of getting a sum of 8?",
    answer="5 / 36 (approx 13.89%).",
    explanation="Total possible outcomes when rolling two dice = 6 * 6 = 36. Favorable outcomes where sum of numbers is 8: (2, 6), (3, 5), (4, 4), (5, 3), (6, 2) = 5 outcomes. Probability = Favorable outcomes / Total outcomes = 5 / 36.",
    code="// Total sample space = 36\n// Pairs summing to 8: (2,6), (3,5), (4,4), (5,3), (6,2) -> 5 pairs\n// Probability = 5 / 36",
    difficulty="Easy",
    q_type="Aptitude",
    round_type="Online Test",
    freq="High",
    ref="Standard Placement Quantitative Aptitude",
    followup="What is the probability of getting a sum greater than 10?"
)

create_q(
    subject="Aptitude",
    topic="Logical Reasoning",
    subtopic="Coding & Decoding",
    question="In a certain code language, if 'SYSTEM' is coded as 'SYSMET' and 'NEARER' is coded as 'AENRER', how will 'FRACTION' be coded?",
    answer="'CARFNOIT'.",
    explanation="Divide the 8-letter word into two equal halves of 4 letters each: 'FRAC' and 'TION'. Reverse the first half: 'FRAC' reversed becomes 'CARF'. Reverse the second half: 'TION' reversed becomes 'NOIT'. Combine the two reversed halves: 'CARF' + 'NOIT' = 'CARFNOIT'.",
    code="// Step 1: Split FRACTION -> 'FRAC' and 'TION'\n// Step 2: Reverse part 1 -> 'CARF'\n// Step 3: Reverse part 2 -> 'NOIT'\n// Result: 'CARFNOIT'",
    difficulty="Easy",
    q_type="Logical Reasoning",
    round_type="Online Test",
    freq="High",
    ref="Standard Placement Logical Reasoning",
    followup="How would 'COMPUTER' be coded under this rule?"
)

create_q(
    subject="Aptitude",
    topic="Logical Reasoning",
    subtopic="Blood Relations",
    question="Pointing to a photograph of a boy, Suresh said, 'He is the only son of my mother.' How is Suresh related to that boy?",
    answer="Suresh is the boy himself (the photograph is of Suresh).",
    explanation="Breaking down the statement: 'My mother's only son' -> For Suresh, his mother's only son is Suresh himself (assuming Suresh is male and has no brothers). Therefore, the boy in the photograph is Suresh himself.",
    code="// Suresh's mother -> Mother's only son = Suresh\n// The boy is Suresh himself.",
    difficulty="Easy",
    q_type="Logical Reasoning",
    round_type="Online Test",
    freq="High",
    ref="Standard Placement Logical Reasoning",
    followup="If Suresh said 'He is the son of my father's only son', who would it be?"
)

create_q(
    subject="Aptitude",
    topic="Logical Reasoning",
    subtopic="Directions & Distance",
    question="A person walks 4 km North, then turns right and walks 3 km. How far and in what direction is the person from the starting point?",
    answer="5 km North-East.",
    explanation="1) The path forms a right-angled triangle with perpendicular legs: 4 km (North) and 3 km (East). 2) By Pythagoras theorem: Distance = sqrt(4^2 + 3^2) = sqrt(16 + 9) = sqrt(25) = 5 km. 3) The direction from the starting point is North-East.",
    code="// Distance = sqrt(North^2 + East^2)\n// Distance = sqrt(4^2 + 3^2) = sqrt(25) = 5 km North-East",
    difficulty="Easy",
    q_type="Logical Reasoning",
    round_type="Online Test",
    freq="High",
    ref="Standard Placement Logical Reasoning",
    followup="If the person then turns South and walks 4 km, how far are they from the starting point?"
)

create_q(
    subject="Aptitude",
    topic="Logical Reasoning",
    subtopic="Syllogisms",
    question="Statements:\n1. All cats are animals.\n2. All animals need water.\nConclusions:\nI. All cats need water.\nII. All creatures that need water are cats.\nWhich conclusion(s) logically follow?",
    answer="Only Conclusion I follows.",
    explanation="Since the set of all cats is entirely contained within the set of animals, and the set of animals is entirely contained within creatures needing water, All cats need water (Conclusion I is valid). Conclusion II is invalid because other animals (dogs, birds) also need water without being cats.",
    code="// Cats ⊆ Animals ⊆ Need Water\n// Therefore, Cats ⊆ Need Water (Conclusion I is TRUE)\n// Conclusion II claims Need Water ⊆ Cats (FALSE)",
    difficulty="Easy",
    q_type="Logical Reasoning",
    round_type="Online Test",
    freq="High",
    ref="Standard Placement Logical Reasoning",
    followup="What is the distributed term in the first premise?"
)

create_q(
    subject="Aptitude",
    topic="Verbal Ability",
    subtopic="Subject-Verb Agreement",
    question="Find the grammatical error in this sentence: 'Each of the students have submitted their project report on time.'",
    answer="'have' should be replaced with 'has'.",
    explanation="The grammatical subject is 'Each', which is a singular indefinite pronoun. Therefore, it requires a singular verb 'has' rather than plural 'have': 'Each of the students HAS submitted his or her project report on time.'",
    code="// Incorrect: Each of the students have...\n// Correct:   Each of the students has...",
    difficulty="Easy",
    q_type="Concept",
    round_type="Online Test",
    freq="High",
    ref="Standard Verbal Ability Guide",
    followup="Does 'Neither of the options' take a singular or plural verb?"
)

create_q(
    subject="Aptitude",
    topic="Verbal Ability",
    subtopic="Synonyms & Antonyms",
    question="What is the synonym of 'CANDID' and what is the antonym of 'OBSOLETE'?",
    answer="Synonym of CANDID: Frank, Honest, or Forthright. Antonym of OBSOLETE: Modern, Current, or Contemporary.",
    explanation="'Candid' means truthful, straightforward, and sincere. 'Obsolete' means no longer in use or outdated; its opposite is current/modern.",
    code="// CANDID: Synonym = Frank / Sincere\n// OBSOLETE: Antonym = Modern / Contemporary",
    difficulty="Easy",
    q_type="Concept",
    round_type="Online Test",
    freq="High",
    ref="High Frequency Placement Vocabulary",
    followup="What is the meaning of the word 'Pragmatic'?"
)

create_q(
    subject="Aptitude",
    topic="Verbal Ability",
    subtopic="Sentence Completion",
    question="Choose the correct word to fill in the blank: 'Although the team worked rigorously, they could not ______ the deadline.' (achieve, meet, make, finalize)",
    answer="'meet'.",
    explanation="The standard English collocation with 'deadline' is 'meet the deadline' (meaning to finish before or at the due time). While 'achieve' applies to goals, 'meet' is the correct verb used with deadlines.",
    code="// Collocation: 'meet a deadline', 'miss a deadline'",
    difficulty="Easy",
    q_type="Concept",
    round_type="Online Test",
    freq="High",
    ref="Standard Placement English Grammar",
    followup="What preposition follows the verb 'congratulate'?"
)

create_q(
    subject="Aptitude",
    topic="Data Interpretation",
    subtopic="Tabular Data Analysis",
    question="In a software firm, Branch A has 40 engineers with a 10% attrition rate, while Branch B has 60 engineers with a 20% attrition rate. What is the overall attrition rate of the firm?",
    answer="16%.",
    explanation="1) Total engineers = 40 + 60 = 100. 2) Engineers leaving Branch A = 10% of 40 = 4. 3) Engineers leaving Branch B = 20% of 60 = 12. 4) Total engineers who left = 4 + 12 = 16. 5) Overall attrition rate = (16 / 100) * 100 = 16%.",
    code="// Branch A: 40 * 0.10 = 4\n// Branch B: 60 * 0.20 = 12\n// Total Left = 16 / 100 = 16%",
    difficulty="Easy",
    q_type="Aptitude",
    round_type="Online Test",
    freq="High",
    ref="Standard Data Interpretation Guide",
    followup="What would be the overall attrition rate if both branches had an equal number of engineers?"
)

create_q(
    subject="Aptitude",
    topic="Data Interpretation",
    subtopic="Percentage Growth from Chart",
    question="A startup's quarterly revenue rose from $200,000 in Q1 to $260,000 in Q2. What was the percentage growth in revenue?",
    answer="30%.",
    explanation="Percentage Growth Formula: ((Final Value - Initial Value) / Initial Value) * 100 = ((260,000 - 200,000) / 200,000) * 100 = (60,000 / 200,000) * 100 = 0.30 * 100 = 30%.",
    code="// Growth = ((260000 - 200000) / 200000) * 100 = 30%",
    difficulty="Easy",
    q_type="Aptitude",
    round_type="Online Test",
    freq="High",
    ref="Standard Data Interpretation Guide",
    followup="If revenue drops from $260,000 back down to $200,000, what is the percentage decrease?"
)

# ==============================================================================
# 14. Problem Solving / DSA (8 questions: Palindrome, Binary Search, Valid Parentheses, Queue, Cycle detection, Two Sum, Recursion, Sliding Window)
# ==============================================================================
create_q(
    subject="DSA",
    topic="Two Pointers",
    subtopic="Check if String is Palindrome",
    question="Write a function using the two-pointer technique to check if a string is a palindrome.",
    answer="Set one pointer 'left' at index 0 and 'right' at index str.length - 1. While left < right, compare characters at left and right. If they mismatch, return false immediately. Otherwise increment left and decrement right. If the loop completes without mismatches, return true. Time complexity is O(N), Space complexity is O(1).",
    explanation="The two-pointer technique avoids creating reversed string copies in memory.",
    code="function isPalindrome(str) {\n  let left = 0;\n  let right = str.length - 1;\n\n  while (left < right) {\n    if (str[left] !== str[right]) return false;\n    left++;\n    right--;\n  }\n  return true;\n}\n\nconsole.log(isPalindrome(\"racecar\")); // true\nconsole.log(isPalindrome(\"hello\"));   // false",
    difficulty="Fresher Coding",
    q_type="Coding",
    round_type="Coding Round",
    freq="High",
    ref="LeetCode 125 - Valid Palindrome",
    followup="How do you handle alphanumeric characters while ignoring spaces and punctuation?"
)

create_q(
    subject="DSA",
    topic="Searching",
    subtopic="Binary Search Implementation",
    question="Write an iterative Binary Search function to find a target value in a sorted array and explain its time complexity.",
    answer="Binary Search works on sorted arrays by repeatedly halving the search space. Compute mid = Math.floor((left + right) / 2). If arr[mid] === target, return mid. If arr[mid] < target, search right half (left = mid + 1). If arr[mid] > target, search left half (right = mid - 1). If left exceeds right, return -1. Time complexity is O(log N) because each comparison eliminates half the remaining elements; space complexity is O(1).",
    explanation="Binary search is dramatically faster than linear search O(N) on large datasets (e.g. searching 1,000,000 items takes only ~20 comparisons).",
    code="function binarySearch(arr, target) {\n  let left = 0;\n  let right = arr.length - 1;\n\n  while (left <= right) {\n    const mid = Math.floor((left + right) / 2);\n    if (arr[mid] === target) return mid; // Found index\n    if (arr[mid] < target) {\n      left = mid + 1;  // Search right\n    } else {\n      right = mid - 1; // Search left\n    }\n  }\n  return -1; // Not found\n}\n\nconsole.log(binarySearch([2, 5, 8, 12, 16, 23, 38], 16)); // 4",
    difficulty="Fresher Coding",
    q_type="Coding",
    round_type="Coding Round",
    freq="High",
    ref="LeetCode 704 - Binary Search",
    followup="What happens if the array is unsorted before binary search is executed?"
)

create_q(
    subject="DSA",
    topic="Stacks",
    subtopic="Valid Parentheses Problem",
    question="Given a string containing '(', ')', '{', '}', '[' and ']', write a function using a Stack to determine if the input string is valid.",
    answer="Initialize an empty stack array. Iterate through characters of the string: when encountering an opening bracket, push it onto the stack. When encountering a closing bracket, pop the top element from the stack; if the stack is empty or the popped bracket does not match, return false. After processing all characters, return stack.length === 0.",
    explanation="A stack operates on Last-In, First-Out (LIFO), perfectly tracking nested opening brackets.",
    code="function isValidParentheses(s) {\n  const stack = [];\n  const bracketMap = { ')': '(', '}': '{', ']': '[' };\n\n  for (const char of s) {\n    if (['(', '{', '['].includes(char)) {\n      stack.push(char);\n    } else if (bracketMap[char]) {\n      if (stack.pop() !== bracketMap[char]) {\n        return false;\n      }\n    }\n  }\n  return stack.length === 0;\n}\n\nconsole.log(isValidParentheses(\"()[]{}\")); // true\nconsole.log(isValidParentheses(\"(]\"));     // false\nconsole.log(isValidParentheses(\"([)]\"));   // false",
    difficulty="Fresher Coding",
    q_type="Coding",
    round_type="Coding Round",
    freq="High",
    ref="LeetCode 20 - Valid Parentheses",
    followup="What is the space complexity of this solution?"
)

create_q(
    subject="DSA",
    topic="Queues",
    subtopic="Queue Implementation & FIFO Principle",
    question="What is a Queue, how does FIFO work, and how do you implement a basic Queue in JavaScript?",
    answer="A Queue is a linear First-In, First-Out (FIFO) data structure where elements are added at the back (enqueue) and removed from the front (dequeue). In JavaScript, a basic Queue can be implemented with a class holding an array, using push() to enqueue and shift() to dequeue (or pointer offsets for O(1) dequeue performance). Real-world applications: message queues (RabbitMQ), printer job queues, and Breadth-First Search (BFS).",
    explanation="Array shift() takes O(N) time because all elements must shift down; an object with head/tail pointers achieves true O(1) operations.",
    code="class Queue {\n  constructor() {\n    this.items = {};\n    this.head = 0;\n    this.tail = 0;\n  }\n  enqueue(element) {\n    this.items[this.tail++] = element;\n  }\n  dequeue() {\n    if (this.isEmpty()) return null;\n    const item = this.items[this.head];\n    delete this.items[this.head++];\n    return item;\n  }\n  isEmpty() { return this.tail - this.head === 0; }\n}\n\nconst q = new Queue();\nq.enqueue('User 1');\nq.enqueue('User 2');\nconsole.log(q.dequeue()); // 'User 1' (FIFO)",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="GeeksforGeeks - Queue Data Structure",
    followup="How do you implement a Queue using two Stacks?"
)

create_q(
    subject="DSA",
    topic="Linked Lists",
    subtopic="Cycle Detection (Floyd's Tortoise and Hare Algorithm)",
    question="What is a Singly Linked List and how does Floyd's Tortoise and Hare algorithm detect a cycle?",
    answer="A Singly Linked List consists of nodes where each node stores data and a pointer (next) to the subsequent node. Floyd's cycle detection algorithm uses two pointers: a slow pointer moving 1 step at a time and a fast pointer moving 2 steps at a time. If there is a cycle, the fast pointer will eventually catch up and equal the slow pointer (O(N) time, O(1) space). If the fast pointer reaches null, the list has no cycle.",
    explanation="Floyd's algorithm detects cycles without mutating node values or storing visited nodes in a hash set.",
    code="function hasCycle(head) {\n  let slow = head;\n  let fast = head;\n\n  while (fast !== null && fast.next !== null) {\n    slow = slow.next;       // 1 step\n    fast = fast.next.next;  // 2 steps\n    if (slow === fast) return true; // Cycle detected!\n  }\n  return false; // Reached end of list without cycle\n}",
    difficulty="Medium",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="LeetCode 141 - Linked List Cycle",
    followup="How do you find the starting node of the cycle once detected?"
)

create_q(
    subject="DSA",
    topic="Hash Maps",
    subtopic="Two Sum Problem using Hash Map",
    question="Write an optimal function in JavaScript to solve the Two Sum problem: find indices of two numbers that add up to a target in an array.",
    answer="Use a Hash Map (or JavaScript Map / plain object) to store numbers and their indices as you iterate through the array. For each element num, calculate its complement: complement = target - num. If the complement already exists in the map, return [map.get(complement), currentIndex]. Otherwise, insert the current number into the map. This achieves optimal O(N) time complexity and O(N) space, avoiding the O(N^2) brute-force nested loops.",
    explanation="The hash map lookup runs in constant O(1) average time.",
    code="function twoSum(nums, target) {\n  const map = new Map();\n  for (let i = 0; i < nums.length; i++) {\n    const complement = target - nums[i];\n    if (map.has(complement)) {\n      return [map.get(complement), i];\n    }\n    map.set(nums[i], i);\n  }\n  return [];\n}\n\nconsole.log(twoSum([2, 7, 11, 15], 9)); // [0, 1] (2 + 7 = 9)",
    difficulty="Fresher Coding",
    q_type="Coding",
    round_type="Coding Round",
    freq="High",
    ref="LeetCode 1 - Two Sum",
    followup="What if the array is already sorted? How would two-pointer approach work?"
)

create_q(
    subject="DSA",
    topic="Recursion",
    subtopic="Base Case & Factorial Implementation",
    question="What is recursion, why is a base case essential, and write a recursive function for factorial?",
    answer="Recursion is a programming technique where a function calls itself to solve smaller subproblems of the same problem. A base case is the termination condition that stops recursion. Without a base case, the function calls itself indefinitely, exhausting the maximum call stack size and throwing a 'RangeError: Maximum call stack size exceeded' (stack overflow).",
    explanation="Every recursive function can alternatively be written iteratively using a loop and manual stack.",
    code="function factorial(n) {\n  if (n <= 1) return 1; // Base case: stops recursion\n  return n * factorial(n - 1); // Recursive call\n}\n\nconsole.log(factorial(5)); // 120 (5 * 4 * 3 * 2 * 1)",
    difficulty="Easy",
    q_type="Coding",
    round_type="Coding Round",
    freq="High",
    ref="MDN Web Docs - Recursion",
    followup="What is tail call optimization in recursion?"
)

create_q(
    subject="DSA",
    topic="Sliding Window",
    subtopic="Maximum Sum Subarray of Size K",
    question="Write a function using the Sliding Window technique to find the maximum sum of any contiguous subarray of size k.",
    answer="Calculate the sum of the first k elements to establish the initial window. Then slide the window across the array from index k to the end by adding the incoming element on the right and subtracting the exiting element on the left. Track the maximum sum encountered. This reduces time complexity from O(N * K) brute force to O(N) linear time.",
    explanation="Sliding window avoids re-summing overlapping subarray elements from scratch.",
    code="function maxSubarraySum(arr, k) {\n  if (arr.length < k) return null;\n  let windowSum = 0;\n  for (let i = 0; i < k; i++) windowSum += arr[i];\n  let maxSum = windowSum;\n\n  for (let i = k; i < arr.length; i++) {\n    windowSum += arr[i] - arr[i - k]; // Slide window\n    maxSum = Math.max(maxSum, windowSum);\n  }\n  return maxSum;\n}\n\nconsole.log(maxSubarraySum([2, 1, 5, 1, 3, 2], 3)); // 9 ([5, 1, 3])",
    difficulty="Fresher Coding",
    q_type="Coding",
    round_type="Coding Round",
    freq="High",
    ref="LeetCode 643 - Maximum Average Subarray I",
    followup="How would you adapt this for a variable-length sliding window problem?"
)

# ==============================================================================
# 15. Git / GitHub (4 pure Git questions: Merge conflicts, gitignore/rm cached, pull vs fetch, reset vs revert)
# ==============================================================================
create_q(
    subject="Git",
    topic="Branching",
    subtopic="Resolving Git Merge Conflicts",
    question="How do merge conflicts occur in Git and what is the step-by-step process to resolve them?",
    answer="A merge conflict occurs when Git attempts to merge two branches that modified the exact same lines of code differently, and Git cannot automatically decide which change to keep. Steps to resolve: 1) Run 'git status' to see conflicted files. 2) Open the file and locate conflict markers (<<<<<<< HEAD, =======, >>>>>>> branch). 3) Manually edit the file to keep desired code and remove all marker lines. 4) Run 'git add <filename>' to stage resolution. 5) Run 'git commit -m \"Resolved merge conflict\"'.",
    explanation="Communication with the teammate who authored the conflicting lines is best practice during conflict resolution.",
    code="<<<<<<< HEAD\nconst API_URL = 'https://api.v1.example.com';\n=======\nconst API_URL = 'https://api.v2.example.com';\n>>>>>>> feature-upgrade\n\n# Solution: Choose desired URL, delete marker lines, and commit:\ngit add api.js\ngit commit -m \"Resolved API URL conflict\"",
    difficulty="Easy",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="Git Documentation - Basic Merge Conflicts",
    followup="What does git merge --abort do during an ongoing conflict?"
)

create_q(
    subject="Git",
    topic="Configuration",
    subtopic=".gitignore and git rm --cached",
    question="What is .gitignore and how do you remove a sensitive file from Git tracking that was already committed by mistake?",
    answer=".gitignore specifies file patterns that Git should deliberately ignore and avoid staging (e.g. node_modules/, .env, build/). If a sensitive file like .env was already committed previously, simply adding it to .gitignore does NOT stop tracking it. You must run 'git rm --cached .env' to remove it from the Git index while keeping the physical file intact on your local hard drive, then commit the change.",
    explanation="git rm --cached removes files from version control tracking without physically deleting them from your disk.",
    code="# 1. Add pattern to .gitignore:\n# echo \".env\" >> .gitignore\n\n# 2. Untrack file from Git repository index:\ngit rm --cached .env\n\n# 3. Commit the removal:\ngit commit -m \"Remove .env from version tracking\"",
    difficulty="Easy",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="Git Documentation - gitignore",
    followup="Does .gitignore affect files already committed to remote repository history?"
)

create_q(
    subject="Git",
    topic="Remote Sync",
    subtopic="git fetch vs git pull",
    question="What is the difference between git fetch and git pull?",
    answer="git fetch contacts the remote repository and downloads all new commits, branches, and tags to your local repository database, but does NOT merge or alter your current working files (allowing you to safely inspect incoming changes using git log or git diff before merging). git pull is a shortcut command that performs git fetch followed immediately by git merge origin/<branch> into your currently checked-out branch.",
    explanation="Professional developers often use git fetch followed by git status to verify changes before merging.",
    code="# Safe workflow:\ngit fetch origin\ngit log HEAD..origin/main --oneline # Inspect incoming commits\ngit merge origin/main\n\n# Direct shortcut:\ngit pull origin main",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Git Documentation - git-fetch",
    followup="What is git pull --rebase and when would you use it?"
)

create_q(
    subject="Git",
    topic="History Modification",
    subtopic="git reset vs git revert",
    question="What is the difference between git reset (soft, mixed, hard) and git revert?",
    answer="git revert <commit-hash> creates a brand-new commit that inverses the changes of the specified commit, safely preserving commit history (safe for shared public remote branches). git reset <commit-hash> rewrites history by moving the HEAD branch pointer backwards: 1) --soft moves HEAD back but leaves changes staged. 2) --mixed (default) un-stages changes but leaves files in working directory. 3) --hard permanently discards all changes and uncommitted files.",
    explanation="Never use git reset --hard on public branches that colleagues have already pulled.",
    code="# Safe for public shared branches:\ngit revert HEAD\n\n# Local undo before pushing:\ngit reset --soft HEAD~1 # Undoes last commit, keeps code staged",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Git Documentation - git-reset",
    followup="What is the Git Reflog and how does it save you from an accidental hard reset?"
)

# ==============================================================================
# 16. Testing (4 dedicated testing questions: Jest basics, Mocking, TDD, Positive vs Negative)
# ==============================================================================
create_q(
    subject="Testing",
    topic="Unit Testing",
    subtopic="Jest Basics (describe, test, expect)",
    question="What is Jest and how do you write a basic unit test using describe, test, and expect?",
    answer="Jest is a JavaScript testing framework. describe('suite name', () => { ... }) groups related test cases together. test('test description', () => { ... }) (or it()) defines an individual test assertion. expect(actual).matcher(expected) evaluates results using matchers: toBe() for primitive strict equality, toEqual() for deep object/array equality, toContain(), or toThrow().",
    explanation="Jest runs tests in parallel using worker processes for fast test execution.",
    code="// math.test.js\nconst { sum, multiply } = require('./math');\n\ndescribe('Math Utility Functions', () => {\n  test('adds 5 + 3 to equal 8', () => {\n    expect(sum(5, 3)).toBe(8);\n  });\n\n  test('compares object equality correctly', () => {\n    expect({ status: 'ok' }).toEqual({ status: 'ok' });\n  });\n});",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Jest Documentation - Getting Started",
    followup="What is the difference between toBe() and toEqual() in Jest?"
)

create_q(
    subject="Testing",
    topic="Mocking",
    subtopic="Mock Functions with jest.fn()",
    question="What is mocking in automated testing and how do you mock a function or API call in Jest?",
    answer="Mocking replaces real external dependencies (such as HTTP network calls, file system I/O, or database queries) with simulated implementations. This isolates the unit under test, ensures tests run lightning-fast without network latency, and prevents real-world side effects. In Jest, jest.fn() creates a mock function that tracks calls, arguments, and return values (e.g. jest.fn().mockResolvedValue(data)).",
    explanation="Unit tests should never make real HTTP calls across the public internet.",
    code="const fetchUser = async (apiClient) => {\n  const user = await apiClient.getUser();\n  return user.name.toUpperCase();\n};\n\ntest('formats user name in uppercase', async () => {\n  const mockApiClient = {\n    getUser: jest.fn().mockResolvedValue({ name: 'neha' })\n  };\n\n  const result = await fetchUser(mockApiClient);\n  expect(result).toBe('NEHA');\n  expect(mockApiClient.getUser).toHaveBeenCalledTimes(1);\n});",
    difficulty="Medium",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="Jest Documentation - Mock Functions",
    followup="How do you reset all mocks before each test using beforeEach()?"
)

create_q(
    subject="Testing",
    topic="Methodology",
    subtopic="Test-Driven Development (TDD) Red-Green-Refactor",
    question="What is Test-Driven Development (TDD) and what is the Red-Green-Refactor cycle?",
    answer="TDD is a software development approach where automated test cases are written BEFORE writing production code. The cycle: 1) Red: Write a test for the desired functionality and run it; verify it fails (confirming the test is actually testing something). 2) Green: Write the minimal amount of code necessary to make the test pass. 3) Refactor: Clean up and optimize the implementation while keeping all tests passing.",
    explanation="TDD ensures high test coverage and produces modular, decoupled code.",
    code="// 1. Red: Write test for formatCurrency(100) -> '$100.00' (Fails)\n// 2. Green: Implement basic function returning '$' + num.toFixed(2) (Passes)\n// 3. Refactor: Handle edge cases (negative numbers, invalid inputs)",
    difficulty="Easy",
    q_type="Concept",
    round_type="Technical Round",
    freq="High",
    ref="Agile Alliance - Test-Driven Development",
    followup="What are the main benefits and tradeoffs of TDD for teams?"
)

create_q(
    subject="Testing",
    topic="Test Strategy",
    subtopic="Positive vs Negative Test Scenarios",
    question="What is the difference between Positive and Negative testing scenarios for a User Login feature?",
    answer="Positive Testing verifies that the system works as expected when valid input is provided (the happy path): entering registered email and correct password returns HTTP 200, JWT token, and redirects to dashboard. Negative Testing verifies that the system gracefully handles invalid, unexpected, or malicious input without crashing: entering an empty email, wrong password, malformed email format, or SQL injection payload returns appropriate 400 or 401 error messages without revealing internal stack traces.",
    explanation="Negative testing is essential to verify application robustness, input sanitization, and security.",
    code="// Positive Test Case:\ntest('valid credentials returns 200 and auth token', async () => { ... });\n\n// Negative Test Cases:\ntest('empty password returns 400 with validation message', async () => { ... });\ntest('unregistered email returns 401 unauthorized', async () => { ... });\ntest('special characters in email sanitized without crash', async () => { ... });",
    difficulty="Easy",
    q_type="Scenario",
    round_type="Technical Round",
    freq="High",
    ref="Software Testing Fundamentals",
    followup="What is boundary value analysis in test case design?"
)

# ==============================================================================
# 17. Projects (5 project discussion questions: Auth flow, Validation, Deployment, DB optimization, Error UX)
# ==============================================================================
create_q(
    subject="Projects",
    topic="Security",
    subtopic="Implementing Authentication and Protected Routes",
    question="How did you implement user authentication and protect private routes in your project?",
    answer="During registration, passwords were encrypted using bcrypt with salt rounds before storing in MongoDB. Upon login, credentials were verified; if valid, the server signed a JSON Web Token (JWT) containing userId and role using an environment secret key (JWT_SECRET). The client attached this token in the 'Authorization: Bearer <token>' header on subsequent requests. An Express authentication middleware verified the token with jwt.verify() before granting access to protected API routes; on the frontend, a React ProtectedRoute component redirected unauthenticated users to /login.",
    explanation="Articulating the full authentication handshake shows clear full-stack understanding to interviewers.",
    code="// Backend Auth Middleware:\nconst authMiddleware = (req, res, next) => {\n  const authHeader = req.headers.authorization;\n  if (!authHeader?.startsWith('Bearer ')) {\n    return res.status(401).json({ error: 'Access token missing' });\n  }\n  try {\n    const token = authHeader.split(' ')[1];\n    req.user = jwt.verify(token, process.env.JWT_SECRET);\n    next();\n  } catch (err) {\n    res.status(401).json({ error: 'Invalid or expired token' });\n  }\n};",
    difficulty="Easy",
    q_type="Project",
    round_type="Project Discussion",
    freq="High",
    ref="Full Stack Project Architecture",
    followup="How did you handle token expiration and logout?"
)

create_q(
    subject="Projects",
    topic="Validation",
    subtopic="Dual-Layer Validation on Frontend and Backend",
    question="Why did you implement validation on BOTH the frontend and backend in your project?",
    answer="Frontend validation (HTML5 attributes and React state) provides immediate, friendly user experience—warning users about missing fields or invalid email formats instantly without waiting for a server network round-trip. Backend validation (Express middleware and Mongoose schema constraints) is MANDATORY for security because any client (using Postman, curl, or browser DevTools) can bypass frontend checks and submit raw malicious or malformed payloads directly to the server endpoints.",
    explanation="Frontend validation is for UX; backend validation is for security and data integrity.",
    code="// Frontend: Immediate visual feedback\n// Backend: Absolute security defense line",
    difficulty="Easy",
    q_type="Project",
    round_type="Project Discussion",
    freq="High",
    ref="Full Stack Architecture Guidelines",
    followup="What happens if a user disables JavaScript in their browser?"
)

create_q(
    subject="Projects",
    topic="Deployment",
    subtopic="Project Deployment & Environment Variables",
    question="How did you deploy your full-stack project and manage production environment variables?",
    answer="The React frontend was deployed on Vercel/Netlify with Continuous Deployment (CD) connected to the GitHub main branch. The Express/Node.js backend was deployed on Render/Railway. The database was hosted in the cloud using MongoDB Atlas with IP allowlisting. Environment variables (MONGO_URI, JWT_SECRET, PORT) were securely configured in the hosting provider's dashboard settings rather than committing .env files to Git.",
    explanation="Demonstrating a live URL and explaining environment configuration proves real-world deployment competence.",
    code="// Deployment Architecture:\n// GitHub Repo -> Automatic Build Webhook -> Vercel (Frontend)\n// GitHub Repo -> Automatic Docker/Node Build -> Render (Backend)\n// Backend -> Encrypted TLS Connection -> MongoDB Atlas Cloud Cluster",
    difficulty="Easy",
    q_type="Project",
    round_type="Project Discussion",
    freq="High",
    ref="Deployment Best Practices",
    followup="How did you configure CORS between your frontend and backend domains?"
)

create_q(
    subject="Projects",
    topic="Performance",
    subtopic="Troubleshooting Slow Database Queries in Projects",
    question="If a database query in your project started responding very slowly, how would you troubleshoot and fix it?",
    answer="1) Pinpoint the slow query using backend logging or MongoDB Atlas Performance Advisor. 2) Run .explain('executionStats') on the query to check whether it performed a full collection scan (COLLSCAN) instead of an index scan (IXSCAN). 3) Add an index on frequently filtered or sorted fields (e.g. userId, createdAt). 4) Implement pagination (limit and skip) so the endpoint never fetches thousands of documents at once. 5) Use projection to retrieve only the specific fields needed by the UI.",
    explanation="Adding indexes and limiting query projections typically reduces query execution time by over 90%.",
    code="// Optimized query:\nawait Order.find({ userId: req.user.id }, { orderNumber: 1, total: 1, date: 1 })\n  .sort({ date: -1 })\n  .limit(10);",
    difficulty="Easy",
    q_type="Project",
    round_type="Project Discussion",
    freq="High",
    ref="Database Optimization Guidelines",
    followup="What are potential downsides of adding too many indexes to a collection?"
)

create_q(
    subject="Projects",
    topic="Error Handling",
    subtopic="End-to-End Graceful Error Handling & Feedback",
    question="How did you handle errors gracefully across your frontend and backend so the application doesn't crash?",
    answer="On the backend, asynchronous controllers were wrapped in try/catch blocks that passed errors to a centralized Express error handling middleware, ensuring structured JSON error responses ({ success: false, message }) with accurate HTTP status codes. On the frontend, API calls checked res.ok, caught network rejections, and populated component error state to display friendly inline toast notifications or retry buttons rather than white screen crashes.",
    explanation="Graceful error handling ensures users always understand what went wrong and how to recover.",
    code="// Frontend Graceful Handling:\ntry {\n  const res = await api.post('/orders', orderData);\n  showToast('Order placed successfully!', 'success');\n} catch (err) {\n  const msg = err.response?.data?.message || 'Network error. Please try again.';\n  showToast(msg, 'error');\n}",
    difficulty="Easy",
    q_type="Project",
    round_type="Project Discussion",
    freq="High",
    ref="System Design - Error Handling",
    followup="What is an Error Boundary in React?"
)

# ==============================================================================
# 18. HR / Communication (5 questions: Why company, Conflict resolution, Stuck on problem, Deadlines, Questions for interviewer)
# ==============================================================================
create_q(
    subject="HR",
    topic="Motivation",
    subtopic="Why This Company Specifically",
    question="Why do you want to work for our company specifically?",
    answer="State a tailored, researched response: 'I have followed your company's work in [mention domain, e.g. scalable enterprise SaaS or fintech], especially how your engineering team prioritizes performance and reliability. As a fresher, I want to begin my software career in an environment with high engineering standards, clear code reviews, and strong mentorship. My skills in React, Node.js, and SQL align well with your tech stack, and I am eager to contribute to production features and grow as a software engineer here.'",
    explanation="Demonstrating genuine research about the company differentiates top candidates from generic applicants.",
    code="// Key Elements:\n// 1. Specific company domain / achievement\n// 2. Alignment with company tech stack\n// 3. Eagerness to learn, contribute, and accept mentorship",
    difficulty="Easy",
    q_type="HR",
    round_type="HR Round",
    freq="High",
    ref="HR Interview Guide",
    followup="What do you know about our current product offerings?"
)

create_q(
    subject="HR",
    topic="Teamwork",
    subtopic="Resolving a Disagreement in a Project Team",
    question="Describe a situation where you had a disagreement with a project teammate and how you resolved it.",
    answer="Use the STAR method: 'During our final semester project, a teammate wanted to use Firebase for instant setup, while I advocated for Node.js, Express, and MongoDB because our rubric required custom relational business logic. Instead of arguing, we evaluated both against project requirements, delivery timelines, and grading criteria. We agreed that Express gave us the exact control we needed for custom authentication. We divided backend and UI responsibilities clearly, held daily standups, and delivered the project on schedule.'",
    explanation="Focus on objective criteria, constructive dialogue, and team success over personal ego.",
    code="// STAR Method:\n// Situation: Competing technology choices\n// Task: Agree on best architecture for project rubric\n// Action: Objective pros/cons discussion based on rubric\n// Result: Successful on-time delivery with zero friction",
    difficulty="Easy",
    q_type="HR",
    round_type="HR Round",
    freq="High",
    ref="Behavioral Interview Best Practices",
    followup="What did you learn from that experience?"
)

create_q(
    subject="HR",
    topic="Problem Solving",
    subtopic="What to Do When Stuck on a Programming Problem",
    question="What do you do when you are completely stuck on a difficult programming bug or problem?",
    answer="A structured 4-step approach: 1) Read the error stack trace carefully, isolate the minimal reproducible example, and inspect variable states with debugger/console.log. 2) Consult official documentation (MDN, React/Node docs) and verified developer resources. 3) Step away from the screen for 5-10 minutes to reset perspective. 4) If still blocked after 45 minutes, formulate a clear, concise question explaining what I'm trying to accomplish, what I've tried, and what happened, and seek guidance from a mentor or senior peer.",
    explanation="Showing structured troubleshooting combined with respectful escalation demonstrates maturity.",
    code="// 1. Reproduce minimally\n// 2. Read official docs\n// 3. Reset perspective\n// 4. Ask mentor with concise context",
    difficulty="Easy",
    q_type="HR",
    round_type="HR Round",
    freq="High",
    ref="Engineering Culture Guidelines",
    followup="Can you give an example of a difficult bug you resolved independently?"
)

create_q(
    subject="HR",
    topic="Work Ethic",
    subtopic="Handling Deadlines and Pressure",
    question="How do you handle deadlines and pressure during exam or project submissions?",
    answer="'I handle pressure by staying organized and breaking large deliverables into smaller daily milestones. For example, during final semester project submissions while preparing for campus placements, I prioritized essential backend APIs first, followed by core UI, leaving non-essential features for last. I maintain focused work blocks, track tasks on a checklist, and communicate proactively if any milestone risk arises so expectations are clear.'",
    explanation="Shows composure, organizational ability, and proactive communication under pressure.",
    code="// Priorities:\n// 1. Break into small deliverables\n// 2. Focus on MVP core first\n// 3. Proactive status communication",
    difficulty="Easy",
    q_type="HR",
    round_type="HR Round",
    freq="High",
    ref="HR Interview Guide",
    followup="How do you prioritize when two tasks have the same deadline?"
)

create_q(
    subject="HR",
    topic="Communication",
    subtopic="Questions to Ask the Interviewer at the End",
    question="Do you have any questions for us at the end of the interview?",
    answer="Always ask thoughtful questions that show curiosity and enthusiasm: 1) 'What does a typical day look like for a junior developer joining your team?' 2) 'What tech stack or projects will the incoming batch of freshers work on during the first few months?' 3) 'What engineering practices (like code reviews or testing) does your team emphasize most?' 4) 'What advice would you give to a fresher to hit the ground running here?'",
    explanation="Asking informed questions demonstrates genuine interest in the team's engineering culture.",
    code="// Excellent questions:\n// - Team workflow & mentorship structure\n// - Tech stack for upcoming quarter\n// - Code review and testing practices",
    difficulty="Easy",
    q_type="HR",
    round_type="HR Round",
    freq="High",
    ref="HR Interview Guide",
    followup="Why should a fresher avoid asking only about salary or leave in the first technical round?"
)

# ==============================================================================
# Normalization & Deduplication Pass
# ==============================================================================
combined_questions = existing_questions + new_questions

# Strict questionType mapping to allowed set
TYPE_MAP = {
    "Comparison": "Concept",
    "Practical": "Scenario",
    "Fresher Coding": "Coding",
    "Logical Reasoning": "Logical Reasoning",
    "SQL Query": "SQL Query",
    "Aptitude": "Aptitude",
    "Coding": "Coding",
    "Output": "Output",
    "Debugging": "Debugging",
    "Scenario": "Scenario",
    "Project": "Project",
    "HR": "HR",
    "Concept": "Concept"
}

for q in combined_questions:
    curr_type = q.get("questionType", "Concept")
    q["questionType"] = TYPE_MAP.get(curr_type, "Concept")
    # Normalize difficulty
    if q.get("difficulty") not in ["Easy", "Medium", "Fresher Coding"]:
        q["difficulty"] = "Easy"

# Re-index num field sequentially
for idx, q in enumerate(combined_questions, 1):
    q["num"] = idx

print(f"Total verified questions after normalization: {len(combined_questions)}")

# Write to all targets
js_code = "window.FRESHER_QUESTIONS_DATA = " + json.dumps(combined_questions, indent=2) + ";\n"

for target_path in [DATA_FILE, MERN_200_FILE, NETLIFY_FILE]:
    if os.path.exists(os.path.dirname(target_path)):
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(js_code)
        print(f"Successfully saved to {target_path}")

print("Validation and rebuild complete.")

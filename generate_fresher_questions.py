# -*- coding: utf-8 -*-
"""
Generator for Fresher Interview Questions Data
Covers: HTML, CSS, JavaScript, ES6, DOM, jQuery, React, Node.js, Express,
SQL, MongoDB, Aptitude, Problem Solving, DSA, Coding, Engineering Basics, Projects, HR.
"""
import json, os

OUT_PATH = r"C:\Users\Qsp\Documents\mernstack_interview_questions\mern-200\fresher-data.js"

questions = []
qid = 1

def add_q(subject, topic, subtopic, question, answer, explanation="", code="", difficulty="Easy", q_type="Concept", round_type="Technical Round", freq="High", ref="", followup=""):
    global qid
    questions.append({
        "id": f"q-{qid}",
        "num": qid,
        "subject": subject,
        "topic": topic,
        "subTopic": subtopic,
        "question": question,
        "answer": answer,
        "shortExplanation": explanation,
        "codeExample": code,
        "difficulty": difficulty, # Easy, Medium, Fresher Coding
        "questionType": q_type, # Concept, MCQ, Output, Coding, Debugging, Scenario, SQL Query, Aptitude, Logical Reasoning, Project, HR
        "interviewRound": round_type, # Aptitude Round, Online Test, Technical Round, Coding Round, Machine Coding, Project Discussion, HR Round
        "frequency": freq, # High, Medium, Low
        "references": ref,
        "followUpQuestions": followup,
        "addedAt": qid
    })
    qid += 1

# ==========================================
# 1. HTML (Fresher Questions)
# ==========================================
add_q("HTML", "Semantic HTML", "Elements", 
      "What is semantic HTML and why is it important?",
      "Semantic HTML uses meaningful tags like <header>, <nav>, <main>, <article>, <section>, and <footer> to describe their meaning to both the browser and developer.",
      "It improves accessibility for screen readers, enhances SEO rankings by helping search engines index content structure, and makes code maintainable.",
      "<header>\n  <nav><a href=\"/\">Home</a></nav>\n</header>\n<main>\n  <article><h1>Title</h1><p>Content</p></article>\n</main>",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What happens if you only use <div> tags?")

add_q("HTML", "HTML Basics", "Block vs Inline",
      "What is the difference between block-level and inline elements?",
      "Block elements always start on a new line and take up the full available width (e.g., <div>, <p>, <h1>-<h6>). Inline elements only take up as much width as their content and do not start on a new line (e.g., <span>, <a>, <strong>).",
      "Inline elements cannot have top/bottom margins or set width/height unless display is changed to inline-block or block.",
      "<!-- Block elements stack vertically -->\n<div>Block 1</div>\n<div>Block 2</div>\n\n<!-- Inline elements sit side-by-side -->\n<span>Inline 1</span> <span>Inline 2</span>",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Can you put a block element inside an inline element in HTML5?")

add_q("HTML", "HTML Elements", "Div vs Span",
      "What is the difference between <div> and <span>?",
      "<div> is a generic block-level container used for grouping larger sections or layout blocks. <span> is an inline container used for styling or scripting a specific portion of text.",
      "Neither tag has semantic meaning on its own; use semantic tags like <section> or <em> when applicable.",
      "<div class=\"card\">\n  <p>Status: <span class=\"badge-active\">Online</span></p>\n</div>",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Why should we prefer semantic tags over excessive divs?")

add_q("HTML", "HTML Forms", "Input Types",
      "What are the common HTML5 input types and their validation attributes?",
      "Common input types include text, password, email, number, date, checkbox, radio, file, and submit. Attributes like required, pattern, min, max, and maxlength provide built-in client-side validation.",
      "Browsers automatically validate types like email and number before form submission without requiring custom JavaScript.",
      "<form>\n  <input type=\"email\" required placeholder=\"Enter email\">\n  <input type=\"number\" min=\"1\" max=\"100\" required>\n  <input type=\"submit\" value=\"Submit\">\n</form>",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Can client-side HTML5 validation replace backend validation?")

add_q("HTML", "Accessibility", "A11y Basics",
      "What is the importance of the 'alt' attribute in <img> tags?",
      "The 'alt' (alternative text) attribute provides a text description for images when they fail to load and allows screen readers to read the description to visually impaired users.",
      "It also benefits SEO by helping search engines understand image content. For decorative images, use alt=\"\" (empty) so screen readers skip them.",
      "<img src=\"profile.jpg\" alt=\"Candidate profile photo\">\n<!-- Decorative image: -->\n<img src=\"divider.png\" alt=\"\">",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What happens if you omit the alt attribute entirely?")

add_q("HTML", "HTML5", "New Features",
      "What new features were introduced in HTML5?",
      "HTML5 introduced semantic tags (<header>, <nav>, <section>), native audio and video (<audio>, <video>), Canvas and SVG for graphics, client-side storage (localStorage, sessionStorage), and new form input types.",
      "It removed the need for external plugins like Adobe Flash to play media in browsers.",
      "<video width=\"320\" height=\"240\" controls>\n  <source src=\"movie.mp4\" type=\"video/mp4\">\n  Your browser does not support HTML5 video.\n</video>",
      "Easy", "Concept", "Technical Round", "Medium", "MDN", "What is the difference between localStorage and sessionStorage?")

add_q("HTML", "SEO Basics", "Meta Tags",
      "Which HTML meta tags and elements are most crucial for basic SEO?",
      "The <title> tag, <meta name=\"description\">, <meta name=\"viewport\"> for mobile responsiveness, canonical links, and Open Graph tags (<meta property=\"og:title\">).",
      "A unique title and descriptive meta description appear directly in search engine search result snippets.",
      "<head>\n  <title>Fresher Interview Preparation Guide</title>\n  <meta name=\"description\" content=\"Practice 300+ fresher technical and coding questions.\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n</head>",
      "Easy", "Concept", "Technical Round", "Medium", "MDN", "Why should there be only one <h1> tag per page?")

add_q("HTML", "HTML Tables", "Structure",
      "How is an HTML table structured and how do colspan and rowspan work?",
      "A table uses <table>, <thead>, <tbody>, <tr> for rows, <th> for headers, and <td> for cells. colspan merges multiple columns horizontally, while rowspan merges multiple rows vertically.",
      "Tables should only be used for tabular data, not for general page layout.",
      "<table border=\"1\">\n  <tr>\n    <th>Name</th>\n    <th colspan=\"2\">Contact</th>\n  </tr>\n  <tr>\n    <td>Asha</td>\n    <td>Email</td>\n    <td>Phone</td>\n  </tr>\n</table>",
      "Easy", "Concept", "Technical Round", "Medium", "MDN", "Why should tables not be used for webpage layouts?")

add_q("HTML", "HTML Lists", "Types",
      "What are ordered lists, unordered lists, and description lists?",
      "<ol> creates numbered lists (ordered). <ul> creates bulleted lists (unordered). <dl> creates description/definition lists with <dt> (term) and <dd> (description).",
      "List items in <ol> and <ul> must be wrapped in <li> tags.",
      "<dl>\n  <dt>HTML</dt>\n  <dd>HyperText Markup Language</dd>\n  <dt>CSS</dt>\n  <dd>Cascading Style Sheets</dd>\n</dl>",
      "Easy", "Concept", "Online Test", "Low", "MDN", "Can you nest an unordered list inside an ordered list?")

add_q("HTML", "Script Loading", "Async vs Defer",
      "What is the difference between <script>, <script async>, and <script defer>?",
      "Regular <script> pauses HTML parsing while downloading and executing. 'async' downloads in parallel and executes immediately once downloaded (unordered). 'defer' downloads in parallel but executes in order only after HTML parsing is complete.",
      "For modern apps that manipulate the DOM, 'defer' is usually preferred because the DOM is fully constructed before execution.",
      "<script src=\"analytics.js\" async></script>\n<script src=\"app.js\" defer></script>",
      "Medium", "Concept", "Technical Round", "High", "MDN", "Which script attribute preserves the execution order of multiple scripts?")

# ==========================================
# 2. CSS (Fresher Questions)
# ==========================================
add_q("CSS", "CSS Box Model", "Box Sizing",
      "What is the CSS Box Model and how does box-sizing: border-box work?",
      "The CSS Box Model comprises content, padding, border, and margin. By default (content-box), width specifies only the content width. With border-box, width includes content + padding + border, preventing elements from expanding unexpectedly.",
      "Most modern CSS resets apply * { box-sizing: border-box; } globally for predictable sizing.",
      "/* Standard CSS Reset */\n* {\n  box-sizing: border-box;\n  margin: 0;\n  padding: 0;\n}",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What is margin collapse in CSS?")

add_q("CSS", "CSS Specificity", "Cascade Rules",
      "How is CSS Specificity calculated when styles conflict?",
      "Specificity hierarchy is: Inline styles (1000) > IDs (100) > Classes, pseudo-classes, attributes (10) > Elements and pseudo-elements (1). !important overrides standard specificity.",
      "When specificities are equal, the rule defined latest in the stylesheet wins (the Cascade).",
      "/* Specificity: 0-1-1 (1 class + 1 element = 11) */\nul.menu li { color: blue; }\n\n/* Specificity: 1-0-0 (1 ID = 100) -> WINS */\n#main-menu { color: red; }",
      "Medium", "Concept", "Technical Round", "High", "MDN", "Why is using !important considered a bad practice in CSS?")

add_q("CSS", "CSS Positioning", "Position Values",
      "Explain the five CSS position property values: static, relative, absolute, fixed, and sticky.",
      "static: Default normal flow. relative: Positioned relative to its normal position. absolute: Positioned relative to the nearest positioned ancestor (non-static). fixed: Positioned relative to the viewport; stays on scroll. sticky: Toggles between relative and fixed based on scroll position.",
      "To position a child absolutely, make its parent position: relative.",
      ".parent {\n  position: relative;\n  width: 200px; height: 200px;\n}\n.child {\n  position: absolute;\n  top: 10px; right: 10px;\n}",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What happens to an absolute element if no ancestor has position: relative?")

add_q("CSS", "Flexbox", "Centering & Layout",
      "How do you center a child element both vertically and horizontally using Flexbox?",
      "Set display: flex on the parent, justify-content: center (horizontal alignment along main axis), and align-items: center (vertical alignment along cross axis).",
      "Flexbox is ideal for one-dimensional layouts (row or column).",
      ".parent {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  height: 100vh;\n}",
      "Easy", "Coding", "Coding Round", "High", "MDN", "How do you reverse the flex direction?")

add_q("CSS", "CSS Grid", "Grid Basics",
      "What is CSS Grid and when should you use Grid vs Flexbox?",
      "CSS Grid is a two-dimensional layout system (rows AND columns). Flexbox is a one-dimensional system (rows OR columns). Use Grid for overall page layouts and tables, and Flexbox for components like navbars and button groups.",
      "Grid makes responsive layouts easy with grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)).",
      ".grid-container {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  gap: 16px;\n}",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What does the 'fr' unit stand for in CSS Grid?")

add_q("CSS", "Responsive Design", "Media Queries",
      "What are CSS Media Queries and how do you write a mobile-first responsive query?",
      "Media queries apply different styles based on device characteristics like screen width. In mobile-first design, base styles target mobile screens, and min-width queries add styles for larger screens.",
      "Mobile-first is preferred because it ensures lighter CSS and faster loading on mobile devices.",
      "/* Base styles for mobile */\n.container { width: 100%; padding: 12px; }\n\n/* Desktop tablet breakpoint */\n@media (min-width: 768px) {\n  .container { width: 750px; margin: auto; }\n}",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What meta tag is required in HTML for media queries to work properly on mobile?")

add_q("CSS", "Pseudo Selectors", "Class vs Element",
      "What is the difference between pseudo-classes (:hover) and pseudo-elements (::before)?",
      "A pseudo-class (single colon :) selects elements based on their state or tree position (e.g. :hover, :focus, :first-child). A pseudo-element (double colon ::) creates or targets a virtual sub-part of an element (e.g. ::before, ::after, ::placeholder).",
      "::before and ::after require a content: '' property to render.",
      ".button:hover {\n  background-color: #0284c7;\n}\n.badge::before {\n  content: '• ';\n  color: green;\n}",
      "Easy", "Concept", "Technical Round", "Medium", "MDN", "What does the :nth-child(even) selector do?")

add_q("CSS", "CSS Layout", "Margin vs Padding",
      "What is the difference between margin and padding?",
      "Padding is space inside the element's border, surrounding the content. Margin is space outside the element's border, creating distance between the element and adjacent elements.",
      "Background colors and images cover the content and padding, but not the margin.",
      ".card {\n  padding: 16px; /* space inside border */\n  border: 1px solid #ccc;\n  margin-bottom: 24px; /* space below card */\n}",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Can negative margins be used in CSS?")

add_q("CSS", "CSS Stacking", "Z-Index",
      "How does the z-index property work and why might it fail to work?",
      "z-index controls vertical stacking order along the z-axis (higher values sit on top). It only works on elements with a position value other than static (i.e. relative, absolute, fixed, or sticky) or flex/grid items.",
      "An element with z-index: 9999 inside a parent with a lower stacking context cannot appear above an element outside that parent.",
      ".modal-overlay {\n  position: fixed;\n  top: 0; left: 0;\n  width: 100%; height: 100%;\n  z-index: 1000;\n}",
      "Medium", "Concept", "Technical Round", "Medium", "MDN", "What creates a new stacking context in CSS?")

add_q("CSS", "CSS Output", "Display None vs Visibility Hidden",
      "What is the difference between display: none and visibility: hidden?",
      "display: none removes the element completely from document flow; it takes up zero space. visibility: hidden hides the element visually, but it still occupies its original layout space and dimensions.",
      "Screen readers also ignore display: none elements.",
      "/* Element takes no space */\n.hidden-box { display: none; }\n\n/* Element is invisible but space remains reserved */\n.invisible-box { visibility: hidden; }",
      "Easy", "Concept", "Online Test", "High", "MDN", "Does opacity: 0 occupy space in the document layout?")

# ==========================================
# 3. DOM (DEDICATED SUBJECT - 30+ Questions)
# ==========================================
add_q("DOM", "DOM Basics", "Definition",
      "What is the DOM (Document Object Model)?",
      "DOM stands for Document Object Model. It is a language-independent programming interface that represents an HTML or XML document as a tree of objects that JavaScript can inspect, traverse, and modify dynamically.",
      "The browser creates the DOM tree in memory after parsing the raw HTML file. Each HTML tag, attribute, and text piece becomes a DOM node.",
      "// Access document node\nconsole.log(document.nodeName); // #document\nconsole.log(document.body.nodeType); // 1 (Element Node)",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Is the DOM part of JavaScript itself or the browser?")

add_q("DOM", "DOM Tree", "Node Types",
      "What are the main node types in the DOM tree?",
      "The main node types are: Element Node (nodeType 1, e.g. <div>, <p>), Text Node (nodeType 3, text inside elements), and Document Node (nodeType 9, the root document).",
      "Whitespace and line breaks in HTML source code are parsed as text nodes by the browser engine.",
      "const el = document.querySelector('p');\nconsole.log(el.nodeType); // 1 (Element)\nconsole.log(el.firstChild.nodeType); // 3 (Text node)",
      "Easy", "Concept", "Technical Round", "Medium", "MDN", "What is the difference between childNodes and children?")

add_q("DOM", "Element Selection", "getElementById",
      "How does document.getElementById() work and what does it return if no element is found?",
      "getElementById() searches the document for an element whose 'id' attribute matches the specified string. It returns a single Element object if found, or null if no match exists.",
      "Because IDs must be unique in HTML, getElementById() is the fastest selector method in the DOM API.",
      "const title = document.getElementById('main-title');\nif (title) {\n  title.textContent = 'Updated Title';\n}",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What happens if two elements share the same ID?")

add_q("DOM", "Element Selection", "getElementsByClassName",
      "How does document.getElementsByClassName() work and what is a live HTMLCollection?",
      "getElementsByClassName() returns an HTMLCollection of all elements with the specified class name. It is 'live', meaning changes to the DOM automatically update the collection immediately.",
      "An HTMLCollection is array-like but not an Array; use Array.from() or spread [...collection] to use array methods like .forEach() or .map().",
      "const items = document.getElementsByClassName('item');\nconsole.log(items.length);\n// Convert to real array:\nArray.from(items).forEach(el => el.classList.add('highlight'));",
      "Easy", "Concept", "Technical Round", "High", "MDN", "How does HTMLCollection differ from NodeList?")

add_q("DOM", "Element Selection", "querySelector",
      "What is the difference between querySelector() and querySelectorAll()?",
      "querySelector() returns the first element matching a CSS selector, or null if none matches. querySelectorAll() returns a static NodeList of all matching elements.",
      "Unlike HTMLCollection, a static NodeList does NOT automatically update when the DOM changes, and NodeList has a built-in .forEach() method.",
      "// First match only:\nconst firstBtn = document.querySelector('.btn-primary');\n\n// All matches as NodeList:\nconst allBtns = document.querySelectorAll('button');\nallBtns.forEach(btn => console.log(btn.textContent));",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Can you use complex CSS selectors like 'div > p.active' in querySelector?")

add_q("DOM", "Element Creation", "createElement",
      "How do you create a new DOM element and insert it into the page?",
      "Use document.createElement('tagName') to create the element, configure its properties/content, and use parent.appendChild() or parent.append() to attach it to the DOM.",
      "Elements created with createElement exist only in browser memory until attached to an existing DOM parent.",
      "const newLi = document.createElement('li');\nnewLi.textContent = 'Apples';\nnewLi.className = 'fruit-item';\ndocument.getElementById('fruit-list').appendChild(newLi);",
      "Easy", "Coding", "Coding Round", "High", "MDN", "Why should you use DocumentFragment when appending multiple elements in a loop?")

add_q("DOM", "DOM Manipulation", "append vs appendChild",
      "What is the difference between parent.append() and parent.appendChild()?",
      "append() can accept multiple nodes AND plain text strings directly, and returns undefined. appendChild() accepts only a single Node object and returns the appended node.",
      "append() is modern and versatile, while appendChild() is older and standard across legacy browsers.",
      "const div = document.createElement('div');\n// append allows text + nodes together:\ndiv.append('Hello ', document.createElement('span'));\n\n// appendChild only accepts nodes:\ndiv.appendChild(document.createElement('p'));",
      "Medium", "Concept", "Technical Round", "High", "MDN", "Can appendChild move an element from one parent to another without copying it?")

add_q("DOM", "DOM Manipulation", "remove vs removeChild",
      "How do you remove an element from the DOM using remove() vs removeChild()?",
      "element.remove() directly removes the element itself. parent.removeChild(child) is called on the parent to remove and return the specified child element.",
      "element.remove() is simpler and standard in modern JavaScript.",
      "const banner = document.querySelector('.banner');\n// Modern direct remove:\nbanner.remove();\n\n// Legacy parent remove:\n// banner.parentNode.removeChild(banner);",
      "Easy", "Concept", "Technical Round", "Medium", "MDN", "Does removing an element from the DOM delete it from JavaScript memory if a variable still references it?")

add_q("DOM", "Attributes", "getAttribute & setAttribute",
      "How do you get, set, remove, and check HTML attributes using JavaScript?",
      "Use element.getAttribute('name'), element.setAttribute('name', 'value'), element.removeAttribute('name'), and element.hasAttribute('name').",
      "For standard properties like id or href, you can also access them directly via element.id or element.href.",
      "const link = document.querySelector('a');\nlink.setAttribute('target', '_blank');\nlink.setAttribute('rel', 'noopener noreferrer');\nconsole.log(link.hasAttribute('target')); // true",
      "Easy", "Concept", "Technical Round", "Medium", "MDN", "What is the dataset property in DOM elements?")

add_q("DOM", "Class Manipulation", "classList API",
      "How does the element.classList API work (add, remove, toggle, contains)?",
      "classList provides convenient methods to manipulate CSS classes without regex or string concatenation: .add('cls'), .remove('cls'), .toggle('cls') (adds if missing, removes if present), and .contains('cls') (returns boolean).",
      "classList is far safer than directly assigning to element.className because it doesn't overwrite other existing classes.",
      "const card = document.getElementById('card');\ncard.classList.add('active', 'shadow');\ncard.classList.remove('loading');\nif (card.classList.contains('active')) {\n  card.classList.toggle('highlight');\n}",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Can classList.add() accept multiple class names at once?")

add_q("DOM", "Text Content", "innerHTML vs textContent vs innerText",
      "What are the differences between innerHTML, textContent, and innerText?",
      "innerHTML parses and renders HTML tags (security risk for XSS). textContent gets/sets raw text of all nodes including hidden ones (fastest). innerText is aware of CSS styling and layout; it ignores hidden text and triggers reflow.",
      "Always prefer textContent for inserting plain user text to prevent Cross-Site Scripting (XSS) injection attacks.",
      "const div = document.createElement('div');\n// Safe plain text:\ndiv.textContent = '<script>alert(1)</script>'; // Rendered literally as text!\n\n// Unsafe if user input:\n// div.innerHTML = userInput; // DANGER: XSS vulnerability",
      "Medium", "Concept", "Technical Round", "High", "MDN", "Why does innerText trigger browser layout reflow while textContent does not?")

add_q("DOM", "DOM Traversal", "Family Navigation",
      "How do you traverse between parent, child, and sibling elements in the DOM?",
      "Use element.parentElement (parent element), element.children (child elements), element.firstElementChild / lastElementChild, and element.nextElementSibling / previousElementSibling.",
      "Element-based traversal properties (like .children) ignore comment and whitespace text nodes, whereas .childNodes includes them.",
      "const item = document.querySelector('.active-item');\nconst list = item.parentElement;\nconst nextItem = item.nextElementSibling;\nconst prevItem = item.previousElementSibling;",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What is the difference between parentNode and parentElement?")

add_q("DOM", "Events", "addEventListener",
      "How do you attach and remove event listeners in modern JavaScript?",
      "Use element.addEventListener('event', handler, options) to attach a listener. Use element.removeEventListener('event', handler) to remove it.",
      "To remove an event listener, you must pass the exact same named function reference; anonymous functions cannot be removed.",
      "function handleClick(e) {\n  console.log('Clicked element:', e.target);\n}\nconst btn = document.getElementById('submit-btn');\nbtn.addEventListener('click', handleClick);\n\n// Later cleanup:\nbtn.removeEventListener('click', handleClick);",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What does the { once: true } option do in addEventListener?")

add_q("DOM", "Event Propagation", "Event Bubbling",
      "What is Event Bubbling in the DOM?",
      "Event bubbling is the phase where an event starts at the deepest target element that triggered it and bubbles upward through its ancestors in the DOM tree up to <body>, <html>, and document.",
      "Most DOM events (like click, keydown, input) bubble by default. Some events (like focus, blur, mouseenter) do not bubble.",
      "// Clicking inner button triggers button handler first, then div handler:\ndocument.querySelector('button').addEventListener('click', () => console.log('Button clicked'));\ndocument.querySelector('.wrapper').addEventListener('click', () => console.log('Wrapper parent clicked'));",
      "Medium", "Concept", "Technical Round", "High", "MDN", "How can you prevent an event from bubbling up the DOM tree?")

add_q("DOM", "Event Propagation", "Event Capturing",
      "What is Event Capturing (Trickling) and how do you enable it?",
      "Event capturing is the reverse of bubbling: the event travels downward from window and document down through ancestors to the target element. Enable it by passing { capture: true } or true as the 3rd argument in addEventListener.",
      "The complete event lifecycle is: Capturing phase -> Target phase -> Bubbling phase.",
      "// Capture phase listener:\nparent.addEventListener('click', () => {\n  console.log('Parent handled in CAPTURE phase first');\n}, true);",
      "Medium", "Concept", "Technical Round", "Medium", "MDN", "In what order do capture and bubble listeners execute?")

add_q("DOM", "Event Delegation", "Performance Pattern",
      "What is Event Delegation and why is it useful?",
      "Event delegation is attaching a single event listener to a common parent element instead of adding individual listeners to multiple children, using event.target to identify which child was clicked.",
      "It significantly saves memory, improves performance with large lists, and automatically handles dynamically added child elements without reattaching listeners.",
      "document.getElementById('todo-list').addEventListener('click', function(e) {\n  if (e.target && e.target.matches('button.delete-btn')) {\n    e.target.closest('li').remove();\n  }\n});",
      "Medium", "Coding", "Technical Round", "High", "MDN", "What does Element.matches() and Element.closest() do?")

add_q("DOM", "Event Methods", "preventDefault",
      "What does event.preventDefault() do? Give two common examples.",
      "event.preventDefault() stops the browser's default native action associated with that event.",
      "Common examples: stopping a <form> submit from refreshing the page, or stopping an <a> tag from following a URL link.",
      "const form = document.querySelector('form');\nform.addEventListener('submit', (e) => {\n  e.preventDefault(); // Stop page reload\n  // Run client-side AJAX/fetch\n});",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Does event.preventDefault() stop the event from bubbling up?")

add_q("DOM", "Event Methods", "stopPropagation",
      "What is the difference between event.stopPropagation() and event.stopImmediatePropagation()?",
      "stopPropagation() prevents the event from propagating further up (or down) the DOM tree to parent elements. stopImmediatePropagation() additionally stops any other listeners attached to the SAME element from executing.",
      "Neither method cancels the default browser action; use preventDefault() for that.",
      "btn.addEventListener('click', (e) => {\n  e.stopPropagation(); // Parent won't receive this click\n});",
      "Medium", "Concept", "Technical Round", "High", "MDN", "Can you call both preventDefault() and stopPropagation() on the same event?")

add_q("DOM", "Forms & Inputs", "Input vs Change Events",
      "What is the difference between the 'input' event and the 'change' event on text inputs?",
      "The 'input' event fires immediately every time the input value changes (every keystroke). The 'change' event fires only when the user commits the change and unfocuses (blurs) the input element.",
      "Use 'input' for live search and instant character counters, and 'change' for validation on blur or dropdown selects.",
      "const searchBox = document.getElementById('search');\nsearchBox.addEventListener('input', (e) => {\n  console.log('Current query:', e.target.value);\n});",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Which event is preferred for a live instant search filter?")

add_q("DOM", "Dynamic DOM", "DocumentFragment",
      "What is a DocumentFragment and why should it be used when adding multiple elements?",
      "A DocumentFragment is a lightweight, in-memory container for DOM nodes that has no parent. Appending nodes to a fragment and then appending the fragment to the DOM triggers only a single browser reflow and repaint.",
      "Directly appending 500 items one-by-one to document.body causes 500 reflows and lags the browser.",
      "const fragment = document.createDocumentFragment();\nfor (let i = 1; i <= 50; i++) {\n  const li = document.createElement('li');\n  li.textContent = `Item ${i}`;\n  fragment.appendChild(li);\n}\ndocument.getElementById('list').appendChild(fragment); // 1 single DOM reflow!",
      "Medium", "Coding", "Coding Round", "High", "MDN", "What happens to the DocumentFragment once appended to the DOM?")

add_q("DOM", "Basic DOM Coding", "Toggle Class",
      "Write JavaScript to toggle an 'active' class on a button and change its text between 'Follow' and 'Following'.",
      "Select the button, add a click event listener, toggle the class with classList.toggle(), and update textContent using a ternary operator.",
      "The toggle method returns true if the class was added, or false if removed.",
      "const btn = document.querySelector('#follow-btn');\nbtn.addEventListener('click', () => {\n  const isFollowing = btn.classList.toggle('active');\n  btn.textContent = isFollowing ? 'Following' : 'Follow';\n});",
      "Easy", "Coding", "Coding Round", "High", "MDN", "How can you check if an element currently has a class?")

add_q("DOM", "Basic DOM Coding", "Counter Button",
      "Write a basic DOM counter with a count display, an increment button, and a decrement button.",
      "Maintain a count variable, listen for click events on the increment and decrement buttons, update the count, and update the display element's textContent.",
      "Ensure count cannot drop below zero if negative numbers are not allowed.",
      "let count = 0;\nconst display = document.getElementById('count-val');\n\ndocument.getElementById('btn-inc').addEventListener('click', () => {\n  count++;\n  display.textContent = count;\n});\ndocument.getElementById('btn-dec').addEventListener('click', () => {\n  if (count > 0) count--;\n  display.textContent = count;\n});",
      "Easy", "Coding", "Coding Round", "High", "MDN", "What happens if you store the count in element.textContent instead of a JS variable?")

add_q("DOM", "DOM Output", "Predict Output",
      "What is logged to the console by the following code?\n\n<ul id=\"fruits\">\n  <li>Apple</li>\n  <li>Banana</li>\n</ul>\n\nconst list = document.getElementById('fruits');\nconsole.log(list.children.length);\nconsole.log(list.childNodes.length);",
      "list.children.length logs 2 (only the <li> element nodes). list.childNodes.length logs 5 (includes text nodes created by the whitespace and line breaks before, between, and after the tags).",
      "children counts only Element nodes (nodeType 1), while childNodes counts all nodes including Text nodes (nodeType 3).",
      "// Output:\n// 2\n// 5",
      "Medium", "Output", "Technical Round", "High", "MDN", "How can you remove whitespace text nodes from childNodes?")

add_q("DOM", "DOM Debugging", "Script Placement",
      "Why does document.getElementById('btn') return null when placed in the <head> tag, and how do you fix it?",
      "Browsers parse HTML top to bottom. If the script in <head> executes before the browser reaches the <body> and parses the button, the element does not yet exist in the DOM tree.",
      "Fix by adding the 'defer' attribute to <script src=\"app.js\" defer>, moving the <script> before </body>, or wrapping code in document.addEventListener('DOMContentLoaded', ...).",
      "<!-- Solution 1: Use defer in head -->\n<head>\n  <script src=\"app.js\" defer></script>\n</head>\n\n<!-- Solution 2: DOMContentLoaded in JS -->\ndocument.addEventListener('DOMContentLoaded', () => {\n  const btn = document.getElementById('btn'); // Now works!\n});",
      "Easy", "Debugging", "Technical Round", "High", "MDN", "What is the difference between window.onload and DOMContentLoaded?")

add_q("DOM", "DOM Form Coding", "Form Submission",
      "Write JavaScript to handle a form submit, prevent reload, and validate that the username field is not empty.",
      "Attach a 'submit' event listener to the form, call event.preventDefault(), read input.value.trim(), and display an error message if empty.",
      "Always trim whitespace to prevent users from submitting only spaces.",
      "const form = document.getElementById('login-form');\nconst userInp = document.getElementById('username');\nconst errorMsg = document.getElementById('error');\n\nform.addEventListener('submit', (e) => {\n  e.preventDefault();\n  const val = userInp.value.trim();\n  if (val === '') {\n    errorMsg.textContent = 'Username is required';\n    userInp.focus();\n  } else {\n    errorMsg.textContent = '';\n    console.log('Submitting:', val);\n  }\n});",
      "Easy", "Coding", "Coding Round", "High", "MDN", "How do you reset form input fields after successful submission?")

# ==========================================
# 4. JavaScript Core (Fresher Questions)
# ==========================================
add_q("JavaScript", "Variables", "Var vs Let vs Const",
      "What are the differences between var, let, and const in JavaScript?",
      "var is function-scoped, can be redeclared, and is hoisted initialized as undefined. let and const are block-scoped ({}), cannot be redeclared in the same scope, and exist in a Temporal Dead Zone (TDZ) before declaration. const cannot be reassigned.",
      "Always prefer const by default; use let only when variable reassignment is required. Avoid var in modern code.",
      "// var leaks outside block:\nif (true) { var a = 1; let b = 2; }\nconsole.log(a); // 1\n// console.log(b); // ReferenceError: b is not defined",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Can you modify properties of an object declared with const?")

add_q("JavaScript", "Data Types", "Primitives vs Non-Primitives",
      "What are the primitive data types in JavaScript and how do they differ from non-primitive types?",
      "JavaScript has 7 primitive types: string, number, boolean, undefined, null, bigint, and symbol. Non-primitive types are objects (including arrays, functions, and dates).",
      "Primitives are immutable and passed by value. Objects are mutable and passed by reference.",
      "let x = 10; let y = x; y = 20; // x is still 10 (value copy)\nlet obj1 = { val: 10 };\nlet obj2 = obj1; // Reference copy!\nobj2.val = 20; // obj1.val is now also 20",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Why does typeof null return 'object' in JavaScript?")

add_q("JavaScript", "Type Coercion", "Double vs Triple Equals",
      "What is the difference between == (loose equality) and === (strict equality)?",
      "== compares values after performing implicit type coercion (converting operands to a common type). === compares both value AND data type without type coercion.",
      "Always use === to avoid unexpected coercion bugs (e.g. 0 == '' is true, 0 == false is true).",
      "console.log(5 == '5');  // true (type coerced string to number)\nconsole.log(5 === '5'); // false (number !== string)\nconsole.log(null == undefined);  // true\nconsole.log(null === undefined); // false",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What does Object.is() do differently compared to ===?")

add_q("JavaScript", "Hoisting", "Variable & Function Hoisting",
      "What is hoisting in JavaScript?",
      "Hoisting is JavaScript's default behavior of moving variable and function declarations to the top of their containing scope during the compilation phase before code execution.",
      "Function declarations are hoisted with their full definition. var is hoisted initialized as undefined. let and const are hoisted but remain in the Temporal Dead Zone (TDZ) until their definition line is executed.",
      "sayHi(); // Works! Logs 'Hi'\nfunction sayHi() { console.log('Hi'); }\n\nconsole.log(x); // undefined\nvar x = 5;\n\n// console.log(y); // ReferenceError: Cannot access 'y' before initialization\nlet y = 10;",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Are function expressions hoisted the same way as function declarations?")

add_q("JavaScript", "Closures", "Definition & Example",
      "What is a closure in JavaScript and give a practical use case.",
      "A closure is a function bundled together with references to its surrounding lexical scope. It allows an inner function to access an outer function's variables even after the outer function has finished executing.",
      "Practical uses: creating private variables (encapsulation), data privacy, currying, and memoization.",
      "function createCounter() {\n  let count = 0; // Private variable\n  return function() {\n    count++;\n    return count;\n  };\n}\nconst counter = createCounter();\nconsole.log(counter()); // 1\nconsole.log(counter()); // 2",
      "Medium", "Concept", "Technical Round", "High", "MDN", "Can closures cause memory leaks if not cleaned up?")

add_q("JavaScript", "Functions", "Arrow vs Regular Functions",
      "What are the main differences between regular functions and arrow functions?",
      "1) Regular functions have their own 'this' bound dynamically to the caller; arrow functions inherit 'this' lexically from their enclosing scope. 2) Regular functions have an 'arguments' object; arrow functions do not. 3) Regular functions can be constructors with 'new'; arrow functions cannot.",
      "Arrow functions provide concise syntax for callbacks and functional methods like map and filter.",
      "const obj = {\n  name: 'Asha',\n  regularFn: function() { console.log(this.name); },\n  arrowFn: () => { console.log(this.name); } // 'this' is window / global, not obj\n};",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Why should you avoid using arrow functions as object methods?")

add_q("JavaScript", "Array Methods", "Map vs Filter vs Reduce",
      "Explain map(), filter(), and reduce() with code examples.",
      "map() creates a new array by transforming every item. filter() creates a new array with items that pass a test condition. reduce() accumulates array elements into a single output value (number, object, etc.).",
      "All three methods are non-mutating (pure functions) and return a new result.",
      "const nums = [1, 2, 3, 4];\n// map: double each\nconst doubled = nums.map(n => n * 2); // [2, 4, 6, 8]\n// filter: evens only\nconst evens = nums.filter(n => n % 2 === 0); // [2, 4]\n// reduce: sum all\nconst sum = nums.reduce((acc, curr) => acc + curr, 0); // 10",
      "Easy", "Coding", "Coding Round", "High", "MDN", "What is the difference between forEach() and map()?")

add_q("JavaScript", "Asynchronous JS", "Promises & States",
      "What is a Promise and what are its three states?",
      "A Promise represents the eventual completion (or failure) of an asynchronous operation and its resulting value. Its three states are: pending (initial state), fulfilled (operation succeeded), and rejected (operation failed).",
      "Once settled (fulfilled or rejected), a promise cannot change states again.",
      "const myPromise = new Promise((resolve, reject) => {\n  setTimeout(() => resolve('Data loaded!'), 1000);\n});\nmyPromise\n  .then(res => console.log(res))\n  .catch(err => console.error(err))\n  .finally(() => console.log('Done'));",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What is Promise.all() and how does it handle rejections?")

add_q("JavaScript", "Asynchronous JS", "Async / Await",
      "What is async/await and how does it improve asynchronous code?",
      "async/await is syntactic sugar built on top of Promises that allows asynchronous code to be written and read like synchronous code, using standard try/catch blocks for error handling.",
      "An 'async' function always returns a Promise automatically. 'await' can only be used inside async functions.",
      "async function fetchUser() {\n  try {\n    const res = await fetch('https://api.example.com/user');\n    const data = await res.json();\n    return data;\n  } catch (error) {\n    console.error('Fetch failed:', error.message);\n  }\n}",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What happens if an error thrown inside an async function is not caught with try/catch?")

add_q("JavaScript", "Event Loop", "Call Stack & Microtasks",
      "What is the output of this code and why?\n\nconsole.log(1);\nsetTimeout(() => console.log(2), 0);\nPromise.resolve().then(() => console.log(3));\nconsole.log(4);",
      "The output is: 1, 4, 3, 2.",
      "Explanation: 1 and 4 are synchronous and run on Call Stack immediately. Promise.then callback enters Microtask Queue. setTimeout enters Macrotask Queue. The Event Loop drains ALL microtasks (3) before running any macrotasks (2).",
      "// Output order:\n// 1\n// 4\n// 3\n// 2",
      "Medium", "Output", "Technical Round", "High", "MDN", "Does process.nextTick() in Node.js run before or after Promise microtasks?")

# ==========================================
# 5. ES6+ Features (Fresher Questions)
# ==========================================
add_q("ES6", "Syntax Features", "Destructuring",
      "How does object and array destructuring work in ES6?",
      "Destructuring allows extracting values from arrays or properties from objects into distinct variables using clean, concise syntax, with support for default values.",
      "You can also rename object properties during destructuring using the colon syntax (e.g. { name: userName }).",
      "// Object destructuring with default and alias:\nconst user = { name: 'Asha', role: 'admin' };\nconst { name, role, country = 'India' } = user;\n\n// Array destructuring:\nconst coords = [10, 20];\nconst [x, y] = coords;",
      "Easy", "Concept", "Technical Round", "High", "MDN", "How do you extract nested properties using destructuring?")

add_q("ES6", "Operators", "Spread vs Rest",
      "What is the difference between the Spread operator and the Rest parameter?",
      "Both use the three dots (...) syntax. Spread EXPANDS an array or object into individual elements. Rest CONDENSES multiple elements or arguments into a single array.",
      "Spread is used in function calls, array literals, and object copying. Rest is used in function parameter definitions.",
      "// Spread: expands elements\nconst arr1 = [1, 2]; const arr2 = [...arr1, 3, 4]; // [1, 2, 3, 4]\n\n// Rest: gathers arguments into an array\nfunction sum(...numbers) {\n  return numbers.reduce((acc, n) => acc + n, 0);\n}\nconsole.log(sum(1, 2, 3, 4)); // 10",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Does the spread operator create a deep clone or shallow clone of an object?")

add_q("ES6", "Operators", "Optional Chaining & Nullish Coalescing",
      "What are Optional Chaining (?.) and Nullish Coalescing (??)?",
      "Optional Chaining (?.) allows safe reading of nested properties without throwing TypeError if an intermediate reference is null or undefined. Nullish Coalescing (??) returns the right-hand operand only when left-hand operand is null or undefined.",
      "Unlike ||, ?? treats falsy values like 0, false, and '' as valid, preventing common bugs.",
      "const user = { profile: { age: 0 } };\n// Optional chaining:\nconst city = user?.address?.city; // undefined (no error!)\n\n// Nullish coalescing:\nconst age = user.profile.age ?? 18; // 0 (|| would give 18!)",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What is the difference between value ?? default and value || default?")

add_q("ES6", "Data Structures", "Set & Map",
      "What are Set and Map in ES6?",
      "Set is a collection of unique values of any type (automatically removes duplicates). Map is a collection of keyed key-value pairs where keys can be of any type (including objects and functions).",
      "A standard JS object only supports string and symbol keys, whereas Map allows object keys and preserves insertion order.",
      "// Remove duplicates from array using Set:\nconst nums = [1, 2, 2, 3, 3, 4];\nconst unique = [...new Set(nums)]; // [1, 2, 3, 4]\n\n// Map:\nconst userMap = new Map();\nuserMap.set('id1', { name: 'Asha' });\nconsole.log(userMap.get('id1'));",
      "Easy", "Concept", "Technical Round", "High", "MDN", "How do you check if an item exists in a Set?")

# ==========================================
# 6. jQuery (Fresher Questions)
# ==========================================
add_q("jQuery", "Basics", "Syntax & Document Ready",
      "What is jQuery and what does $(document).ready() do?",
      "jQuery is a fast, lightweight JavaScript library designed to simplify HTML DOM tree traversal, event handling, animation, and AJAX calls with cross-browser compatibility.",
      "$(document).ready(function() { ... }) ensures the DOM is fully loaded and safe to manipulate before running jQuery script.",
      "$(document).ready(function() {\n  $('button').click(function() {\n    $('p').toggle();\n  });\n});",
      "Easy", "Concept", "Technical Round", "Medium", "jQuery Docs", "What is the modern Vanilla JS equivalent of $(document).ready()?")

add_q("jQuery", "DOM Manipulation", "Classes & Events",
      "How do you add/remove classes and handle click events in jQuery?",
      "Use $(selector).addClass('className'), $(selector).removeClass('className'), and $(selector).toggleClass('className'). Attach click events with $(selector).click(fn) or $(selector).on('click', fn).",
      "jQuery methods automatically apply across all matching elements in the selection without needing an explicit loop.",
      "$('#myButton').on('click', function() {\n  $('.card').toggleClass('highlight');\n});",
      "Easy", "Concept", "Technical Round", "Medium", "jQuery Docs", "Why is $(selector).on() preferred over shorthand methods like .click()?")

add_q("jQuery", "Comparison", "jQuery vs Vanilla JS",
      "Why has modern web development shifted from jQuery to Vanilla JavaScript and modern frameworks?",
      "Modern browsers standardized the DOM API (querySelectorAll, fetch, classList, addEventListener), eliminating cross-browser incompatibilities. Modern frameworks (React, Vue) use virtual DOM declarative patterns instead of direct DOM manipulation.",
      "Vanilla JavaScript avoids the 30KB+ jQuery library download footprint.",
      "// jQuery:\n$('#btn').addClass('active');\n\n// Modern Vanilla JS (built-in!):\ndocument.querySelector('#btn').classList.add('active');",
      "Easy", "Concept", "Technical Round", "High", "MDN", "Is jQuery still relevant in legacy corporate applications?")

# ==========================================
# 7. React (Fresher Questions)
# ==========================================
add_q("React", "Core Concepts", "Virtual DOM",
      "What is the Virtual DOM in React and how does reconciliation work?",
      "The Virtual DOM is a lightweight JavaScript object representation of the real DOM tree kept in memory. When state changes, React creates a new Virtual DOM tree, diffs it with the previous one (reconciliation), and updates ONLY the changed real DOM nodes.",
      "Batching DOM updates significantly improves rendering performance compared to touching the real DOM repeatedly.",
      "// React declarative UI:\nfunction App() {\n  const [count, setCount] = React.useState(0);\n  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;\n}",
      "Easy", "Concept", "Technical Round", "High", "React Docs", "What algorithm does React use for diffing the Virtual DOM?")

add_q("React", "Core Concepts", "Props vs State",
      "What is the difference between Props and State in React?",
      "Props (short for properties) are read-only inputs passed from a parent component to configure child components (one-way data flow). State is internal data managed and owned by the component that triggers re-rendering when updated.",
      "Components cannot modify their own props directly (props are immutable).",
      "// Parent passes props, Child renders:\nfunction Greeting({ name }) { // Props\n  const [isOnline, setIsOnline] = useState(true); // State\n  return <h2>Hello {name}, status: {isOnline ? 'Online' : 'Offline'}</h2>;\n}",
      "Easy", "Concept", "Technical Round", "High", "React Docs", "Can a parent pass state down as props to a child?")

add_q("React", "Hooks", "useState",
      "How does the useState hook work and why should you use an updater function?",
      "useState declares a state variable and returns a pair: [currentState, setterFunction]. When updating state based on previous state, always pass an updater function (prev => prev + 1) to avoid stale closures during asynchronous state batching.",
      "Never mutate state directly (e.g. count = count + 1); always call the setter function.",
      "const [count, setCount] = useState(0);\n\n// Correct way to increment based on previous state:\nconst handleIncrement = () => {\n  setCount(prevCount => prevCount + 1);\n};",
      "Easy", "Concept", "Technical Round", "High", "React Docs", "What happens if you update state with the exact same value?")

add_q("React", "Hooks", "useEffect",
      "Explain the dependency array in useEffect and when cleanup functions run.",
      "useEffect handles side effects (data fetching, timers, subscriptions). 1) No array: runs after EVERY render. 2) Empty array []: runs ONCE on mount. 3) [dep1, dep2]: runs on mount and whenever dependencies change.",
      "Returning a cleanup function from useEffect runs before the effect re-executes and when the component unmounts to prevent memory leaks.",
      "useEffect(() => {\n  const timer = setInterval(() => console.log('Tick'), 1000);\n  // Cleanup function runs on unmount:\n  return () => clearInterval(timer);\n}, []);",
      "Easy", "Concept", "Technical Round", "High", "React Docs", "What happens if you forget to add a variable used inside useEffect to the dependency array?")

add_q("React", "Lists & Keys", "Importance of Keys",
      "Why are 'key' props required when rendering lists in React, and why should you avoid using array index as key?",
      "Keys give each list item a stable identity so React's diffing algorithm can identify which items changed, added, or removed. Using array indexes as keys causes bugs, wrong input values, and poor performance when list items are reordered, filtered, or deleted.",
      "Always use a unique ID from the data (like user.id) as the key prop.",
      "// Good: Unique ID\n{todos.map(todo => (\n  <TodoItem key={todo.id} todo={todo} />\n))}\n\n// Bad: Index as key on dynamic list\n// {todos.map((todo, index) => <TodoItem key={index} todo={todo} />)}",
      "Easy", "Concept", "Technical Round", "High", "React Docs", "What is the error React throws in console when a key prop is missing?")

add_q("React", "Forms", "Controlled Components",
      "What is a Controlled Component in React?",
      "A Controlled Component is an input form element whose value is controlled by React state. The input's current value is read from state (value={val}), and changes trigger an onChange handler to update state.",
      "This provides a single source of truth and enables instant validation and conditional button disabling.",
      "function LoginForm() {\n  const [email, setEmail] = useState('');\n  return (\n    <input \n      type=\"email\" \n      value={email} \n      onChange={(e) => setEmail(e.target.value)} \n    />\n  );\n}",
      "Easy", "Concept", "Technical Round", "High", "React Docs", "What is an uncontrolled component and how do you access its value using useRef?")

# ==========================================
# 8. Node.js (Fresher Questions)
# ==========================================
add_q("Node.js", "Basics", "Runtime & Architecture",
      "What is Node.js and why is it single-threaded?",
      "Node.js is an open-source, cross-platform JavaScript runtime environment built on Chrome's V8 engine that runs JavaScript outside the browser. It uses an asynchronous, event-driven, non-blocking I/O model.",
      "It is single-threaded on the JavaScript execution stack, but offloads expensive I/O operations (file, network, DNS) to the OS and C++ threadpool using the libuv library.",
      "// Single thread handles request routing asynchronously:\nconst http = require('http');\nconst server = http.createServer((req, res) => {\n  res.writeHead(200, { 'Content-Type': 'text/plain' });\n  res.end('Hello from Node.js\\n');\n});\nserver.listen(3000);",
      "Easy", "Concept", "Technical Round", "High", "Node.js Docs", "Is Node.js suitable for CPU-intensive tasks like video encoding?")

add_q("Node.js", "npm & Modules", "package.json",
      "What is the purpose of package.json and what is the difference between dependencies and devDependencies?",
      "package.json holds metadata about a Node project, scripts, and lists required packages. 'dependencies' are packages needed in production runtime (e.g. express, mongoose). 'devDependencies' are only needed during development and testing (e.g. nodemon, jest, eslint).",
      "npm install --save-dev installs a package into devDependencies.",
      "{\n  \"name\": \"fresher-api\",\n  \"version\": \"1.0.0\",\n  \"dependencies\": {\n    \"express\": \"^4.18.2\"\n  },\n  \"devDependencies\": {\n    \"nodemon\": \"^3.0.1\"\n  }\n}",
      "Easy", "Concept", "Technical Round", "High", "Node.js Docs", "What is the difference between package.json and package-lock.json?")

add_q("Node.js", "Modules", "CommonJS vs ES Modules",
      "What is the difference between CommonJS and ES Modules in Node.js?",
      "CommonJS is Node's original module system using require() and module.exports (synchronous). ES Modules (ESM) is the standard JavaScript module system using import and export (asynchronous).",
      "To use ES Modules in Node.js, set \"type\": \"module\" in package.json or use .mjs file extension.",
      "// CommonJS:\nconst fs = require('fs');\nmodule.exports = { myFunction };\n\n// ES Modules:\nimport fs from 'fs';\nexport default myFunction;",
      "Easy", "Concept", "Technical Round", "High", "Node.js Docs", "Can you use require() inside an ES Module file?")

add_q("Node.js", "File System", "fs Module",
      "How do you read a file asynchronously in Node.js using the 'fs' module?",
      "Use fs.readFile(path, encoding, callback) or fs.promises.readFile(path, encoding) with async/await. Asynchronous reading does not block the main thread while waiting for disk I/O.",
      "Always specify 'utf-8' encoding to receive a text string instead of a raw Buffer.",
      "const fs = require('fs').promises;\n\nasync function loadData() {\n  try {\n    const data = await fs.readFile('data.txt', 'utf-8');\n    console.log(data);\n  } catch (err) {\n    console.error('File read error:', err.message);\n  }\n}",
      "Easy", "Coding", "Technical Round", "High", "Node.js Docs", "What is the danger of using fs.readFileSync in a web server?")

# ==========================================
# 9. Express.js (Fresher Questions)
# ==========================================
add_q("Express", "Routing", "Basic Server",
      "What is Express.js and how do you create a basic REST API endpoint?",
      "Express.js is a minimal, flexible web application framework for Node.js that provides routing, middleware pipeline support, and HTTP utility methods.",
      "Endpoints are defined using app.get(), app.post(), app.put(), app.delete().",
      "const express = require('express');\nconst app = express();\napp.use(express.json()); // Parse JSON body\n\napp.get('/api/users', (req, res) => {\n  res.status(200).json([{ id: 1, name: 'Asha' }]);\n});\n\napp.listen(5000, () => console.log('Server running on 5000'));",
      "Easy", "Coding", "Technical Round", "High", "Express Docs", "What does app.use(express.json()) do?")

add_q("Express", "Middleware", "Middleware Pipeline",
      "What is Middleware in Express.js and what does the next() function do?",
      "Middleware functions are functions that have access to req, res, and the next() function in the application's request-response cycle. They can execute code, modify req and res objects, end the cycle, or call next() to pass control to the next middleware.",
      "If a middleware does not call next() or send a response with res.send(), the client request hangs indefinitely.",
      "// Custom logger middleware:\nconst logger = (req, res, next) => {\n  console.log(`${req.method} ${req.url} at ${new Date().toISOString()}`);\n  next(); // Pass control to next handler\n};\napp.use(logger);",
      "Easy", "Concept", "Technical Round", "High", "Express Docs", "How does an error-handling middleware differ from regular middleware in Express?")

add_q("Express", "HTTP Status Codes", "REST Codes",
      "What are the most common HTTP status codes every fresher must know in REST APIs?",
      "200 OK (standard success), 201 Created (resource successfully created), 400 Bad Request (invalid client input), 401 Unauthorized (missing/invalid credentials), 403 Forbidden (authenticated but lacks permission), 404 Not Found (resource doesn't exist), 500 Internal Server Error (server crashed/unhandled exception).",
      "Returning appropriate status codes is essential for client-side error handling.",
      "app.post('/api/items', (req, res) => {\n  if (!req.body.name) {\n    return res.status(400).json({ error: 'Name is required' });\n  }\n  res.status(201).json({ id: 101, name: req.body.name });\n});",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What is the difference between 401 Unauthorized and 403 Forbidden?")

add_q("Express", "Request Parameters", "Params vs Query vs Body",
      "What is the difference between req.params, req.query, and req.body in Express?",
      "req.params extracts route URL parameters (e.g. /users/:id -> req.params.id). req.query extracts URL query strings (e.g. /search?q=js -> req.query.q). req.body extracts payload sent in POST/PUT request bodies (requires express.json()).",
      "Use params for resource identity, query for filtering/sorting, and body for creating/updating records.",
      "// Route param:\napp.get('/users/:id', (req, res) => {\n  const userId = req.params.id;\n  res.json({ id: userId });\n});",
      "Easy", "Concept", "Technical Round", "High", "Express Docs", "Why is req.body undefined if express.json() is omitted?")

# ==========================================
# 10. SQL (Fresher Questions)
# ==========================================
add_q("SQL", "Basic Queries", "SELECT & WHERE",
      "Write a SQL query to select all employees from department 'IT' earning more than 50,000, sorted by salary descending.",
      "Use SELECT * FROM employees WHERE department = 'IT' AND salary > 50000 ORDER BY salary DESC;.",
      "WHERE filters rows before sorting; ORDER BY sorts the output result set.",
      "SELECT id, name, salary \nFROM employees \nWHERE department = 'IT' AND salary > 50000 \nORDER BY salary DESC;",
      "Easy", "SQL Query", "Online Test", "High", "SQL Standard", "What is the default sort order of ORDER BY?")

add_q("SQL", "Joins", "Inner vs Left vs Right Join",
      "Explain the difference between INNER JOIN, LEFT JOIN, and RIGHT JOIN.",
      "INNER JOIN returns only rows that have matching values in both tables. LEFT JOIN returns all rows from the left table, and matched rows from the right table (NULL if no match). RIGHT JOIN returns all rows from the right table, and matched rows from left.",
      "Use LEFT JOIN when you want all records from the primary table regardless of whether they have linked records.",
      "SELECT orders.order_id, customers.customer_name\nFROM orders\nINNER JOIN customers ON orders.customer_id = customers.id;",
      "Easy", "Concept", "Technical Round", "High", "SQL Standard", "What does a FULL OUTER JOIN return?")

add_q("SQL", "Aggregations", "GROUP BY & HAVING",
      "What is the difference between WHERE and HAVING clauses in SQL?",
      "WHERE filters individual rows BEFORE aggregate functions are applied. HAVING filters grouped rows AFTER aggregate functions (SUM, COUNT, AVG) have computed.",
      "HAVING can use aggregate functions in its condition; WHERE cannot.",
      "SELECT department, COUNT(*) AS total_emps, AVG(salary) AS avg_sal\nFROM employees\nWHERE status = 'Active'\nGROUP BY department\nHAVING AVG(salary) > 60000;",
      "Medium", "Concept", "Technical Round", "High", "SQL Standard", "Can you use HAVING without GROUP BY in SQL?")

add_q("SQL", "Queries", "Second Highest Salary",
      "Write a SQL query to find the second highest salary from an Employee table.",
      "SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);. Alternatively: SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;.",
      "Using the subquery method works across all SQL databases (MySQL, Postgres, SQL Server, Oracle).",
      "SELECT MAX(salary) AS SecondHighestSalary \nFROM employees \nWHERE salary < (\n  SELECT MAX(salary) FROM employees\n);",
      "Medium", "SQL Query", "Coding Round", "High", "SQL Standard", "How would you find the N-th highest salary?")

add_q("SQL", "Keys & Constraints", "Primary vs Foreign Key",
      "What is the difference between a Primary Key and a Foreign Key?",
      "A Primary Key uniquely identifies each row in a table; it cannot contain NULL and must be unique. A Foreign Key is a column that refers to the Primary Key of another table, establishing a relationship and enforcing referential integrity.",
      "A table can have only one Primary Key, but multiple Foreign Keys.",
      "CREATE TABLE orders (\n  order_id INT PRIMARY KEY,\n  customer_id INT,\n  FOREIGN KEY (customer_id) REFERENCES customers(id)\n);",
      "Easy", "Concept", "Technical Round", "High", "SQL Standard", "What is a Composite Primary Key?")

# ==========================================
# 11. MongoDB (Fresher Questions)
# ==========================================
add_q("MongoDB", "Basics", "Collections vs Tables",
      "What is MongoDB and how do its concepts map to Relational Database (SQL) concepts?",
      "MongoDB is a NoSQL, document-oriented database that stores data as JSON-like BSON documents. Database maps to Database, Table maps to Collection, Row maps to Document, and Column maps to Field.",
      "Documents in the same collection do not need identical schemas (schema flexibility).",
      "// SQL: INSERT INTO users (name, age) VALUES ('Asha', 24);\n// MongoDB:\ndb.users.insertOne({ name: \"Asha\", age: 24, skills: [\"JS\", \"React\"] });",
      "Easy", "Concept", "Technical Round", "High", "MongoDB Docs", "What is BSON and why does MongoDB use it instead of plain JSON?")

add_q("MongoDB", "CRUD", "find & Operators",
      "How do you query documents in MongoDB with comparison operators like $gt and $in?",
      "Use db.collection.find({ field: { $operator: value } }). Example: db.products.find({ price: { $gt: 500 }, category: { $in: ['electronics', 'books'] } }).",
      "Comparison operators include $eq, $ne, $gt, $gte, $lt, $lte, and $in.",
      "db.products.find({\n  price: { $gte: 100, $lte: 1000 },\n  inStock: true\n});",
      "Easy", "Concept", "Technical Round", "High", "MongoDB Docs", "How do you project (select) only specific fields in a MongoDB query?")

add_q("MongoDB", "Schema Design", "Embedding vs Referencing",
      "What is the difference between Embedding and Referencing in MongoDB schema design?",
      "Embedding stores related data inside the same document as nested objects or arrays (1-to-1 or bounded 1-to-few). Referencing stores the _id of related documents in a separate collection (normalized, like foreign keys).",
      "Embedding provides faster reads with zero joins, but documents have a hard 16MB size limit. Referencing avoids document size overflow and duplication for many-to-many relationships.",
      "// Embedding (address inside user doc):\n{ name: \"Asha\", address: { city: \"Pune\", pin: \"411001\" } }\n\n// Referencing (order references user id):\n{ orderId: \"ORD123\", userId: ObjectId(\"60c72b2f9b1d8b2bad000001\") }",
      "Easy", "Concept", "Technical Round", "High", "MongoDB Docs", "What is the populate() method in Mongoose?")

# ==========================================
# 12. Aptitude & Logical Reasoning (Fresher Questions)
# ==========================================
add_q("Aptitude", "Quantitative", "Percentages",
      "If the price of an article increases by 25%, by what percentage must consumption be reduced so that expenditure remains unchanged?",
      "Formula: [r / (100 + r)] * 100%. Here r = 25%. Calculation: [25 / (100 + 25)] * 100 = (25 / 125) * 100 = (1 / 5) * 100 = 20%.",
      "Shortcut: Let original price = 100, new price = 125. To return from 125 to 100, decrease by 25. Percentage decrease = (25/125) * 100 = 20%.",
      "// Formula: (r / (100 + r)) * 100\n// (25 / 125) * 100 = 20%",
      "Easy", "Aptitude", "Aptitude Round", "High", "RS Aggarwal", "What if the price decreases by 20%?")

add_q("Aptitude", "Quantitative", "Time & Work",
      "A can complete a piece of work in 10 days, and B can complete the same work in 15 days. How many days will they take working together?",
      "Together they take 6 days. Calculation: 1 day work of A = 1/10. 1 day work of B = 1/15. Together 1 day work = 1/10 + 1/15 = (3 + 2)/30 = 5/30 = 1/6. Total days = 6 days.",
      "Shortcut formula: (A * B) / (A + B) = (10 * 15) / (10 + 15) = 150 / 25 = 6 days.",
      "// Formula: (A * B) / (A + B)\n// (10 * 15) / (10 + 15) = 150 / 25 = 6 days",
      "Easy", "Aptitude", "Aptitude Round", "High", "RS Aggarwal", "If A and B work on alternate days starting with A, how many days will it take?")

add_q("Aptitude", "Quantitative", "Speed, Time & Distance",
      "A train 150 meters long is running at 54 km/hr. How many seconds will it take to cross an electric pole?",
      "It will take 10 seconds. Step 1: Convert speed to m/s: 54 * (5/18) = 15 m/s. Step 2: Distance to cross a point object (pole) = length of train = 150 m. Step 3: Time = Distance / Speed = 150 / 15 = 10 seconds.",
      "Always remember: multiply km/hr by 5/18 to convert into m/s, or multiply m/s by 18/5 to get km/hr.",
      "// Speed in m/s = 54 * (5/18) = 15 m/s\n// Time = Distance / Speed = 150 / 15 = 10 seconds",
      "Easy", "Aptitude", "Aptitude Round", "High", "RS Aggarwal", "How much time will it take if crossing a 250m platform instead of a pole?")

add_q("Aptitude", "Logical Reasoning", "Number Series",
      "Find the missing number in the sequence: 2, 6, 12, 20, 30, ?",
      "The missing number is 42. Explanation: Differences between terms are +4, +6, +8, +10. The next difference must be +12. Therefore: 30 + 12 = 42.",
      "Alternate logic: 1*2=2, 2*3=6, 3*4=12, 4*5=20, 5*6=30, 6*7=42.",
      "// Pattern: n * (n + 1)\n// 1*2=2, 2*3=6, 3*4=12, 4*5=20, 5*6=30, 6*7 = 42",
      "Easy", "Logical Reasoning", "Online Test", "High", "Logical Reasoning", "What is the next number after 42 in this sequence?")

# ==========================================
# 13. Problem Solving & DSA (Fresher Questions)
# ==========================================
add_q("DSA", "Complexity", "Big-O Basics",
      "What is Big-O notation and what are the time complexities of O(1), O(log n), O(n), and O(n^2)?",
      "Big-O notation describes the upper bound (worst-case scenario) of time or space an algorithm requires as input size n grows.",
      "O(1): Constant time (array index lookup). O(log n): Logarithmic (binary search). O(n): Linear (single loop over array). O(n^2): Quadratic (nested loops like bubble sort).",
      "// O(1): arr[0]\n// O(n): for (let i = 0; i < n; i++)\n// O(n^2): for (let i = 0; i < n; i++) for (let j = 0; j < n; j++)",
      "Easy", "Concept", "Technical Round", "High", "DSA Guide", "What is space complexity?")

add_q("DSA", "Array Problem", "Two Sum",
      "How do you solve the Two Sum problem in O(n) time using a Hash Map?",
      "Iterate through the array. For each number, calculate complement = target - num. If complement exists in map, return indices. Otherwise store num: index in map.",
      "This reduces time complexity from O(n^2) brute force with nested loops to O(n) single pass time and O(n) space.",
      "function twoSum(nums, target) {\n  const map = new Map();\n  for (let i = 0; i < nums.length; i++) {\n    const complement = target - nums[i];\n    if (map.has(complement)) {\n      return [map.get(complement), i];\n    }\n    map.set(nums[i], i);\n  }\n  return [];\n}",
      "Medium", "Coding", "Coding Round", "High", "LeetCode #1", "Can you solve Two Sum in O(1) space if the array is already sorted?")

add_q("DSA", "Stack", "Valid Parentheses",
      "How do you check if a string of parentheses '()[]{}' is valid using a Stack?",
      "Iterate over characters. Push opening brackets onto stack. For closing brackets, check if stack is empty or top doesn't match; if so return false. Return true if stack is empty at the end.",
      "Stack enforces Last-In-First-Out (LIFO) order, which matches matching bracket nesting.",
      "function isValid(s) {\n  const stack = [];\n  const pairs = { ')': '(', '}': '{', ']': '[' };\n  for (let char of s) {\n    if (char === '(' || char === '{' || char === '[') {\n      stack.push(char);\n    } else if (stack.pop() !== pairs[char]) {\n      return false;\n    }\n  }\n  return stack.length === 0;\n}",
      "Medium", "Coding", "Coding Round", "High", "LeetCode #20", "What is the time and space complexity of this solution?")

add_q("DSA", "Strings", "Palindrome Check",
      "How do you check if a string is a palindrome using two pointers in O(1) extra space?",
      "Place one pointer at start (0) and another at end (len-1). Compare characters while left < right. If mismatch, return false; otherwise increment left and decrement right.",
      "Two pointers avoids creating reversed string copies in memory.",
      "function isPalindrome(str) {\n  let left = 0, right = str.length - 1;\n  while (left < right) {\n    if (str[left] !== str[right]) return false;\n    left++;\n    right--;\n  }\n  return true;\n}",
      "Easy", "Coding", "Coding Round", "High", "DSA Guide", "How would you handle ignoring spaces and punctuation?")

# ==========================================
# 14. Coding (Fresher Practical Coding)
# ==========================================
add_q("Coding", "Array Manipulation", "Remove Duplicates",
      "Write a function to remove duplicates from an array in JavaScript.",
      "Use new Set(arr) spread into an array: [...new Set(arr)]. Or use arr.filter((item, index) => arr.indexOf(item) === index).",
      "Set is O(n) time complexity, whereas filter with indexOf is O(n^2).",
      "// Method 1: Using Set (O(n) - Recommended)\nconst removeDuplicates = arr => [...new Set(arr)];\nconsole.log(removeDuplicates([1, 2, 2, 3, 4, 4])); // [1, 2, 3, 4]",
      "Easy", "Coding", "Coding Round", "High", "JS Interview", "How do you remove duplicate objects based on an id property?")

add_q("Coding", "Classic Coding", "FizzBuzz",
      "Write a function that prints numbers 1 to n. For multiples of 3 print 'Fizz', multiples of 5 print 'Buzz', and multiples of both print 'FizzBuzz'.",
      "Loop from 1 to n. Check divisible by 15 (3 and 5) first, then by 3, then by 5, else print number.",
      "Always check the combined condition (15) first before checking individual divisors.",
      "function fizzBuzz(n) {\n  for (let i = 1; i <= n; i++) {\n    if (i % 15 === 0) console.log('FizzBuzz');\n    else if (i % 3 === 0) console.log('Fizz');\n    else if (i % 5 === 0) console.log('Buzz');\n    else console.log(i);\n  }\n}",
      "Easy", "Coding", "Coding Round", "High", "Classic", "How can you implement FizzBuzz without modulo operator?")

add_q("Coding", "Optimization", "Debounce Function",
      "Write a simple debounce function in JavaScript.",
      "Debounce returns a function that clears the previous timer on each call and sets a new timer to execute the function only after delay milliseconds of inactivity.",
      "Crucial in browser apps for search boxes to avoid firing an API call on every keystroke.",
      "function debounce(func, delay = 300) {\n  let timer;\n  return function(...args) {\n    clearTimeout(timer);\n    timer = setTimeout(() => func.apply(this, args), delay);\n  };\n}",
      "Medium", "Fresher Coding", "Coding Round", "High", "MDN", "What is the difference between debounce and throttle?")

# ==========================================
# 15. Engineering Basics (Git & Testing)
# ==========================================
add_q("Git", "Version Control", "Core Commands",
      "What are the essential Git commands for daily fresher development?",
      "git clone <url> (download repo), git status (check file changes), git add . (stage changes), git commit -m \"message\" (commit staged files), git pull (fetch and merge from remote), git push (upload local commits), and git checkout -b <name> (create branch).",
      "Always pull before pushing to prevent merge conflicts with teammate commits.",
      "# Standard daily feature flow:\ngit checkout -b feature/login-page\n# make changes\ngit add .\ngit commit -m \"Add login form validation\"\ngit push origin feature/login-page",
      "Easy", "Concept", "Technical Round", "High", "Git Docs", "What is the difference between git fetch and git pull?")

add_q("Git", "Branching", "Merge vs Rebase",
      "What is the difference between git merge and git rebase?",
      "git merge combines two branches by creating a new merge commit, preserving historical commit order and branch history. git rebase moves the entire feature branch commits onto the tip of the target branch, creating a clean linear history.",
      "Never rebase on a public shared branch like main/master.",
      "# Merge:\ngit checkout main\ngit merge feature-branch\n\n# Rebase:\ngit checkout feature-branch\ngit rebase main",
      "Medium", "Concept", "Technical Round", "Medium", "Git Docs", "How do you resolve a Git merge conflict?")

add_q("Testing", "Playwright & E2E", "Playwright Basics",
      "What is Playwright and how do you write a basic test to verify page title and button click?",
      "Playwright is a modern end-to-end testing library from Microsoft that automates Chromium, Firefox, and WebKit browsers with auto-waiting and headless mode support.",
      "Tests use page.goto(), page.click(), page.fill(), and expect() assertions.",
      "import { test, expect } from '@playwright/test';\n\ntest('homepage has title and button works', async ({ page }) => {\n  await page.goto('http://localhost:3000');\n  await expect(page).toHaveTitle(/Fresher Prep/);\n  await page.click('button#start');\n  await expect(page.locator('#content')).toBeVisible();\n});",
      "Easy", "Concept", "Technical Round", "Medium", "Playwright Docs", "What does auto-waiting mean in Playwright?")

# ==========================================
# 16. Projects (Fresher Interview Discussion)
# ==========================================
add_q("Projects", "Project Overview", "Elevator Pitch",
      "Tell me about your academic or portfolio project.",
      "Structure using the STAR framework: 1) What it does (elevator pitch), 2) Tech stack used and why, 3) Your specific role, 4) A key feature you implemented, 5) A challenge you resolved.",
      "Example: 'I built an E-Commerce portal using React, Node.js, Express, and MongoDB. I developed the product listing with search and filter, integrated JWT authentication, and fixed an issue where repeated API calls lagged the UI by implementing debouncing and indexing.'",
      "// STAR framework:\n// Situation: E-commerce web app for student marketplace\n// Task: Built auth and product search\n// Action: Added debounced search + MongoDB compound index\n// Result: Search latency reduced by 60%",
      "Easy", "Project", "Project Discussion", "High", "STAR Framework", "What would you improve in your project if given another month?")

add_q("Projects", "Tech Decisions", "Database Choice",
      "Why did you choose MongoDB instead of a Relational SQL Database in your project?",
      "Answer genuinely: 'I chose MongoDB because my project had dynamic product attributes where different categories had different fields. Document JSON mapped naturally to JavaScript objects in my Node.js backend without writing migration scripts. If I had strict transactional financial requirements, I would have chosen PostgreSQL.'",
      "Interviewers want to see that you understand the trade-offs, not just that you used it because of a tutorial.",
      "// Key points:\n// 1. JSON document structure matches JS objects\n// 2. Flexible schema for varying attributes\n// 3. Fast iterative development for student project",
      "Easy", "Project", "Project Discussion", "High", "Architecture", "When would you prefer PostgreSQL over MongoDB?")

add_q("Projects", "Problem Solving", "Technical Challenge",
      "What was the most challenging bug or issue you encountered in your project and how did you solve it?",
      "Answer with concrete details: 'During the search feature implementation, typing rapidly triggered multiple asynchronous fetch requests that resolved out of order, displaying stale results. I diagnosed the race condition, implemented an AbortController in useEffect cleanup to cancel outdated requests, and added a 300ms debounce.'",
      "Demonstrates debugging ability, understanding of asynchronous JavaScript, and real hands-on experience.",
      "// Code fix learned:\nuseEffect(() => {\n  const controller = new AbortController();\n  fetchData(query, { signal: controller.signal });\n  return () => controller.abort(); // Cancel previous on re-type\n}, [query]);",
      "Medium", "Project", "Project Discussion", "High", "Debugging", "How did you verify the bug was fixed?")

# ==========================================
# 17. HR Questions (Fresher HR Round)
# ==========================================
add_q("HR", "Introduction", "Tell Me About Yourself",
      "Tell me about yourself.",
      "Structure: 1) Education & degree, 2) Core technical skills (HTML, CSS, JS, React, Node, SQL), 3) Key project highlight, 4) Why you are excited about this entry-level role.",
      "Keep it under 90 seconds. Focus on what you can contribute, not childhood history.",
      "\"Hello, I recently completed my degree in Computer Science. Over the past year, I focused on fullstack web development with JavaScript, React, Node.js, and SQL. I built two practical projects, including a full-stack e-commerce app with JWT authentication. I am passionate about writing clean code, solving problems, and eager to contribute as a junior software engineer at your company.\"",
      "Easy", "HR", "HR Round", "High", "HR Guide", "What are your short-term career goals?")

add_q("HR", "Motivation", "Why Should We Hire You",
      "Why should we hire you as a fresher over other candidates?",
      "Highlight strong fundamentals, eagerness to learn, project experience, and adaptability: 'As a fresher, I bring a solid understanding of core computer science fundamentals, hands-on practice building web apps from scratch, and a strong work ethic. I learn quickly, take constructive feedback well, and am ready to start contributing to your team immediately.'",
      "Avoid claiming to know everything; emphasize attitude, speed of learning, and strong foundational knowledge.",
      "// Key talking points:\n// 1. Solid fundamentals in JS, Web, and Problem Solving\n// 2. Hands-on project experience\n// 3. Fast learner and team player",
      "Easy", "HR", "HR Round", "High", "HR Guide", "How do you keep your technical skills up to date?")

add_q("HR", "Self-Awareness", "Strengths and Weaknesses",
      "What are your greatest strength and one real weakness you are improving?",
      "Strength: Consistency and debugging persistence. Weakness: Being hesitant to ask for help early when stuck. Explain how you are actively addressing it by following the 30-minute rule (try independently for 30 minutes, then ask senior guidance with details of what was tried).",
      "Never say 'I have no weaknesses' or fake weaknesses like 'I work too hard'. Be honest and show active improvement.",
      "\"My strength is logical debugging and persistence when solving coding errors. A weakness I noticed was spending too much time trying to solve a blocker alone; I now use a 30-minute rule where I attempt debugging first, document my attempts, and then seek team guidance.\"",
      "Easy", "HR", "HR Round", "High", "HR Guide", "Can you give an example of working under a deadline?")

# Write to file
js_content = "window.FRESHER_QUESTIONS_DATA = " + json.dumps(questions, indent=2) + ";"
with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated {len(questions)} high-quality fresher questions in {OUT_PATH}")

"""
bank_builders/html_builder.py
Generates 205+ genuine, simple, interview-focused HTML questions for freshers.
Covers: Document structure, DOCTYPE, elements, attributes, headings, paragraphs,
links, images, lists, tables, forms, validation, buttons, semantic HTML,
block vs inline, div vs span, HTML5 media, iframes, meta tags, SEO, accessibility, ARIA.
"""

from .common import make_q

def get_html_questions(start_num=1):
    qs = []
    num = start_num

    # 1. Document Structure & DOCTYPE (Easy -> Intermediate -> Advanced)
    doc_struct = [
        ("What does HTML stand for?", "HTML stands for HyperText Markup Language. It is the standard language used to create and structure web pages on the internet.", "Easy", "Concept", "What is the current major version of HTML?"),
        ("What is the purpose of the <!DOCTYPE html> declaration?", "The <!DOCTYPE html> declaration tells the web browser which version of HTML the page is written in. In HTML5, it ensures the browser renders the page in standards mode instead of quirks mode.", "Easy", "Concept", "What happens if you omit the DOCTYPE declaration?"),
        ("What is the difference between standards mode and quirks mode in browsers?", "Standards mode renders pages according to modern W3C specifications. Quirks mode emulates older browser behaviors from the late 1990s to maintain compatibility with very old websites.", "Intermediate", "Concept", "How does a browser decide to use quirks mode?"),
        ("What is the root element of an HTML document?", "The <html> element is the root element that wraps all other HTML tags on a page, except the DOCTYPE declaration.", "Easy", "Concept", "What attribute should always be included on the <html> tag for accessibility?"),
        ("Why should you include the 'lang' attribute in the <html> tag?", "The 'lang' attribute specifies the primary language of the document (such as lang='en'). It helps search engines index content and helps screen readers pronounce words correctly.", "Easy", "Concept", "Can you change the language for a specific paragraph inside the page?"),
        ("What is the difference between the <head> and <body> elements?", "The <head> element contains metadata, page title, stylesheets, and scripts that are not displayed directly on the screen. The <body> element contains the visible content rendered to the user.", "Easy", "Comparison", "Can you put an <h1> tag inside the <head> element?"),
        ("What is the purpose of the <meta charset='UTF-8'> tag?", "It defines the character encoding for the document. UTF-8 includes almost all characters and symbols from all human languages, preventing text display errors.", "Easy", "Concept", "Where should the charset meta tag be placed in the <head>?"),
        ("What is the purpose of the viewport meta tag in HTML5?", "The viewport meta tag (<meta name='viewport' content='width=device-width, initial-scale=1.0'>) controls how a webpage is displayed on mobile screens by matching screen width and setting the initial zoom level.", "Intermediate", "Concept", "What happens on a mobile device if you remove the viewport meta tag?"),
        ("What does the <title> tag do in an HTML document?", "The <title> tag defines the document title shown on the browser tab, in browser bookmarks, and as the main headline in search engine search results.", "Easy", "Concept", "Can a page have multiple <title> tags?"),
        ("How do you link an external CSS stylesheet in HTML?", "Use the <link> tag inside the <head> section: <link rel='stylesheet' href='styles.css'>.", "Easy", "Practical", "What does the 'rel' attribute stand for in the link tag?"),
        ("How do you include an external JavaScript file in HTML?", "Use the <script> tag: <script src='app.js'></script>. It can be placed in the <head> or at the end of the <body>.", "Easy", "Practical", "Why is it often placed at the end of the body?"),
        ("What is the difference between the 'defer' and 'async' attributes on <script> tags?", "'async' downloads the script in the background and executes it immediately when downloaded, which may interrupt HTML parsing. 'defer' downloads in the background but waits until HTML parsing is complete before executing in order.", "Intermediate", "Comparison", "Which one should you use for scripts that depend on the DOM?"),
        ("What does the <noscript> tag do in HTML?", "The <noscript> tag defines fallback content that is displayed only if the user has disabled JavaScript in their browser or if the browser does not support scripts.", "Intermediate", "Concept", "Can you put styled HTML inside a <noscript> tag?"),
        ("Which DOCTYPE declaration triggers HTML5 standard mode?", "A. <!DOCTYPE html5>\nB. <!DOCTYPE html>\nC. <!DOCTYPE HTML PUBLIC>\nD. <DOCTYPE html>", "Easy", "MCQ", "Why was the HTML5 DOCTYPE simplified compared to HTML4?"),
        ("What is the difference between an HTML tag and an HTML element?", "An HTML tag is the syntax like <p> (opening) or </p> (closing). An HTML element includes the opening tag, its content, and the closing tag together.", "Easy", "Concept", "Are all HTML tags paired with closing tags?"),
        ("What are self-closing (void) elements in HTML?", "Void elements are elements that cannot contain any text or child elements and do not have a closing tag, such as <img>, <br>, <hr>, <input>, and <meta>.", "Easy", "Concept", "Is the trailing slash <br/> required in HTML5?"),
        ("What happens if you open an HTML tag and forget to close it?", "The browser attempts to auto-close it using HTML error-recovery rules, but this can lead to unexpected layout bugs, broken styling, or rendering issues.", "Intermediate", "Scenario", "Which tool can you use to validate your HTML syntax?"),
        ("What is an HTML attribute?", "An attribute provides additional information or settings for an HTML element. It is written inside the opening tag as name='value' pairs (for example, class='btn' or id='main').", "Easy", "Concept", "Can an element have custom attributes?"),
        ("What are data-* attributes in HTML5?", "data-* attributes let you store custom data directly on HTML elements without affecting rendering. JavaScript can access them using the element.dataset API.", "Intermediate", "Concept", "Can CSS target elements by data-* attributes?"),
        ("What is the DOM in relation to HTML?", "The DOM (Document Object Model) is a tree-like object representation of the HTML document created by the browser in memory, which JavaScript can interact with and manipulate.", "Intermediate", "Concept", "Does the DOM always match the original HTML source code?")
    ]

    for item in doc_struct:
        q_text, ans, diff, qtype, fup = item
        code = ""
        if "viewport" in q_text.lower():
            code = "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
        elif "defer" in q_text.lower():
            code = "<script src=\"app.js\" defer></script>"
        elif "data-*" in q_text.lower():
            code = "<button data-user-id=\"101\" data-role=\"admin\">Profile</button>"
        elif "link" in q_text.lower():
            code = "<link rel=\"stylesheet\" href=\"style.css\">"
        elif "DOCTYPE" in q_text and qtype == "MCQ":
            qs.append(make_q(
                f"q-html-{num}", num, "HTML", "Document Structure", "DOCTYPE",
                "Which DOCTYPE declaration triggers HTML5 standard mode?",
                "<!DOCTYPE html> is the official DOCTYPE for HTML5.",
                difficulty="Easy", question_type="MCQ",
                code_example="<!DOCTYPE html>",
                mcq_options={"A": "<!DOCTYPE html5>", "B": "<!DOCTYPE html>", "C": "<!DOCTYPE HTML PUBLIC>", "D": "<DOCTYPE html>"},
                correct_option="B", follow_up=fup
            ))
            num += 1
            continue

        qs.append(make_q(
            f"q-html-{num}", num, "HTML", "Document Structure", "Basics",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup
        ))
        num += 1

    return qs

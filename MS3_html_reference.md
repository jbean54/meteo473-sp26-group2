# Milestone 3: HTML, CSS, and JavaScript Reference

This guide introduces the three languages of the web to students who know Python but have never written a webpage. Each section explains the concept, compares it to something from Python where helpful, and shows the syntax with examples.

> **Example files:** A working demo page is provided in the `html/` folder alongside this document (`index.html`, `styles.css`, `script.js`). Read through those files alongside this guide — they are heavily commented and demonstrate most of the concepts below.

> **Important — files must be in your web directory:** Your website files (`index.html`, `styles.css`, `script.js`, and any images) must be placed inside the `website/` folder within your group project directory (`/courses/meteo473/<semester>/473_<semester>_group<#>/website/`). This folder is a symlink that points to the publicly served web directory — anything you save there will be visible on your group's URL. `index.html` is the special filename that the web server renders automatically when someone visits that URL — it is your homepage.

> **Use a real browser to view your website, not Jupyter:** Some JavaScript features (event listeners, form interactions, dynamic image swapping) will not work when you open an HTML file inside the JupyterHub file editor. Always test your page by visiting your public URL in a real browser. A hard reload (Shift + click the refresh button in Chrome) may be needed to see recent changes if the browser has cached an older version.

---

## 1. How a Webpage Is Built

A webpage is made of three languages that each play a different role — think of them like layers:

| Language | Role | Python analogy |
|----------|------|----------------|
| **HTML** | Structure — defines what's on the page | The data itself (variables, lists) |
| **CSS** | Appearance — controls colors, fonts, layout | Matplotlib figure styling |
| **JavaScript** | Behavior — makes the page interactive | Functions that respond to events |

All three files are loaded by the browser when someone visits your page. You link CSS and JavaScript files from inside your HTML file.

---

## 2. Basic Document Structure

Every HTML file follows the same skeleton. Indentation and whitespace don't affect behavior (unlike Python), but they make the file readable.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Metadata — not visible on the page -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page Title</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Everything visible goes here -->
    <p>Hello, world!</p>

    <!-- JavaScript goes at the bottom of the body -->
    <script src="script.js"></script>
</body>
</html>
```

**Key points:**
- `<!DOCTYPE html>` tells the browser this is modern HTML5
- `<html>` wraps the entire document
- `<head>` contains metadata — the title bar, links to CSS, etc. None of it appears on the page itself
- `<body>` contains everything the user sees
- `<script>` is placed at the bottom so the HTML loads before JavaScript runs

### HTML Tags

HTML is written as **tags** — opening and closing pairs that wrap content:

```html
<tagname>content goes here</tagname>
```

Some tags are **self-closing** (they have no content):
```html
<img src="plot.png" alt="My plot">
<br>
<hr>
```

**Comments** in HTML use `<!-- -->`:
```html
<!-- This is a comment and won't appear on the page -->
```

---

## 3. Head Elements

The `<head>` section is invisible to users but critical for the page to work correctly.

```html
<head>
    <!-- Character encoding — always include this -->
    <meta charset="UTF-8">

    <!-- Makes the page responsive on phones and tablets -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- The text that appears in the browser tab -->
    <title>My Threat Index</title>

    <!-- Link to your external CSS file -->
    <link rel="stylesheet" href="styles.css">
</head>
```

---

## 4. Headings

HTML has six levels of headings, `<h1>` through `<h6>`. Think of them like section levels in a report.

```html
<h1>Page Title (largest — use once per page)</h1>
<h2>Section Heading</h2>
<h3>Subsection Heading</h3>
<h4>Smaller subheading</h4>
<h5>Even smaller</h5>
<h6>Smallest heading</h6>
```

> **Rule of thumb:** Use only one `<h1>` per page. Headings should be used for document structure, not just to make text bigger (use CSS for that).

---

## 5. Paragraphs and Text Formatting

```html
<!-- Paragraph -->
<p>This is a paragraph of text. Browsers ignore extra whitespace in HTML.</p>

<!-- Bold and italic -->
<p>This word is <strong>bold</strong> and this one is <em>italic</em>.</p>

<!-- <b> and <i> also create bold/italic but with less semantic meaning -->
<p>Also <b>bold</b> and <i>italic</i>.</p>

<!-- Line break (like \n in Python strings) -->
<p>Line one.<br>Line two.</p>

<!-- Horizontal rule (a dividing line) -->
<hr>

<!-- Inline code styling -->
<p>Run the function <code>calculate_index()</code> to get started.</p>
```

---

## 6. Links

The `<a>` (anchor) tag creates hyperlinks. The destination is set with the `href` attribute.

```html
<!-- Link to an external site — opens in a new tab -->
<a href="https://www.w3schools.com/html/" target="_blank">W3Schools HTML Reference</a>

<!-- Link to another page in your project -->
<a href="about.html">About Page</a>

<!-- Link to a section on the same page (uses an id) -->
<a href="#results">Jump to Results</a>

<!-- Then somewhere on the page: -->
<section id="results">
    <h2>Results</h2>
    ...
</section>
```

**Important attributes:**
- `href` — the URL or file path the link goes to
- `target="_blank"` — opens in a new browser tab

---

## 7. Images

```html
<!-- Basic image -->
<img src="images/threat_000.png" alt="Threat index for hour 000">

<!-- Image with a fixed width -->
<img src="images/threat_000.png" alt="Threat index for hour 000" width="600">

<!-- Image with caption using <figure> and <figcaption> -->
<figure>
    <img src="images/threat_000.png" alt="Threat index for hour 000" width="600">
    <figcaption>GFS-based threat index, valid 00Z March 16 2026.</figcaption>
</figure>
```

**Important attributes:**
- `src` — the path to the image file (relative to your HTML file, or an absolute path)
- `alt` — a text description shown if the image fails to load, and used by screen readers
- `width` / `height` — size in pixels (use only one to preserve the aspect ratio)

> **Tip:** Organize your images in a subfolder like `images/` to keep the project directory clean.

---

## 8. Lists

### Unordered list (bullet points)

```html
<ul>
    <li>Wind speed</li>
    <li>Dew point temperature</li>
    <li>Precipitation rate</li>
</ul>
```

### Ordered list (numbered)

```html
<ol>
    <li>Download model data</li>
    <li>Calculate threat index</li>
    <li>Save plots as PNG</li>
</ol>
```

Lists can be nested — just put a `<ul>` or `<ol>` inside a `<li>`:

```html
<ul>
    <li>Model inputs
        <ul>
            <li>Temperature</li>
            <li>Wind</li>
        </ul>
    </li>
    <li>Derived parameters</li>
</ul>
```

---

## 9. Tables

Tables are built row by row. `<thead>` holds the header row, `<tbody>` holds the data rows.

```html
<table>
    <thead>
        <tr>
            <th>Forecast Hour</th>
            <th>Max Threat Index</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>f000</td>
            <td>2.4</td>
        </tr>
        <tr>
            <td>f006</td>
            <td>3.7</td>
        </tr>
    </tbody>
</table>
```

| Tag | Meaning |
|-----|---------|
| `<table>` | The whole table |
| `<thead>` | Header section |
| `<tbody>` | Body/data section |
| `<tr>` | Table row |
| `<th>` | Header cell (bold, centered by default) |
| `<td>` | Data cell |

---

## 10. Divs, Sections, and Spans

These tags are used to group and organize content. They have no visual appearance on their own — they only become useful when you attach CSS or JavaScript to them.

```html
<!-- <div> is a generic block-level container (takes up the full width) -->
<div id="main-content">
    <p>This paragraph is inside a div.</p>
</div>

<!-- <section> is like a <div> but with semantic meaning (used for page sections) -->
<section id="results">
    <h2>Results</h2>
    <p>Our threat index produced reasonable values for all test cases.</p>
</section>

<!-- <span> is an inline container (stays within the flow of text) -->
<p>The index reached a peak value of <span style="color: red;">5.0</span> at hour 012.</p>
```

**Block vs. inline:**
- **Block elements** (`<div>`, `<section>`, `<p>`, `<h2>`) start on a new line and take up the full width
- **Inline elements** (`<span>`, `<a>`, `<strong>`, `<em>`) flow within the surrounding text

---

## 11. Navigation Bar

The `<nav>` element marks a section of navigation links. Combined with CSS, it becomes the menu bar at the top of a page.

```html
<nav>
    <a href="#about">About</a>
    <a href="#results">Results</a>
    <a href="#contact">Contact</a>
</nav>
```

---

## 12. Forms and Inputs

Forms collect input from the user. Without a server, you can handle the data with JavaScript.

```html
<form id="myForm">
    <!-- Text input -->
    <label for="nameInput">Name:</label>
    <input type="text" id="nameInput" name="name" placeholder="Your name">

    <!-- Multi-line text area -->
    <label for="messageInput">Message:</label>
    <textarea id="messageInput" name="message" rows="4"></textarea>

    <!-- Dropdown selector -->
    <label for="hourSelect">Forecast hour:</label>
    <select id="hourSelect">
        <option value="000">Hour 000</option>
        <option value="006">Hour 006</option>
        <option value="012">Hour 012</option>
    </select>

    <!-- Submit button -->
    <button type="submit">Submit</button>
</form>
```

The `<label>` tag is paired with an input by matching the `for` attribute on the label to the `id` on the input. This makes the label clickable and improves accessibility.

---

## 13. Buttons

```html
<!-- Standalone button (no form submission) -->
<button id="myButton">Click Me</button>

<!-- Submit button inside a form -->
<button type="submit">Submit</button>

<!-- Button that doesn't submit (useful with JavaScript) -->
<button type="button" id="prevBtn">Previous</button>
```

---

## 14. Attributes: id and class

Attributes give HTML elements extra information. The two most important ones are `id` and `class`.

```html
<!-- id — unique identifier. Only ONE element on the page should have a given id.
     Used to target a specific element with CSS (#id) or JavaScript (getElementById) -->
<div id="main-content">...</div>

<!-- class — reusable label. MANY elements can share the same class.
     Used to apply the same CSS style to multiple elements (.classname) -->
<div class="content-block">First section</div>
<div class="content-block">Second section</div>
```

In your CSS file:
```css
/* Target by id — uses # */
#main-content {
    max-width: 900px;
    margin: 0 auto;
}

/* Target by class — uses . */
.content-block {
    background-color: white;
    padding: 20px;
    margin-bottom: 16px;
}
```

---

## 15. Inline Style vs. External CSS

You can apply CSS in two ways. Prefer the external file for anything that applies to multiple elements.

```html
<!-- Inline style — applies only to this one element -->
<p style="color: red; font-weight: bold;">Warning text</p>

<!-- Class-based style in styles.css — reusable across many elements -->
<p class="warning">Warning text</p>
```

In `styles.css`:
```css
.warning {
    color: red;
    font-weight: bold;
}
```

---

## 16. Connecting JavaScript

JavaScript is loaded via a `<script>` tag, placed at the **bottom of the body** (after all your HTML). This ensures the HTML elements exist before JavaScript tries to interact with them.

```html
<body>
    <!-- ... all your HTML ... -->

    <script src="script.js"></script>
</body>
```

The most common way JavaScript interacts with HTML is through `getElementById`:

```javascript
// Get a reference to an HTML element by its id
const myButton = document.getElementById("myButton");

// Do something when the button is clicked
myButton.addEventListener("click", () => {
    alert("Button was clicked!");
});
```

Changing element content from JavaScript:
```javascript
// Change the text inside an element
document.getElementById("plot-label").textContent = "Showing: threat_012.png";

// Change the src of an image
document.getElementById("my-img").src = "images/threat_012.png";

// Add or remove a CSS class
document.getElementById("info-box").classList.add("hidden");
document.getElementById("info-box").classList.remove("hidden");
document.getElementById("info-box").classList.toggle("hidden");
```

---

## 17. Useful Browser Tool: DevTools

Every modern browser has **Developer Tools** (press `F12` or right-click → Inspect). This is invaluable for debugging your webpage:

- **Elements tab** — shows the live HTML structure; hover over elements to highlight them on the page
- **Console tab** — shows JavaScript errors and lets you run JS commands; use `console.log("value")` in your script to print values here (like Python's `print()`)
- **Network tab** — shows which files loaded and whether any failed (e.g., missing images)

If your page isn't looking right, open DevTools first.

---

## 18. Quick Reference: Common Tags

| Tag | Purpose |
|-----|---------|
| `<h1>`–`<h6>` | Headings (h1 is largest) |
| `<p>` | Paragraph |
| `<strong>` | Bold text (semantic) |
| `<em>` | Italic text (semantic) |
| `<a href="...">` | Hyperlink |
| `<img src="..." alt="...">` | Image |
| `<ul>` / `<ol>` | Unordered / ordered list |
| `<li>` | List item |
| `<table>` | Table container |
| `<tr>` / `<th>` / `<td>` | Table row / header cell / data cell |
| `<div>` | Generic block container |
| `<section>` | Semantic section container |
| `<span>` | Inline container |
| `<nav>` | Navigation links |
| `<header>` | Page or section header |
| `<footer>` | Page or section footer |
| `<figure>` / `<figcaption>` | Image with caption |
| `<form>` | Form container |
| `<input>` | Text field, checkbox, etc. |
| `<textarea>` | Multi-line text input |
| `<select>` / `<option>` | Dropdown selector |
| `<button>` | Clickable button |
| `<label>` | Label for a form input |
| `<code>` | Inline code snippet |
| `<br>` | Line break (self-closing) |
| `<hr>` | Horizontal rule/divider (self-closing) |
| `<!-- ... -->` | Comment |

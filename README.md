# lightdown

A minimal Python web framework for building simple websites using **Markdown** and **routing**.

## Features
- Easy routing system
- Render `.md` files directly as HTML
- Pass context variables into Markdown templates
- Static file support (`/static`)
- Works with both **Markdown** (`.md`) and **HTML** (`.html`) files

## Installation

```bash
pip install lightdown
```

## Quick Start

```python
from lightdown.core import App

app = App()

@app.route("/")
def home():
    return ("index.md", {"title": "Hoşgeldiniz", "message": "Bu bir mini framework!"})

if __name__ == "__main__":
    app.run()
```

## Example `markdown/index.md`

```markdown
# {{ title }}

This is a simple page rendered with **Markdown**.  

Message: {{ message }}
```

When you start the server and visit `http://127.0.0.1:8000/`,  
you will see your Markdown page rendered as HTML.

## Static Files
Place your static files (CSS, JS, images) inside the `static/` folder.  
They can be accessed at `/static/filename.css`.

## Notes
- Works with `.md` templates (recommended).
- Can also be used with `.html` templates.

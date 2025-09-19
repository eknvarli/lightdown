import markdown
import os

def render_markdown(filepath, context=None):
    if not os.path.exists(filepath):
        return '<h1>Markdown file not found</h1>'

    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    if context:
        for key, value in context.items():
            text = text.replace(f"{{{{ {key} }}}}", str(value))

    return markdown.markdown(text)

import os

class TemplateEngine:
    def __init__(self, template_dir='templates'):
        self.template_dir = template_dir

    def render(self, template_name, context=None):
        context = context or {}
        template_path = os.path.join(self.template_dir, template_name)

        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()

        for key, value in context.items():
            content = content.replace(f"{{{{ {key} }}}}", str(value))

        return content

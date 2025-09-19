from http.server import BaseHTTPRequestHandler, HTTPServer
from .router import Router
from .template_engine import TemplateEngine
from .markdown_renderer import render_markdown
from .static_handler import StaticHandler
import os


class App:
    def __init__(self, template_dir='templates', static_dir='static', markdown_dir='markdown'):
        self.router = Router()
        self.templates = TemplateEngine(template_dir)
        self.static_handler = StaticHandler(static_dir)
        self.markdown_dir = markdown_dir

    def route(self, path):
        def decorator(func):
            self.router.add_router(path, func)
            return func
        return decorator
    
    def run(self, host='127.0.0.1', port=8000):
        app = self

        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path.startswith('/static/'):
                    rel_path = self.path.replace('/static/','')
                    content, mime_type = app.static_handler.get_file(rel_path)

                    if content:
                        self.send_response(200)
                        self.send_header('Content-type', mime_type)
                        self.end_headers()
                        self.wfile.write(content)
                        return
                    
                handler = app.router.resolve(self.path)
                
                if handler:
                    response = handler()
                    if isinstance(response, tuple) and len(response) == 2:
                        filename, context = response
                        if filename.endswith('.html'):
                            response = app.templates.render(filename, context)
                        elif filename.endswith('.md'):
                            filepath = os.path.join(app.markdown_dir, filename)
                            response = render_markdown(filepath, context)

                    elif isinstance(response, str):
                        if response.endswith('.md'):
                            filepath = os.path.join(app.markdown_dir, response)
                            response = render_markdown(filepath)
                        elif response.endswith('.html'):
                            response = app.templates.render(response)


                    
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(response.encode('utf-8'))

                else:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b'404 Not Found')

        server = HTTPServer((host, port), RequestHandler)
        print(f'Server running on http://{host}:{port}')
        server.serve_forever()
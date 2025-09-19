import os
from mimetypes import guess_type


class StaticHandler:
    def __init__(self, static_dir='static'):
        self.static_dir = static_dir

    def get_file(self, path):
        file_path = os.path.join(self.static_dir, path.lstrip('/'))

        if os.path.exists(file_path) and os.path.isfile(file_path):
            mime_type, _ = guess_type(file_path)
            
            with open(file_path, 'rb') as f:
                return f.read(), mime_type or 'application/octet-stream'
            
        return None, None
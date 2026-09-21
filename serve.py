import http.server
import socketserver
import os

PORT = 8000

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Remove trailing slash to handle browser cached redirects
        if self.path != '/' and self.path.endswith('/'):
            self.path = self.path[:-1]

        # Default behavior for root
        if self.path == '/':
            self.path = '/index.html'
        else:
            # Check if path + '.html' exists as a file first (prioritize file over directory)
            if os.path.isfile(self.translate_path(self.path + '.html')):
                self.path += '.html'
            elif not os.path.exists(self.translate_path(self.path)):
                self.path = '/404.html'
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), CleanURLHandler) as httpd:
    print(f"Servidor rodando em http://localhost:{PORT}")
    httpd.serve_forever()

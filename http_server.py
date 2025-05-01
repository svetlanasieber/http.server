from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"Hello from pure Python web server!")

httpd = HTTPServer(('localhost', 8000), SimpleHandler)
print("Running on http://localhost:8000/")
httpd.serve_forever()

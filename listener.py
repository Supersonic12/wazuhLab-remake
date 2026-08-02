#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer


class UploadHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)

        filename = self.path.lstrip('/') or 'uploaded_file'
        with open(filename, 'wb') as f:
            f.write(data)

        print(f"[+] Received {length} bytes -> saved as {filename}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Upload received\n")


if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), UploadHandler)
    print("Listening on 0.0.0.0:8000 ...")
    server.serve_forever()

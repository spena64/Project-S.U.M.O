from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import socketserver
import json

PORT = 8080

# Resource requests
class requestHandler(BaseHTTPRequestHandler):
    def set_headers(self, contentType):
        self.send_response(200)
        self.send_header("Content-type", contentType)
        self.end_headers()
    
    def do_GET(self):
        if self.path == "/":
            self.path = "/gametest.html"

        try:
            mimeType = ""
            sendReply = False
            if self.path.endswith(".html"):
                mimeType = "text/html"
                sendReply = True
            if self.path.endswith(".js"):
                mimeType = "application/javascript"
                sendReply = True
            if self.path.endswith(".css"):
                mimeType = "text/css"
                sendReply = True
            
            if sendReply:
                file = open(curdir + sep + self.path)
                fileHtml = file.read()
                self.set_headers(mimeType)
                self.wfile.write(fileHtml.encode("utf8"))
                file.close()
            return
        except IOError:
            self.send_error(404, f"File Not Found: {self.path}")

# Start server
with HTTPServer(("", PORT), requestHandler) as server:
    print("serving at port", PORT)
    server.serve_forever()
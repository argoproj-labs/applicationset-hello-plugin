#!/usr/bin/env python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

with open("/var/run/argo/token") as f:
    token = f.read().strip()


class Plugin(BaseHTTPRequestHandler):
    def args(self):
        return json.loads(self.rfile.read(int(self.headers.get('Content-Length'))))

    def reply(self, reply):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(reply).encode("UTF-8"))

    def forbidden(self):
        self.send_response(403)
        self.end_headers()

    def unsupported(self):
        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        if self.headers.get("Authorization") != "Bearer " + token:
            self.forbidden()
            return

        if self.path == '/api/v1/getparams.execute':
            # args = self.args()
            self.reply([
                {
                    "hello": "world",
                },
                {
                    "hello": "again",
                }
            ])
        else:
            self.unsupported()


if __name__ == '__main__':
    httpd = HTTPServer(('', 4355), Plugin)
    httpd.serve_forever()

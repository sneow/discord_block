#!/usr/bin/python
import configparser
from http.server import BaseHTTPRequestHandler, HTTPServer

config = configparser.ConfigParser()
config.read('settings.ini')

port = int(config['DEFAULT']['port'])
discord_server = config['DEFAULT']['discord_server']

class discord_block(BaseHTTPRequestHandler):

    # returns a redirect header to config-specific discord server
    def do_GET(self):
        self.send_response(301)
        self.send_header('Location', discord_server)
        self.end_headers()
        return

try:

    server = HTTPServer(('', port), discord_block)
    print('Discord redirection server started on port ', port)
    server.serve_forever()

except KeyboardInterrupt:

    'Shutting down redirect server..'
    server.socket.close()

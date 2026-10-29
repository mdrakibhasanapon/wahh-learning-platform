#!/usr/bin/env python3
"""
WAHH Security Academy - Local Web Server
Runs a lightweight, zero-dependency HTTP server for the learning platform.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Clean terminal output for requests
        sys.stderr.write(f"[{self.log_date_time_string()}] {args[0]} - {args[1]}\n")

def find_open_port(starting_port):
    import socket
    port = starting_port
    while port < starting_port + 50:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
            port += 1
    return starting_port

def main():
    os.chdir(DIRECTORY)
    port = find_open_port(PORT)
    
    server_address = ('0.0.0.0', port)
    
    # Enable socket reuse
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(server_address, Handler) as httpd:
        url = f"http://localhost:{port}"
        print("\n" + "="*70)
        print("  🛡️  WAHH Security Academy - The Web Application Hacker's Handbook")
        print("="*70)
        print(f"  ✓ Platform Server Running at: {url}")
        print(f"  ✓ Local Directory:            {DIRECTORY}")
        print("  ✓ Press Ctrl+C to stop the server anytime.")
        print("="*70 + "\n")
        
        # Try to open in browser automatically if DISPLAY is set
        if os.environ.get('DISPLAY') or os.environ.get('WAYLAND_DISPLAY'):
            try:
                webbrowser.open(url)
            except Exception:
                pass
                
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down WAHH Security Academy server. Happy hacking!\n")
            httpd.server_close()

if __name__ == '__main__':
    main()

import http.server
import socketserver
import os

PORT = 7575
# Forza la cartella corrente come root del server
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server spotiFUCK PWA attivo sulla porta {PORT}")
    httpd.serve_forever()

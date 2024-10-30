import http.server
import socketserver
import ssl

PORT = 8443  # Utilisez un port HTTPS standard, par exemple 8443 pour les tests

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Serveur HTTPS Python</h1></body></html>")

# Configurer le serveur HTTP
httpd = socketserver.TCPServer(("", PORT), MyHandler)

# Charger le certificat et la clé pour activer SSL
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile="key.pem",
    certfile="cert.pem",
    server_side=True
)

print("Serveur HTTPS en cours d'exécution sur le port", PORT)
httpd.serve_forever()

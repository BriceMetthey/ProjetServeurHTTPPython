from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import csv

class MonServeurHTTP(BaseHTTPRequestHandler):
    
    def send_html_response(self, status_code, title, message):
        """Méthode pour envoyer une réponse HTML formatée avec encodage UTF-8."""
        self.send_response(status_code)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        # Template HTML simple
        html_content = f"""
        <html lang="fr">
            <head>
                <title>{title}</title>
            </head>
            <body>
                <h1>{title}</h1>
                <p>{message}</p>
            </body>
        </html>
        """
        self.wfile.write(html_content.encode("utf-8"))
    
    
    def send_html_table_response(self, title, headers, rows):
        """Méthode pour envoyer une réponse HTML formatée sous forme de tableau."""
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        # Création de la table HTML
        html_content = f"""
        <html lang="fr">
            <head>
                <title>{title}</title>
            </head>
            <body>
                <h1>{title}</h1>
                <table border="1">
                    <tr>
        """
        # Ajout des en-têtes
        for header in headers:
            html_content += f"<th>{header}</th>"
        html_content += "</tr>"
        
        # Ajout des lignes de données
        for row in rows:
            html_content += "<tr>"
            for cell in row:
                html_content += f"<td>{cell}</td>"
            html_content += "</tr>"

        html_content += """
                </table>
            </body>
        </html>
        """
        
        # Envoi de la réponse encodée en UTF-8
        self.wfile.write(html_content.encode("utf-8"))

    def do_GET(self):
        # Analyse du chemin demandé
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path  # Récupération du chemin sans les paramètres
        query_components = urllib.parse.parse_qs(parsed_path.query)
        
        print("---------------------------------")
        print("Méthode HTTP GET")
        print("Chemin:", path)
        print("Paramètres:", query_components)
        print("---------------------------------")

        # Analyse du chemin /submit
        if path == "/submit":
            # Traitement des paramètres
            username = query_components.get("username", ["non fourni"])[0] 
            email = query_components.get("email", ["non fourni"])[0]
            password = query_components.get("password", ["non fourni"])[0]
            comment = query_components.get("comment", ["non fourni"])[0]
            
            message = f"Merci pour votre envoi {username}.<br> Votre email est : {email} <br> Votre password est : {password} <br> Votre commentaire est : {comment} "
            print("GET /submit with :", username, email, password, comment )
            self.send_html_response(200, "Envoi réussi via HTTP GET", message)

        # Analyse du chemin /recherche/utilisateur
        elif path == "/recherche/utilisateur" and query_components.get("filtre") == ["sans"]:
            try:
                # Lecture du fichier CSV avec DictReader
                with open("csv/utilisateurs.csv", newline='', encoding="utf-8") as csvfile:
                    reader = list(csv.DictReader(csvfile, delimiter=';'))
                    if len(reader) > 0 :
                        premier_dico = reader[0]
                        headers = list(premier_dico.keys())  # Les en-têtes de colonne
                        
                        # Les valeurs : tableau de tableau  ex : [ [val1,val2] , [val3,val4]   ]
                        rows = []
                        for dico in reader :
                            current_row = list(dico.values())
                            rows.append(current_row)
                    else :
                        
                        error_message = "Erreur : le fichier CSV ne contient aucunes données."
                        print(error_message)
                        self.send_html_response(404, "Aucunes Données", error_message)
                        return
                        

                print("CSV file read successfully.")
                
                # Envoi de la réponse sous forme de tableau HTML
                self.send_html_table_response("Liste des Utilisateurs", headers, rows)

            except FileNotFoundError:
                error_message = "Erreur : fichier CSV introuvable."
                print(error_message)
                self.send_html_response(404, "Erreur de Fichier", error_message)

        else:
            # Si le chemin n'est pas reconnu, afficher les paramètres
            message = f"Chemin inconnu '{path}'. Paramètres GET : {query_components}"
            print(f"GET {path} with parameters:", query_components)
            self.send_html_response(404, "Chemin inconnu", message)
            
            

    def do_POST(self):
        # Analyse du chemin demandé
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path  # Récupération du chemin sans les paramètres
        
        # Récupérer la longueur des données envoyées par POST
        content_length = int(self.headers["Content-Length"])
        
        # Lire les données envoyées par POST
        post_data = self.rfile.read(content_length)
        post_params = urllib.parse.parse_qs(post_data.decode("utf-8"))
        
        print("---------------------------------")
        print("Méthode HTTP POST")
        print("Chemin:", path)
        print("Paramètres:", post_params)
        print("---------------------------------")

        # Analyse du chemin et traitement des paramètres
        if path == "/submit":
            
            # Vérifier les paramètres attendus "username", "email", "password", "comment"
            username = post_params.get("username", ["non fourni"])[0]
            email = post_params.get("email", ["non fourni"])[0]
            password = post_params.get("password", ["non fourni"])[0]
            comment = post_params.get("comment", ["non fourni"])[0]
            
            message = f"Merci pour votre envoi {username}.<br> Votre email est : {email} <br> Votre password est : {password} <br> Votre commentaire est : {comment} "
            print("POST /submit with :", username, email, password, comment )
            
            self.send_html_response(200, "Envoi réussi via HTTP POST", message)

        else:
            # Si le chemin n'est pas reconnu, afficher les paramètres
            message = f"Chemin inconnu '{path}'. Paramètres POST : {post_params}"
            print(f"POST {path} with parameters:", post_params)
            self.send_html_response(404, "Chemin inconnu", message)

def run(server_class=HTTPServer, handler_class=MonServeurHTTP, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serveur démarré sur le port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

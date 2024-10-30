# Serveur HTTP en Python :snake:

Serveur web minimal en Python sans bibliothèques tièrces.

## :bicyclist: Execution du serveur 

`python serveurHTTP.py`

- Utiliser les formulaires HTML mis à disposition `formulaire_GET.html` et `formulaire_POST.html` pour tester l'envois de formulaires HTML via les méthodes GET et POST.
- Dans un navigateur lancer l'URL :  `http://localhost:8080//recherche/utilisateur?filtre=sans` pour lancer la lecture et l'envoi de données provenant d'un fichier CSV.

## :notebook: Améliorations

- [ ] Approche modulaire pour la génération HTML
- [ ] Approche modulaire pour le traitement des requêtes (1 fichier POST, 1 fichier GET)
- [ ] Utiliser un outil en ligne de commande (curl) voir https://curl.se/docs/tutorial.html
- [ ] Ajouter paramètres optionnels  `python serveurHTTP.py --port:9000`
- [X] Explorer usage HTTPS ?


## Serveur HTTPS (A terminer ...)

Générer un Certificat SSL (auto-signé) : Pour un usage de test ou de développement, vous pouvez générer un certificat auto-signé. Cela peut être fait via OpenSSL (si installé) :

`openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365`

- `key.pem` : le fichier de clé privée.
- `cert.pem` : le certificat auto-signé.

- Ce script configure un serveur HTTP simple qui écoute sur le port 8443.
- Avec ssl.wrap_socket, le serveur devient un serveur HTTPS en utilisant les certificats fournis.

### Tester le Serveur HTTPS

1. Exécutez le serveur avec ce script Python.

2. Ouvrez un navigateur web et accédez à https://localhost:8443. Le navigateur affichera probablement un avertissement de sécurité parce que le certificat est auto-signé. Vous pouvez ajouter une exception de sécurité pour accéder au site en local.

3. Utiliser un certificat valide en production : Pour un serveur en production, vous devez utiliser un certificat signé par une autorité de certification reconnue (CA) pour éviter les avertissements de sécurité. Vous pouvez obtenir des certificats gratuits via des services comme Let’s Encrypt.

# Serveur HTTP en Python

Serveur web minimal en Python sans bibliothèques tièrces.

## Execution du serveur

`python serveurHTTP.py`

## Usages

- Utiliser les formulaires mis à disposition pour tester les envois de formulaires via les méthodes GET et POST.
- Dans un navigateur lancer l'URL :  `http://localhost:8080//recherche/utilisateur?filtre=sans` pour lancer la lecture et l'envoi de données provenant d'un fichier CSV.

## Améliorations

- [] Approche modulaire pour la génération HTML
- [] Approche modulaire pour le traitement des requêtes (1 fichier POST, 1 fichier GET)
- [] Utiliser un outil en ligne de commande (curl) voir https://curl.se/docs/tutorial.html
- [] Ajouter paramètres optionnels  `python serveurHTTP.py --port:9000`


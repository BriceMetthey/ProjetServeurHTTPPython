# Serveur HTTP en Python :snake:

Serveur web minimal en Python sans bibliothèques tièrces.

## :bicyclist: Execution du serveur 

`python serveurHTTP.py`

## :plate_with_cutlery: Usages 

- Utiliser les formulaires HTML mis à disposition `formulaire_GET.html` et `formulaire_POST.html` pour tester l'envois de formulaires HTML via les méthodes GET et POST.
- Dans un navigateur lancer l'URL :  `http://localhost:8080//recherche/utilisateur?filtre=sans` pour lancer la lecture et l'envoi de données provenant d'un fichier CSV.

## :notebook: Améliorations

- [ ] Approche modulaire pour la génération HTML
- [ ] Approche modulaire pour le traitement des requêtes (1 fichier POST, 1 fichier GET)
- [ ] Utiliser un outil en ligne de commande (curl) voir https://curl.se/docs/tutorial.html
- [ ] Ajouter paramètres optionnels  `python serveurHTTP.py --port:9000`
- [ ] Explorer usage HTTPS ?

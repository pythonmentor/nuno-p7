# GrandPy
OpenclassRooms projet7

Programme tournant sur un serveur Flask codé en Python en environnement virtuel. Avant de lancer le programme, il faut installer "requirements.txt". 
Le programme contient un dossier Test qui héberge les différents tests de modules python.
Sur le dossier GrandPyApp on trouve, l’application web divisé un modules python.
•	first_imput_parser : qui vas « épurer » les entées utilisateur afin de mieux traiter et faire des différentes requêtes nécessaires.
•	Interface_requests : gérera les requêtes aux APIs Google Maps et WIKI.
•	Process : va rassembler les différentes réponses, et préparer les résultats à envoyer sur la page « interface » « /process » afin d’être affiché en dynamique sur la page principale.
•	Views : qui va gérer la mise en route du serveur, l’affichage principal et les échanges back/front.
Sur le dossier « templates » on va avoir le fichier HTML de la page
Et pour finir « static » vas avoir les images le code css et aussi le code Javascript.
Afin d’intervenir dynamiquement sur la page on utilisera AJAX. 

Le programme se lance par le module "run.py". 




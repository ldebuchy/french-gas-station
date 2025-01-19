# E3FI - PR2 : Projet de Python

L'objectif du mini projet est de pouvoir interragir sur une api pour gerrer des données. Nous avons fait le choix d'utiliser une api sur les stations essence de france. Vous utiliserez des données en Open Data.


## USER GUIDE

### INSTALLATION

1. Clonez ce dépôt dans votre environnement local :

   git clone https://github.com/ldebuchy/french-gas-station

2. Accédez au répertoire du projet :

   cd FRENCH-GS-STATION

3. Installez les dépendances nécessaires :

   $ python -m pip install -r requirements.txt


## UTILISATION

1. Éxecuter le fichier main.py dans une invite de commande.

   $ python main.py

2. Ouvrez un navigateur web taper:

   http://127.0.0.1:8050/

3. Remplissez les paramètres pour affiner vos recherches.


## ANALYSE DES DONNÉES

### ELEMENT 1 : HISTOGRAME

Le graphic permet de comparer les prix des carburants en fonction du département.

### ELEMENT 2 : CARTE DYNAMIQUE DES STATIONS ESSENCE

La carte affiche l'ensemble des stations de france puis seulement celle qui correspondent à vos critaires.


# DEVELOPER GUIDE
### LE PROJET

Le mini projet à 3 dossiers principaux :
assets : Contient le fichier style.css
data : Contient les données enregistrer de la précedente utilisation
src : Contient le code de notre Dashboard

### AJOUTER DU CODE

Pour ajouter du code, suivre les étages suivantes :

1. Creer le fichier python avec sa fonction

2. Ajouter les Div necessaire pour afficher ce que vous venez de rajouter dans le fichier home_page.py

3. Rajouter les callbacks pour interagir avec, dans le fichier callbacks.py

### ARCHITECTURE DU CODE
assets
-->style.css
data
-->raw
---->rawdata.csv
src
-->Pages
---->Viz
------>__init__.py
------>carte.py
------>histogram.py
---->__init__.py
---->callbacks.py
---->home_page.py
-->Utils
---->__init__.py
---->data_analyse.py
---->get_data.py
main.py
README.md
requirements.txt
video.mkv

## COPYRIGHT

je déclare sur l’honneur que le code fourni a été produit par moi/nous même, à l’exception des lignes ci dessous ;
pour chaque ligne (ou groupe de lignes) empruntée, donner la référence de la source et une explication de la syntaxe utilisée ;
toute ligne non déclarée ci dessus est réputée être produite par l’auteur (ou les auteurs) du projet. L’absence ou l’omission de déclaration sera considéré comme du plagiat.
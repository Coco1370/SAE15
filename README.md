# Projet : Visualisation des expérimentations 5G en France

## Description du projet

Ce projet permet d’analyser et de visualiser les expérimentations 5G réalisées en France à partir d’un fichier CSV contenant les données officielles (région, opérateur, fréquences, coordonnées GPS, etc.).  
Le script Python génère automatiquement :
- Une **carte interactive** avec un marqueur par région.
- Des **graphiques** et **tableaux** pour chaque région.
- Des **liens vers des pages HTML régionales** (ex : `Ile-de-France.html`, `Normandie.html`…).

## Technologies utilisées

- **Python 3**
- **Pandas** → traitement des données CSV  
- **Matplotlib** → génération des graphiques et tableaux  
- **Folium** → création de la carte interactive  
- **OS** → gestion des fichiers et dossiers
  
## Structure du projet
```
Projet_5G/
│
├── experimentations_5G.csv # Données source
│
├── script_5G.py # Script principal Python
│
├── Images/ # Dossier des Photos
│ ├── bar_Ile-de-France.png
│ ├── tableau_Normandie.png
│ └── ...
│
├── HTML/ #Dossier des pages HTML
│ ├── Carte.html
│ ├── Ile-de-France.html
│ ├── Normandie.html
│ └── ...
│
└── README.md # Documentation du projet
```

## Installation

1. Installe Python 3 si ce n’est pas déjà fait.  
2. Installe les bibliothèques nécessaires :
   ```bash
   pip install pandas matplotlib folium
   ```

## Utilisation

Lance le script avec la commande :
```bash
python SAE15.PY
```
Ouvre ensuite le fichier suivant dans ton navigateur :```Acceuil.html```

## Fonctionnement

Le programme va automatiquement :
- Créer le dossiers **`Images/`** (s’ils n’existent pas)
- Générer :
  - Des **graphiques et tableaux** dans `Images/`
  - Une **carte interactive** dans `HTML/`

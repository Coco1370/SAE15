# README — Bilingual Version (FR + EN)

## Choisir la langue / Choose your language  
[Version Française](#-version-française)  
[English Version](#-english-version)


# ————————————————————
#   FRENCH VERSION
# ————————————————————

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
│
├── PYTHON/ # Script principal Python
│ ├── experimentations_5G.csv # Données source
│ └── SAE15.py # Script principal Python
│
├── Images/ # Dossier des Photos
│ ├── bar_Ile-de-France.png
│ ├── tableau_Normandie.png
│ └── ...
│
│
├── CSS/ # Dossier Css pour les pages HTML
│ ├── Acceuil.css
│ └── Régions.css
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
cd ../SAE15/PYTHON
python SAE15.PY
```
Ouvre ensuite le fichier suivant dans ton navigateur :```Acceuil.html```

## Fonctionnement

Le programme va automatiquement :
- Créer le dossiers **`Images/`** (s’ils n’existent pas)
- Générer :
  - Des **graphiques et tableaux** dans `Images/`
  - Une **carte interactive** dans `HTML/`

### ———————————————————
###   ENGLISH VERSION
### ———————————————————

# Project: Visualization of 5G Experiments in France  

## Project Description

This project analyzes and visualizes 5G experiments conducted across France using an official CSV dataset (region, operator, frequencies, GPS coordinates, etc.).  
The Python script automatically generates:

- An **interactive map** with one marker per region  
- **Charts** and **tables** for each region  
- **HTML pages** dedicated to each region (e.g., `Ile-de-France.html`, `Normandie.html`)

## Technologies Used

- **Python 3**  
- **Pandas** – CSV data processing  
- **Matplotlib** – chart and table generation  
- **Folium** – interactive map creation  
- **OS** – file and directory handling  

## Project Structure

```
Projet_5G/
│
│
├── PYTHON/ # Script principal Python
│ ├── experimentations_5G.csv # Données source
│ └── SAE15.py # Script principal Python
│
├── Images/ # Dossier des Photos
│ ├── bar_Ile-de-France.png
│ ├── tableau_Normandie.png
│ └── ...
│
│
├── CSS/ # Dossier Css pour les pages HTML
│ ├── Acceuil.css
│ └── Régions.css
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

1. Install Python 3 if it is not already installed.  
2. Install dependencies:

```bash
pip install pandas matplotlib folium
```
## Usage 

Run the script :
```bash
cd ../SAE15/PYTHON
python SAE15.PY
```
Then open this file in your browser:```Acceuil.html```

## How it works

The program automatically:
- Creates the **`Images/`** directory if it does not already exist
- Generates:
  - **Charts and tables** inside `Images/`
  - An **interactive map** inside `HTML/`

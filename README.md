# Projet Semestre 4 - Interface d'Administration de Données

## Contexte du Projet
Ce projet, réalisé dans le cadre du semestre 4 du BUT (Parcours A), consiste à développer une application complète (Front-end et Back-end) permettant de visualiser, manipuler et assainir les données d'une base de données existante. L'objectif est de créer une interface d'administration robuste pour faciliter la gestion des données en vue d'une utilisation ultérieure (par ETL ou autre transformation).

---

## Objectifs
- **Front-end** : Créer une interface utilisateur intuitive pour visualiser et manipuler les données.
- **Back-end** : Développer une API RESTful pour gérer les requêtes et assurer la validité des données.
- **Base de données** : Connecter l'application à une base de données spécifique et permettre des opérations CRUD (Create, Read, Update, Delete).

---

## Fonctionnalités

### Front-end
- **Visualisation des données** :
  - Affichage du modèle des tables.
  - Affichage du contenu des tables.
- **Manipulation des données** :
  - Tri des données par un ou plusieurs attributs.
  - Filtrage des données sur un ou plusieurs attributs.
  - Modification d'une entrée existante.
  - Suppression d'une entrée.
  - Ajout de nouvelles entrées.
- **Import/Export des données** :
  - Envoi de données pour écraser le contenu d'une table.
  - Envoi de données pour ajouter à une table.
  - Initialisation de toute la base de données.
  - Extraction des données d'une table (complètes ou filtrées).

### Back-end (API)
- **Gestion des requêtes** :
  - Validation des paramètres pour chaque requête.
  - Conformité aux standards REST.
- **Configuration** :
  - Utilisation d'un fichier de configuration pour paramétrer la connexion à la base de données.
  - Lecture des variables d'environnement pour une meilleure sécurité.

---

## Barème d'Évaluation (20 points)

### Front-end (10 points)
- **Architecture (Composants, Services)** : 2 pts
- **Gestion des formulaires** : 2 pts
- **Typage** : 2 pts
- **Interface utilisateur** : 2 pts
- **Navigation** : 2 pts

### Back-end (10 points)
- **Respect des standards REST** : 3 pts
- **Modélisation** : 3 pts
- **Utilisation de Python** : 2 pts
- **Typage et documentation** : 2 pts

---

## Technologies Utilisées
- **Front-end** : [Indiquer les technologies utilisées, par exemple React, Angular, etc.]
- **Back-end** : [Indiquer les technologies utilisées, par exemple Flask, Django, etc.]
- **Base de données** : [Indiquer la base de données utilisée, par exemple MySQL, PostgreSQL, etc.]
- **Autres outils** : [Indiquer les outils supplémentaires, par exemple Swagger pour la documentation API, etc.]

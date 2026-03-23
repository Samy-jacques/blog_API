# Blog API (FastAPI)

Une API REST développée avec FastAPI permettant de gérer des articles (CRUD, recherche, filtrage).

---

# Installation

## 1. Cloner le projet

```bash
git clone <https://github.com/Samy-jacques/blog_API>
cd blog-api
```

## 2. Créer un environnement virtuel

```bash
python -m venv venv
```

### Activer l’environnement

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

## 3. Installer les dépendances

```bash
pip install fastapi uvicorn sqlalchemy
```

## 4. Lancer l’application

```bash
uvicorn main:app --reload
```

---

# Documentation API

Une fois le serveur lancé, accéder à :

http://127.0.0.1:8000/docs

Cette interface permet de tester les endpoints.

---

# Endpoints

## Créer un article

* POST `/api/articles`

### Exemple JSON:

```json
{
  "title": "Apprendre FastAPI",
  "author": "John",
  "content": "FastAPI est un framework moderne...",
  "category": "Tech",
  "tags": "python, fastapi"
}
```

---

## Récupérer tous les articles

* GET `/api/articles`

### Paramètres optionnels:

* skip : pagination
* limit : nombre d’articles
* category : filtrer par catégorie
* author : filtrer par auteur
* date : format YYYY-MM-DD

### Exemple:

```bash
GET /api/articles?category=Tech&date=2026-03-23
```

---

## Rechercher des articles

* GET `/api/articles/search?query=texte`

### Exemple:

```bash
GET /api/articles/search?query=python
```

---

## Récupérer un article par ID

* GET `/api/articles/{id}`

### Exemple:

```bash
GET /api/articles/1
```

---

## Modifier un article

* PUT `/api/articles/{id}`

### Exemple JSON:

```json
{
  "title": "Nouveau titre",
  "content": "Contenu mis à jour"
}
```

---

## Supprimer un article

* DELETE `/api/articles/{id}`

### Exemple:

```bash
DELETE /api/articles/1
```

### Réponse:

```json
{
  "message": "Article avec ID 1 supprime avec succes"
}
```

---

# Exemple d’utilisation avec cURL

## Créer un article

```bash
curl -X POST "http://127.0.0.1:8000/api/articles" \
-H "Content-Type: application/json" \
-d '{
  "title": "Test API",
  "author": "Admin",
  "content": "Ceci est un test",
  "category": "Tech",
  "tags": "test"
}'
```

---

## Rechercher un article

```bash
curl "http://127.0.0.1:8000/api/articles/search?query=test"
```

---

# Base de données

* SQLite utilisée : blog.db
* Création automatique au démarrage

---

# Technologies utilisées

* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

---

# Fonctionnalités

* CRUD complet
* Recherche par mot-clé
* Filtrage par catégorie, auteur et date
* Documentation Swagger intégrée
* Validation des données avec Pydantic

---

# Notes

* Les dates doivent être au format YYYY-MM-DD
* Les champs title, author et content sont obligatoires

---

# Auteur

Projet réalisé dans le cadre d’apprentissage de FastAPI.

# Job Aggregator – DevOps Project

Projet personnel de **job aggregator** développé avec **FastAPI**, containerisé avec **Docker**, et automatisé avec une **pipeline CI/CD GitHub Actions**.

---

## Description

Ce projet est une API qui agrège des offres d’emploi provenant de plusieurs sources :

- Remotive
- HelloWork
- Welcome to the Jungle (WTTJ)

L’API applique :
- un scoring des offres
- des filtres par localisation et source
- une sélection des offres pertinentes

---

## Stack technique

- Python 3.12
- FastAPI
- Uvicorn
- Docker
- Docker Compose
- Pytest
- GitHub Actions (CI/CD)
- Trivy (scan sécurité)

---


---

## Lancer le projet en local

### 1. Avec Python

```bash
pip install -r requirements.txt
uvicorn api:app --reload
```

API disponible sur :
```
http://localhost:8000
```

---

### 2. Avec Docker

```bash
docker build -t job-aggregator .
docker run -p 8000:8000 job-aggregator
```

---

### 3. Avec Docker Compose

```bash
docker compose up --build
```

---

## Lancer les tests

### Local

```bash
python -m pytest
```

### Dans Docker

```bash
docker compose run --rm job-aggregator python -m pytest
```

---

## CI/CD (GitHub Actions)

Pipeline automatisé :

1. Tests avec pytest
2. Build image Docker
3. Scan sécurité avec Trivy
4. Push image vers Docker Hub

Déclenchement :
- push sur `main`
- pull request sur `main`

---

## Variables d’environnement (GitHub Secrets)

```text
DOCKERHUB_USERNAME=your_username
DOCKERHUB_TOKEN=your_token
```

---

## Endpoints API

### GET /

```json
{ "status": "job-aggregator running" }
```

### GET /jobs

Retourne les offres filtrées et scorées.

### GET /stats

Retourne les statistiques des offres par source et localisation.

---

## Objectifs DevOps du projet

- Containerisation complète avec Docker
- Automatisation des tests
- CI/CD avec GitHub Actions
- Scan de sécurité des images (Trivy)
- Préparation à une architecture Kubernetes

---

## Améliorations possibles

- Ajout d’une base de données (PostgreSQL)
- Déploiement Kubernetes (Minikube / EKS)
- Monitoring (Prometheus / Grafana)
- Cache Redis
- Versioning des images Docker

---

## Auteur

Projet personnel DevOps – Saliha

---

## Licence

Projet personnel – usage éducatif
```


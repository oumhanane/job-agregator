 # Job Aggregator – DevOps Project

Projet personnel de **job aggregator** développé avec **FastAPI**, containerisé avec **Docker**, et automatisé avec une **pipeline CI/CD GitHub Actions**.

---

## Description

Ce projet est une application qui agrège des offres d’emploi provenant de plusieurs sources :

- Remotive  
- HelloWork  
- Welcome to the Jungle (WTTJ)

L’application expose :
- une API REST (FastAPI)
- une interface web simple (HTML/CSS)
- un moteur de scoring des offres
- des filtres par localisation et source

---

## Stack technique

- Python 3.12
- FastAPI
- Uvicorn
- HTML / CSS (UI simple)
- Docker
- Docker Compose
- Pytest
- GitHub Actions (CI/CD)
- Bandit (SAST)
- pip-audit (SCA)
- Trivy (scan sécurité container)

---

## Architecture


sources/ → scraping des jobs
core/ → scoring + filtres métier
api.py → API FastAPI
static/ → interface web (HTML/CSS)
tests/ → tests pytest
Dockerfile → containerisation
.github/ → CI/CD pipeline


---

## Lancer le projet en local

### 1. Avec Python

```bash
pip install -r requirements.txt
uvicorn api:app --reload

Application disponible sur :

http://localhost:8000
2. Interface Web

UI disponible sur :

http://localhost:8000/ui

Elle affiche les offres d’emploi sous forme simple (HTML/CSS).

3. Avec Docker
docker build -t job-aggregator .
docker run -p 8000:8000 job-aggregator
4. Avec Docker Compose
docker compose up --build
Lancer les tests
Local
python -m pytest
Dans Docker
docker compose run --rm job-aggregator python -m pytest
CI/CD (GitHub Actions)

Pipeline automatisé :

Tests avec pytest
Analyse SAST (Bandit)
Analyse SCA (pip-audit)
Build image Docker
Scan sécurité avec Trivy
Push image vers Docker Hub

Déclenchement :

push sur main
tags v*
Variables d’environnement (GitHub Secrets)
DOCKERHUB_USERNAME=your_username
DOCKERHUB_TOKEN=your_token
Endpoints API
GET /
{ "status": "job-aggregator running" }
GET /jobs

Retourne les offres filtrées et scorées.

GET /stats

Retourne les statistiques par source et localisation.

GET /ui

Interface web simple affichant les offres.

Objectifs DevOps du projet
Containerisation complète avec Docker
Automatisation des tests
CI/CD complet (tests + SAST + SCA + build + push)
Scan sécurité des images (Trivy)
Interface web simple (UI)
Préparation à une architecture Kubernetes
Améliorations possibles
Base de données PostgreSQL
Déploiement Kubernetes (Minikube / EKS)
Monitoring (Prometheus / Grafana)
Cache Redis
Versioning avancé des images Docker
UI plus avancée (React ou Vue)
Auteur

Projet personnel DevOps – Saliha

Licence

Projet personnel – usage éducatif
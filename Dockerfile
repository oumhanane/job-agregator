FROM python:3.12-slim

# Empêche Python de générer .pyc + logs bufferisés
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crée un user non-root (bonne pratique sécurité)
RUN useradd -m appuser

WORKDIR /app

# Installer dépendances système minimales (optionnel mais propre)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copier requirements en premier (cache pip optimisé)
COPY requirements.txt .

# Installer dépendances avec cache pip optimisé
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code
COPY . .

# Donner les droits au user non-root
RUN chown -R appuser:appuser /app

# Passer en user non-root
USER appuser

# Healthcheck Docker (important prod)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

# Port exposé
EXPOSE 8000

# Lancement app
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
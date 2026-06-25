FROM python:3.12-slim

WORKDIR /app

# dépendances système minimales
RUN apt-get update && apt-get install -y curl

# copier le projet
COPY . .

# installer dépendances python
RUN pip install --no-cache-dir fastapi uvicorn requests playwright

# installer browsers playwright
RUN python -m playwright install --with-deps

# exposer API
EXPOSE 8000

# lancer API
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
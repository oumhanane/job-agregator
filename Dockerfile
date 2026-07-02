FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ------------------------
# Create non-root user
# ------------------------
RUN useradd -m appuser

WORKDIR /app

# ------------------------
# System deps (MINIMAL)
# ------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# 🔥 IMPORTANT : upgrade security fixes early
RUN apt-get update && apt-get upgrade -y

# ------------------------
# Python deps FIRST (cache layer optimization)
# ------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# ------------------------
# App source
# ------------------------
COPY . .

# ------------------------
# Permissions
# ------------------------
RUN chown -R appuser:appuser /app

USER appuser

# ------------------------
# Healthcheck
# ------------------------
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
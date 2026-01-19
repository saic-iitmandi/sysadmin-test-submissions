FROM python:3.11-slim AS base
WORKDIR /app

# Install build deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY STAC/backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY STAC/backend/ ./

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["gunicorn","STAC.wsgi:application","--bind","0.0.0.0:8000","--workers","3","--config","gunicorn.conf.py"]

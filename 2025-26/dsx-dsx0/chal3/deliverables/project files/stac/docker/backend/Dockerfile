# ----------------------------
# STAC Backend - Django
# ----------------------------

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Workdir for Django app
WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY app/backend/requirements.txt /app/requirements.txt

# Install Python deps
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy Django backend code
COPY app/backend /app

# Copy startup script to root (IMPORTANT)
COPY docker/backend/start.sh /start.sh

# Make it executable
RUN chmod +x /start.sh

EXPOSE 8000

CMD ["sh", "/start.sh"]

# backend/Dockerfile

FROM python:3.12-slim

# 1. The Magic Line: Copy 'uv' directly from its own image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. Use uv to install dependencies
# --system flag tells uv to install into the container's main Python, not a venv
COPY requirements.txt /app/
RUN uv pip install --system -r requirements.txt --index-strategy unsafe-best-match

COPY . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "STAC.wsgi:application"]
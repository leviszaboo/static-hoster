FROM python:3.11-slim AS base

WORKDIR /api

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONFAULTHANDLER=1

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# =========================================
# Development stage
# =========================================
FROM base AS dev

ENV FLASK_ENV=development \
    PYTHONPATH=/

EXPOSE 5001

CMD ["sh", "-c", "cd app && flask --app manage.py run --cert=certs/cert.pem\
 --key=certs/key.pem --host=0.0.0.0 --port=5001"]
# =========================================
# Production stage
# =========================================
FROM base AS prod

ENV FLASK_ENV=production

EXPOSE 8000

CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8000", "wsgi:app"]
#!/usr/bin/env bash
# scripts/start.sh

if [ -f api-service/.env ]; then
  export $(grep -v '^#' api-service/.env | xargs)
else
  echo "Error: api-service/.env file not found."
  exit 1
fi

if [ -z "$POSTGRES_PASSWORD" ]; then
  echo "Error: POSTGRES_PASSWORD is not set in the api-service/.env file."
  exit 1
fi

# Run Docker Compose
docker-compose up -d
# SecureTask API

FastAPI backend project with JWT authentication, task CRUD endpoints, pagination, Alembic migrations, Docker Compose, and a simple development seed flow.

## Features
- FastAPI REST API
- JWT-based authentication
- Task CRUD endpoints with pagination
- PostgreSQL + SQLAlchemy
- Alembic migrations
- Docker Compose setup
- Health check endpoint
- Basic test example with environment-safe defaults

## Tech Stack
- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Docker / Docker Compose

## Run with Docker
```bash
cp .env.example .env
docker compose up --build
```

API: http://localhost:8000  
Docs: http://localhost:8000/docs

## Environment Variables
Create a `.env` file from `.env.example` and update values as needed.

Important variables:
- `DATABASE_URL`
- `JWT_SECRET`
- `JWT_ALG`
- `ACCESS_TOKEN_MINUTES`
- `CORS_ORIGINS`
- `DEMO_USER_EMAIL`
- `DEMO_USER_PASSWORD`

## Demo Seed User
A demo user is created only if both of these values are set in `.env`:
- `DEMO_USER_EMAIL`
- `DEMO_USER_PASSWORD`

This keeps credentials out of the source code while still allowing an easy local demo setup.

## Run Tests
```bash
pytest
```

The included test configuration sets safe test defaults so the basic test suite can run without a manually created `.env` file.

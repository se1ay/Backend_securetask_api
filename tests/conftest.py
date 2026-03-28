import os

os.environ.setdefault("APP_ENV", "test")
os.environ.setdefault("DATABASE_URL", "sqlite:///./test.db")
os.environ.setdefault("JWT_SECRET", "test-secret")
os.environ.setdefault("JWT_ALG", "HS256")
os.environ.setdefault("ACCESS_TOKEN_MINUTES", "120")
os.environ.setdefault("CORS_ORIGINS", "http://localhost:3000")

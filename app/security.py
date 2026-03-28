from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from app.config import settings

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(pw: str) -> str:
    return pwd.hash(pw)

def verify_password(pw: str, hashed: str) -> bool:
    return pwd.verify(pw, hashed)

def create_access_token(subject: str):
    exp = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_minutes)
    token = jwt.encode({"sub": subject, "exp": exp}, settings.jwt_secret, algorithm=settings.jwt_alg)
    return token, settings.access_token_minutes * 60

def decode_token(token: str) -> str:
    payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_alg])
    return payload["sub"]

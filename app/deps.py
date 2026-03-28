from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.security import decode_token
from app.db.models import User

oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2)) -> User:
    try:
        email = decode_token(token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    u = db.query(User).filter(User.email == email).first()
    if not u:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return u

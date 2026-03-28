from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import User
from app.schemas import LoginIn, TokenOut
from app.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=TokenOut)
def login(payload: LoginIn, db: Session = Depends(get_db)):
    u = db.query(User).filter(User.email == payload.email).first()
    if not u or not verify_password(payload.password, u.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token, expires_in = create_access_token(subject=u.email)
    return TokenOut(token=token, expires_in=expires_in)

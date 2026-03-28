from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import User
from app.security import hash_password
from app.config import settings


def main():
    if not settings.demo_user_email or not settings.demo_user_password:
        print("Skipping demo user seed: DEMO_USER_EMAIL / DEMO_USER_PASSWORD not set.")
        return

    db: Session = SessionLocal()
    try:
        u = db.query(User).filter(User.email == settings.demo_user_email).first()
        if not u:
            db.add(
                User(
                    email=settings.demo_user_email,
                    password_hash=hash_password(settings.demo_user_password),
                )
            )
            db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    main()

from sqlalchemy.orm import Session

from app.db.models.user import User


class UserRepository:
    def get_by_mailci(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def get_by_id(self, db: Session, id: int):
        return db.query(User).filter(User.id == id).filter()

    def create(self, db: Session, email: str, password: str):
        user = User(email=email, password=password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

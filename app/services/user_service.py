from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def register(self, db: Session, user: UserCreate):
        """
        We write business login rulse to avoid duplicate route and ...
        Business rule:
        - Email must be unique
        - Password must be hashed
        """
        if self.repo.get_by_email(db, user.email):
            raise ValueError("User already exists")

        hashed_password = hash_password(user.password)
        return self.repo.create(db, user.email, hashed_password)

    def authenticate(self, db: Session, email: str, password: str):
        """
        Business rule:
        - User must exist
        - Password must match
        """
        user = self.repo.get_by_email(db, email)
        if not user:
            return None

        if not verify_password(password, user.password):
            return None

        return user

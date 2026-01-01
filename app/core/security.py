# Generate a JWT
# user sends to your API to prove who they are without having to send their password with every request
# from datetime import datetime, timedelta
# ==> the datetime.utcnow() is  deprecated as of Python 3.12 and scheduled for removal in a future version
from datetime import datetime, timedelta, timezone

from argon2 import PasswordHasher
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from sqlalchemy.orm.descriptor_props import DescriptorProperty

from app.core.config import settings
from app.db.session import SessionLocal, get_db
from app.repositories.user_repo import UserRepository

# =====argon2 password hande=====
pwd_hansher = PasswordHasher()


# ===== Oauth2 scheme for Fastapi =====
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# -------------------------
# Password hashing
# -------------------------
def hash_password(password: str) -> str:
    return pwd_hansher.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    try:
        return pwd_hansher.verify(hashed, plain)
    except Exception:
        return False


# -------------------------
# JWT
# -------------------------
def create_access_token(subject: str) -> str:
    # use universal time zone and add 30 minute for expire
    # example: creation at 4:00PM , if users send at 4:15 it allowed , if 4:31 it reject
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


# -------------------------
# Auth dependency
# -------------------------
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )
        user_id: str | None = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = UserRepository().get_by_id(db, int(user_id))
    if not user:
        raise credentials_exception

    return user

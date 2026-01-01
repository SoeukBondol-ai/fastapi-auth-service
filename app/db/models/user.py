from enum import unique

from sqlalchemy import Column, Integer, String, true

from app.db.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=False)

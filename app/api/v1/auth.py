# This code is just authentication actions only
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.db.session import get_db
from app.schemas.user import Token, UserLogin
from app.services.user_service import UserService

router = APIRouter()
service = User


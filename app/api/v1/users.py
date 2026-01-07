from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.db.session import get_db
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.core.security import get_current_user

router = APIRouter()
service = UserService()

@router.post("/", response_model=UserRead)
def create_user(
    user:UserCreate,
    db:Session = Depends(get_db)
):
    return service.register(db,user)

@router.get("/me", response_model=UserRead)
def read_me(current_user=Depends(get_current_user)):
    return current_user
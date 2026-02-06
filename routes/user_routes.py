from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db
from repositories.user_repo import UserRepo
from schemaS.user_schemas import userschema


router = APIRouter()

@router.post("/signup")
def signup(db:Session = Depends(get_db)):
    user_repo = UserRepo(db)
    user_repo.add_user(user(user))
    return {"message": "User signup successfully"}

@router.post("/login")
def login():
    return {"message": "User login successfully"}
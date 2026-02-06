from fastapi import APIRouter

router = APIRouter()

@router.post("/signup")
def signup():
    return {"message": "User signup successfully"}

@router.post("/login")
def login():
    return {"message": "User login successfully"}
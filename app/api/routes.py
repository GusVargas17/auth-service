from fastapi import APIRouter, HTTPException
from app.services.auth_service import register_user, login_user
from app.repositories.user_repository import get_all_users

router = APIRouter()

@router.post("/create-user")
def create_user_endpoint(email: str, password: str):
    try:
        return register_user(email, password)
    except Exception:
        raise HTTPException(status_code=409, detail="Email already exists")

@router.post("/login")
def login_endpoint(email: str, password: str):
    result = login_user(email, password)

    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return result

@router.get("/users")
def users():
    return {"users": get_all_users()}
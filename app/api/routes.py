from fastapi import APIRouter, HTTPException
from app.services.auth_service import register_user, login_user
from app.repositories.user_repository import get_all_users, get_user_by_email
from app.schemas.auth_schema import RegisterRequest, LoginRequest

router = APIRouter()

@router.post("/create-user")
def create_user_endpoint(data: RegisterRequest):
    try:
        return register_user(data.email, data.password)
    except Exception:
        raise HTTPException(status_code=409, detail="Email already exists")

@router.post("/login")
def login_endpoint(data: LoginRequest):
    result = login_user(data.email, data.password)

    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return result

@router.get("/users")
def users(email: str = None):
    if email:
        return {"user": get_user_by_email(email)}
    return {"users": get_all_users()}
from fastapi import APIRouter, HTTPException, Header
from app.services.auth_service import register_user, login_user
from app.repositories.user_repository import get_all_users, get_user_by_email
from app.schemas.auth_schema import RegisterRequest, LoginRequest
from app.core.security.jwt_handler import verify_token

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
def users(email: str = None, authorization: str = Header(None)):

    if not authorization:
        raise HTTPException(status_code=401, detail="Token required")

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")

    token = authorization.split(" ")[1]
    payload = verify_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    if email:
        return {"user": get_user_by_email(email)}

    return {"users": get_all_users()}
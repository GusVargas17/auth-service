from fastapi import APIRouter, HTTPException, Header, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.services.auth_service import register_user, login_user
from app.repositories.user_repository import get_all_users, get_user_by_email
from app.schemas.auth_schema import RegisterRequest, LoginRequest
from app.core.security.jwt_handler import verify_token

router = APIRouter()
security = HTTPBearer()

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
def users(
    email: str = None,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials
    payload = verify_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    if email:
        return {"user": get_user_by_email(email)}

    return {"users": get_all_users()}
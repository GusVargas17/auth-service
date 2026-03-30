from fastapi import APIRouter, HTTPException, Depends
from app.services.auth_service import register_user, login_user
from app.repositories.user_repository import get_all_users, get_user_by_email, get_user_by_id
from app.schemas.auth_schema import RegisterRequest, LoginRequest
from app.core.security.dependencies import get_current_user

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
def users(
    email: str = None,
    current_user: dict = Depends(get_current_user)
):

    if email:
        user = get_user_by_email(email)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return {"user": user}

    return {"users": get_all_users()}

@router.get("/me")
def get_me(current_user: dict = Depends(get_current_user)):
    user_id = int(current_user["sub"])

    user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"user": user}
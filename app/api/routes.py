from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.services.auth_service import register_user, login_user
from app.services.user_service import (
    get_all_users_service,
    get_user_by_id_service
)
from app.schemas.auth_schema import RegisterRequest, LoginRequest
from app.schemas.user_schema import UserResponse
from app.core.security.dependencies import get_current_user, require_role

router = APIRouter()

@router.post("/create-user")
def create_user_endpoint(data: RegisterRequest):
    try:
        return register_user(data.email, data.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=409, detail="Email already exists")

@router.post("/login")
def login_endpoint(data: LoginRequest):
    result = login_user(data.email, data.password)

    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return result

@router.get("/users", response_model=List[UserResponse])
def users(current_user: dict = Depends(require_role("admin"))):
    return get_all_users_service()

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(
    user_id: int,
    current_user: dict = Depends(get_current_user)
):
    if current_user["sub"] != str(user_id) and current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")

    user = get_user_by_id_service(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.get("/me", response_model=UserResponse)
def get_me(current_user: dict = Depends(get_current_user)):
    user_id = int(current_user["sub"])

    user = get_user_by_id_service(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user
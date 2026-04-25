from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security.jwt_handler import verify_token
from app.core.db import get_connection

def get_db():
    return get_connection()

security = HTTPBearer()

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    payload = verify_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return payload

def require_role(required_role: str):
    def role_checker(current_user: dict = Depends(get_current_user)):

        user_role = current_user.get("role")

        if user_role != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")

        return current_user
    
    return role_checker
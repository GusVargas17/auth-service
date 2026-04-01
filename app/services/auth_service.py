from app.repositories.user_repository import (
    create_user, 
    get_user_with_password,
    get_all_users,
    get_user_by_email,
    get_user_by_id
)
from app.core.security.jwt_handler import create_access_token
from app.core.security.password_handler import hash_password, verify_password

def register_user(email: str, password: str):
    hashed_password = hash_password(password)

    create_user(email, hashed_password)
    
    return {"message": "User created"}

def login_user(email: str, password: str):
    user = get_user_with_password(email)

    if not user:
        return None
    
    stored_password = user[2]

    if not verify_password(password, stored_password):
        return None

    token = create_access_token({"sub": str(user[0])})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

def map_user(user_tuple):
    return {
        "id": user_tuple[0],
        "email": user_tuple[1],
        "created_at": user_tuple[2]
    }

def get_all_users_service():
    users = get_all_users()
    return [map_user(user) for user in users]

def get_user_by_email_service(email: str):
    user = get_user_by_email(email)

    if not user:
        return None

    return map_user(user)

def get_user_by_id_service(user_id: int):
    user = get_user_by_id(user_id)

    if not user:
        return None

    return map_user(user)
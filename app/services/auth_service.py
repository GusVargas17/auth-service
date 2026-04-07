from app.repositories.user_repository import create_user,get_user_with_password 
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
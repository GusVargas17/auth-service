import bcrypt
from app.repositories.user_repository import create_user, get_user_by_email

def register_user(email: str, password: str):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    create_user(email, hashed_password)
    
    return {"message": "User created"}

def login_user(email: str, password: str):
    user = get_user_by_email(email)

    if not user:
        return None
    
    stored_password = user[2]

    if bcrypt.checkpw(password.encode(), stored_password.encode()):
        return {"message": "Login successful"}

    return None
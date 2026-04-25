from app.repositories.user_repository import create_user,get_user_with_password
from app.core.db import get_connection
from app.core.security.jwt_handler import create_access_token, create_refresh_token
from app.core.security.password_handler import hash_password, verify_password

def register_user(email: str, password: str, conn=None):
    own_conn = False

    if conn is None:
        conn = get_connection()
        own_conn = True

    try:
        if " " in password:
            raise ValueError("Password must not contain spaces")

        if password.isalpha():
            raise ValueError("Password must contain numbers or symbols")

        hashed_password = hash_password(password)

        create_user(email, hashed_password, role="user", conn=conn)

        if own_conn:
            conn.commit()

        return {"message": "User created"}

    except Exception:
        if own_conn:
            conn.rollback()
        raise

    finally:
        if own_conn:
            conn.close()

def login_user(email: str, password: str, conn):
    user = get_user_with_password(email, conn)

    if not user:
        return None

    if not verify_password(password, user[2]):
        return None

    payload = {
        "sub": str(user[0]),
        "role": user[3]
    }

    return {
        "access_token": create_access_token(payload),
        "refresh_token": create_refresh_token(payload),
        "token_type": "bearer"
    }
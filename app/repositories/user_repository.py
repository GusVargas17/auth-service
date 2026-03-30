from app.core.db import get_connection

def create_user(email: str, password: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, password)
        )

        conn.commit()

    finally:
        cursor.close()
        conn.close()

def get_user_by_email(email:str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT id, email, password FROM users WHERE email = %s",
            (email,)
        )
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def get_user_by_id(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, email, created_at FROM users WHERE id = %s",
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, email, created_at FROM users;")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def map_user(user_tuple):
    return {
        "id": user_tuple[0],
        "email": user_tuple[1],
        "created_at": user_tuple[2]
    }
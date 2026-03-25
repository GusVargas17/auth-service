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

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, email, created_at FROM users;")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
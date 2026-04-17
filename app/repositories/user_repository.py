from app.core.db import get_connection

def create_user(email: str, password: str, role: str, conn=None):
    own_conn = False

    if conn is None:
        conn = get_connection()
        own_conn = True

    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (email, password, role) VALUES (%s, %s, %s)",
            (email, password, role)
        )

        if own_conn:
            conn.commit()

    finally:
        cursor.close()
        if own_conn:
            conn.close()

def get_user_by_email(email: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT id, email, created_at FROM users WHERE email = %s",
            (email,)
        )
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def get_user_with_password(email:str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT id, email, password, role FROM users WHERE email = %s",
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
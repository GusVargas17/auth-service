import bcrypt
from fastapi import FastAPI
from fastapi import HTTPException
from db import get_connection
from psycopg2 import errors

app = FastAPI()

@app.get("/")
def test_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT 1;")
        result = cursor.fetchone()

        return {"result": result}
    
    except Exception as e:
        return {"error": str(e)}
    
    finally:
        cursor.close()
        conn.close()

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

@app.get("/create-table")
def create_table():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        conn.commit()

        return {"message": "Users table created"}

    except Exception as e:
        return {"error": str(e)}
    
    finally:
        cursor.close()
        conn.close()

@app.post("/create-user")
def create_user(email: str, password: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        hashed_password = hash_password(password)

        cursor.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, hashed_password)
        )

        conn.commit()

        return {"message": "User created"}
    
    except errors.UniqueViolation:
        conn.rollback()
        return {"error": "Email already exists"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cursor.close()
        conn.close()

@app.get("/users")
def get_users():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, email, created_at FROM users;")
        users = cursor.fetchall()

        return {"users": users}

    except Exception as e:
        return {"error": str(e)}

    finally:
        cursor.close()
        conn.close()

@app.post("/login")
def login(email: str, password: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT password FROM users WHERE email = %s",
            (email,)
        )

        user = cursor.fetchone()

        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        stored_password = user[0]

        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            return {"message": "Login successful"}
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()
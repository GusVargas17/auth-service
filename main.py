from fastapi import FastAPI
from db import get_connection

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

        cursor.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, password)
        )

        conn.commit()

        return {"message": "User created"}

    except Exception as e:
        return {"error": str(e)}

    finally:
        cursor.close()
        conn.close()
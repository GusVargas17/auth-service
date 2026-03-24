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
from fastapi.testclient import TestClient
from main import app
import pytest
from app.core.db import get_connection

@pytest.fixture(autouse=True)
def clean_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users;")
    conn.commit()
    cursor.close()
    conn.close()

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def create_user(client):
    def _create_user(email="test@test.com", password="1234567a"):
        from app.services.auth_service import register_user
        return register_user(email, password)
    return _create_user

@pytest.fixture
def get_token(client, create_user):
    def _get_token(email="test@test.com", password="1234567a"):
        response = client.post("/login", json={
            "email": email,
            "password": password
        })
        return response.json()["access_token"]
    return _get_token

@pytest.fixture
def make_admin():
    def _make_admin(email):
        from app.core.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE users SET role = 'admin' WHERE email = %s",
            (email,)
        )

        conn.commit()
        cursor.close()
        conn.close()

    return _make_admin
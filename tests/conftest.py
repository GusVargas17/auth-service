from fastapi.testclient import TestClient
from main import app
import pytest
from app.core.db import get_connection
from app.core.security.dependencies import get_db

@pytest.fixture
def db_connection():
    conn = get_connection()
    conn.autocommit = True
    
    yield conn

    conn.rollback() 
    conn.close()

@pytest.fixture(autouse=True)
def clean_database(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM users;") 
    db_connection.commit()
    cursor.close()

@pytest.fixture
def client(db_connection):
    def override_get_db():
        return db_connection
    
    app.dependency_overrides[get_db] = override_get_db

    client = TestClient(app)

    yield client

    app.dependency_overrides.clear()

@pytest.fixture
def create_user(db_connection):
    def _create_user(email="test@test.com", password="1234567a"):
        from app.services.auth_service import register_user
        return register_user(email, password, conn=db_connection)
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
def make_admin(db_connection):
    def _make_admin(email):
        cursor = db_connection.cursor()
        cursor.execute(
            "UPDATE users SET role = 'admin' WHERE email = %s",
            (email,)
        )
    return _make_admin
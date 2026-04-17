from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login_success():
    client.post("/create-user", json={
        "email": "test@test.com",
        "password": "1234567a"
    })

    response = client.post("/login", json={
        "email": "test@test.com",
        "password": "1234567a"
    })

    assert response.status_code == 200

    data =  response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid():
    response = client.post("/login", json={
        "email": "fake@test.com",
        "password": "wrong"
    })

    assert response.status_code == 401
from fastapi.testclient import TestClient
from main import app
import time

def test_login_success(client, create_user):
    create_user("test@test.com", "1234567a")

    response = client.post("/login", json={
        "email": "test@test.com",
        "password": "1234567a"
    })

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid(client):
    response = client.post("/login", json={
        "email": "fake@test.com",
        "password": "wrong"
    })

    assert response.status_code == 401

def test_token_expiration(client, create_user):
    create_user("test@test.com", "1234567a")

    response = client.post("/login", json={
        "email": "test@test.com",
        "password": "1234567a"
    })

    token = response.json()["access_token"]

    time.sleep(2)

    response = client.get(
        "/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 401
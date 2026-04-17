from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_token():
    client.post("/create-user", json={
        "email": "user@test.com",
        "password": "1234567a"
    })

    response = client.post("/login", json={
        "email": "user@test.com",
        "password": "1234567a"
    })

    return response.json()["access_token"]

def test_users_no_token():
    response = client.get("/users")

    assert response.status_code == 403 or response.status_code == 401

def test_users_requires_admin():
    token = get_token()

    response = client.get(
        "/users",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 403

def test_user_cannot_access_other_user():
    # user1
    client.post("/create-user", json={
        "email": "user1@test.com",
        "password": "1234567a"
    })

    token1 = client.post("/login", json={
        "email": "user1@test.com",
        "password": "1234567a"
    }).json()["access_token"]

    # user2
    client.post("/create-user", json={
        "email": "user2@test.com",
        "password": "1234567a"
    })

    response = client.get(
        "/users/2",
        headers={"Authorization": f"Bearer {token1}"}
    )

    assert response.status_code == 403

def test_users_with_admin():
    email = "admin@test.com"

    client.post("/create-user", json={
        "email": email,
        "password": "1234567a"
    })

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

    response = client.post("/login", json={
        "email": email,
        "password": "1234567a"
    })

    token = response.json()["access_token"]

    response = client.get(
        "/users",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
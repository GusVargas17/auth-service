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

def test_users_requires_admin(client, get_token):
    token = get_token()

    response = client.get(
        "/users",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 403

def test_user_cannot_access_other_user(client, create_user, get_token):
    # user1
    create_user("user1@test.com", "1234567a")
    token1 = get_token("user1@test.com", "1234567a")

    # user2
    create_user("user2@test.com", "1234567a")

    response = client.get(
        "/users/2",
        headers={"Authorization": f"Bearer {token1}"}
    )

    assert response.status_code == 403

def test_users_with_admin(client, get_token, make_admin):
    email = "admin@test.com"

    token = get_token(email)
    make_admin(email)

    response = client.get(
        "/users",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
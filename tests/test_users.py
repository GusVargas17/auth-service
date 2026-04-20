from fastapi.testclient import TestClient
from main import app

def test_users_no_token(client):
    response = client.get("/users")

    assert response.status_code == 403 or response.status_code == 401

def test_users_requires_admin(client, create_user, get_token):
    create_user("test@test.com", "1234567a")
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

def test_users_with_admin(client,create_user, get_token, make_admin):
    email = "admin@test.com"

    create_user(email, "1234567a")
    make_admin(email)
    token = get_token(email)

    response = client.get(
        "/users",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
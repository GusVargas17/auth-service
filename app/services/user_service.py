from app.repositories.user_repository import (
    get_all_users,
    get_user_by_email,
    get_user_by_id
)

def map_user(user_tuple):
    return {
        "id": user_tuple[0],
        "email": user_tuple[1],
        "created_at": user_tuple[2]
    }

def get_all_users_service(conn):
    users = get_all_users(conn)
    return [map_user(user) for user in users]

def get_user_by_email_service(email: str, conn):
    user = get_user_by_email(email, conn)

    if not user:
        return None

    return map_user(user)

def get_user_by_id_service(user_id: int, conn):
    user = get_user_by_id(user_id, conn)

    if not user:
        return None

    return map_user(user)
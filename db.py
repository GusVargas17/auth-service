import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="auth_service",
        user="gus",
        password="123456",
        host="localhost",
        port="5432",
        connect_timeout=3
    )
import psycopg2
import os

DB_NAME = os.getenv("DB_NAME", "auth_service")

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user="gus",
        password="123456",
        host="localhost",
        port="5432",
        connect_timeout=3
    )
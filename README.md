# Auth Service

A backend authentication service built with FastAPI and PostgreSQL, designed with clean architecture principles and production-oriented practices.

---

## Features

- User registration with hashed password (bcrypt)
- User login with JWT authentication.
- Protected routes using Bearer token.
- Retrieve current authenticated user ('/me')
- List and retrieve users
- Clean architecture (API -> Service -> Repository)
- Input validation with Pydantic
- Response standardization using response model

## Architecture

The project follows a layered architecture

API layer (routes) -> Service layer (business logic) -> Repository layer (database access) -> Database (PostgreSQL)

### Responsibilities

- **API layer**: Handles HTTP request and response
- **Service layer**: Contains businnes logic and data transformation
- **Repository layer**: Executes SQL queries and interacts with the database
- **Core**: Shared logic (JWT, password hashing, dependencies)

---

## Project Structure

    app/
    ├── api/
    │ └── routes.py
    ├── services/
    │ └── auth_service.py
    ├── repositories/
    │ └── user_repository.py
    ├── schemas/
    │ ├── auth_schema.py
    │ └── user_schema.py
    ├── core/
    │ ├── security/
    │ │ ├── jwt_handler.py
    │ │ ├── password_handler.py
    │ │ └── dependencies.py
    │ └── database.py
    main.py

---


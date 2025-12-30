# Auth Service

Auth Service is a backend authentication and authorization service designed as an independent component, focused on clearly and securely resolving identity and access management within a system. The project prioritizes clean architecture, separation of responsibilities and real good backend practices. Does not include frontend: exposes an API designed to be consumed by any client (another backend, a web or mobile application). This repository serves as a solid, extensible foundation for understanding how to build a well-made authentication service, with a focus on maintainability, security, and technical criteria.

---

## Purpose

The purpose of this project is to design and implement a well-structured authentication and authorization service.


It serves as:
- A standalone backend component
- A reference implementation of clean architecture
- A practical exercise in building production-oriented infrastructure

The focus is on clarity, correctness, and technical discipline.

---

## Responsibilities

This service is responsible for:
- Managing users and credentials
- Authenticating identities
- Issuing and validating access tokens
- Revoking tokens when access must be terminated
- Enforcing authorization rules through roles and permissions

Anything outside the identity and access domain is intentionally excluded.

---


## Architecture Overview

The project follows a layered architecture with strict separation of concerns:

- **Domain**: core business rules and domain models
- **Use Cases / Services**: application workflows and orchestration
- **Persistence**: database access and repositories
- **API**: HTTP interface
- **Core**: configuration, security, and cross-cutting concerns

The domain layer is framework-agnostic. Infrastructure and frameworks remain at the edges.

---

## Project Structure

```
auth-service/
├── app/
│   ├── api/
│   │   ├── routers/
│   │   │   ├── auth.py               # Authentication endpoints (login, refresh, logout)
│   │   │   ├── users.py              # User management endpoints (create, update, retrieve)
│   │   │   └── health.py             # Service health and readiness checks
│   │   │
│   │   └── dependencies.py           # FastAPI dependency injection (auth, db sessions)
│   │   └── errors.py                 #  HTTP-level error mapping and API exceptions
│   │
│   ├── core/
│   │   ├── config.py                 # Environment configuration and application settings
│   │   ├── security/                 # Security mechanisms and enforcement utilities
│   │   │   ├── jwt.py                # JWT creation, validation, and decoding
│   │   │   ├── passwords.py          # Password hashing and verification
│   │   │   ├── permissions.py        # Authorization rules and permission checks
│   │   │   ├── rate_limit.py         # Rate limiting and abuse prevention logic
│   │   └── constants.py              # Global constants and security-related defaults
│   │   └── exceptions.py             # Core application-level exceptions
│   │   └── logging.py                # Logging configuration
│   │
│   ├── domain/
│   │   └── entities/
│   │   |    ├── user.py              # User domain entity
│   │   |    ├── role.py              # Role domain entity
│   │   |    └── token.py             # Token domain entity / value representation
│   │   └── values_objects/
│   │   |     ├── email.py            # Email value object with validation rules
│   │   |     ├── password.py         # Password value object and invariants
│   │   └── exceptions.py             # Domain-specific business rule violations
|   |
│   ├── schemas/
│   │   ├── user.py                   # User request and response schemas
│   │   ├── auth.py                   # Authentication-related schemas
│   │   └── token.py                  # Token input/output schemas
│   │
│   ├── persistence/
│   │   ├── models/
│   │   |     ├── role.py             # Database role model (ORM)
│   │   |     ├── token.py            # Database token model (ORM)
│   │   |     ├── user.py             # Database user model (ORM)
│   │   ├── repositories/
│   │   │   ├── user_repository.py    # User data access abstraction
│   │   │   └── token_repository.py   # Token persistence and lookup logic
│   │   │   └── role_repository.py    # Role and permission persistence
│   │   │
│   │   └── migrations/               # Database migrations
│   │   └── database.py               # Database setup
│   |
│   ├── use_cases/
│   │     ├── authenticate_user.py     # Authenticate user credentials
│   │     ├── create_user.py           # User creation workflow
│   │     ├── issue_token.py           # Token issuance logic
│   │     ├── refresh_token.py         # Token refresh workflow
│   │     └── revoke_token.py          # Token revocation (logout) logic
│   │
│   ├── main.py                        # Application entry point
│   └── __init__.py
│
├── tests/
│   ├── unit/                          # Domain and use case unit tests
│   └── integration/                   # Persistence and API integration tests
│   └── conftest.py                    # Shared test fixtures and configuration
│
├── scripts/
│   └── create_admin.py                # Initial administrator bootstrap script
│   └── rotate_keys.py                 # Security key rotation utility
│
├── .env.example                       # Environment variables template
├── .gitignore
├── pyproject.toml                     # Project metadata and dependency management
└── README.md
```

---

## Technology Stack

- **Python 3.11+** 
- **FastAPI** — high-performance web framework
- **PostgreSQL** — primary relational database
- **SQLAlchemy** — ORM and database interaction
- **Alembic** — database migrations
- **Pydantic** — database migrations
- **JWT (JSON Web Tokens)** — stateless authentication
- **Passlib / bcrypt** — stateless authentication
- **Pytest** — automated testing

The stack was chosen for reliability, clarity, and real-world backend relevance.

---
# Auth Service Notes

---

## Database

- `conn.rollback()` is required after a failed transaction
- Without rollback, the connection remains in an invalid state

### psycopg2
- `cursor()` → Creates a cursor to execute SQL queries
- `execute()` → Runs a SQL query
- `fetchone()` → Retrieves a single row
- `fetchall()` → Retrieves all rows
- `commit()` → Persists changes
- `rollback()` → Reverts changes on failure

---

## HTTP

- HTTP Status Code → Indicates result of a request
- `200 OK` → Request successful
- `201 Created` → Resource created successfully
- `401 Unauthorized` → Invalid or missing authentication
- `404 Not Found` → Resource does not exist
- `409 Conflict` → Conflict with current state (e.g. duplicate data)
- `500 Internal Server Error` → Unexpected server failure

---

## FastAPI

- Request → Data sent by client
- Endpoint → Function triggered by a request
- GET → Retrieve data
- POST → Create data
- `@app.get()` → Defines GET endpoint
- `@app.post()` → Defines POST endpoint
- `Depends()` → Injects dependencies (e.g. authentication, services)

---

## Security

- Passwords are hashed using bcrypt
- Never store passwords in plain text
- JWT is used for stateless authentication
- JWT payload includes:
  - `sub` → user identifier
  - `exp` → expiration timestamp

---

## Errors

- `"password authentication failed"` → Incorrect database credentials
- `UniqueViolation` → Duplicate value in UNIQUE column
- `JWT ERROR: Subject must be a string` → `sub` must be string

---

## Architecture

### Concepts
- Clean Architecture → Separation of responsibilities into layers
- Layer → Logical boundary in the system
- Separation of Concerns → Each component has a single responsibility
- Abstraction → Hide implementation details

---

### Layers

- API Layer → Handles HTTP requests/responses
- Service Layer → Contains business logic
- Repository Layer → Handles database access
- Core Layer → Shared infrastructure (e.g. security, DB)

---

### Flow

- Request → API → Service → Repository → Database  
- Response → Repository → Service → API → Client

---

## Principles

- Business logic must not depend on frameworks or databases
- Depend on abstractions, not implementations
- Keep layers independent
- Avoid mixing responsibilities

---

## Decisions

- Using raw SQL to understand database behavior
- Starting simple, then refactoring to cleaner architecture
- Combining behaviors initially, then splitting into RESTful endpoints
- Implementing authentication manually before abstractions
- Separating security logic from business logic
- Using JWT instead of sessions for stateless auth

---

## Learning

- Mixing responsibilities leads to hard-to-maintain code
- Proper structure improves scalability and testing
- JWT requires `sub` to be a string
- HTTPBearer + Depends integrates authentication into Swagger
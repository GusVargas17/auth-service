# Auth Service Notes

## Database
  - 'conn.rollback()' is required after a failed transaction
  - Without rollback, the connection remains in an invalid state

## FastAPI
  - Request: A request made by the client to the server (e.g., to retrieve or send data)
  - Endpoint: API access point that executes a function when it receives a request
  - GET: HTTP method used to retrieve data without modifying the system
  - POST: HTTP method used to send data and create resources on the server
  - @app.get(): Decorator that defines a GET endpoint
  - @app.post(): Decorator that defines a POST endpoint

## Errors
  - "password authentication failed" -> incorrect database credential
  - UniqueViolation -> triggered when inserting duplicate values in a UNIQUE column.

## Security
  - Passwords are hashed using bcrypt
  - Never store passwords in plain text

## Decisions
  - Using raw SQL instead of ORM to better understand database behavior
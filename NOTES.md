# Auth Service Notes

## Database
  - 'conn.rollback()' is required after a failed transaction
  - Without rollback, the connection remains in an invalid state

### psycopg2
  - cursor() : Creates a cursor to execute SQL queries on the database.
  - execute() : Runs a SQL query using the cursor.
  - fetchone() : Retrieves a single row from the query result.
  - fetchall() : Retrieves all rows from the query result.
  - commit() : Saves changes made to the database.
  - rollback() : Reverts changes when a transaction fails.

## HTTPS
  - HTTP Status Code: Numeric code that indicates the result of a request.
  - 200 OK : Runs a SQL query using the cursor.
  - 201 Created : Resource was successfully created.
  - 401 Unauthorized : Authentication failed or credentials are invalid.
  - 404 Not Found : Requested resource does not exist.
  - 409 Conflict : Request conflicts with current state.
  - 500 Internal Server Error : Unexpected server error.

## FastAPI
  - Request : A request made by the client to the server (e.g., to retrieve or send data)
  - Endpoint : API access point that executes a function when it receives a request
  - GET : HTTP method used to retrieve data without modifying the system
  - POST : HTTP method used to send data and create resources on the server
  - @app.get() : Decorator that defines a GET endpoint
  - @app.post() : Decorator that defines a POST endpoint

## Errors
  - "password authentication failed" -> incorrect database credential
  - UniqueViolation -> triggered when inserting duplicate values in a UNIQUE column.

## Security
  - Passwords are hashed using bcrypt
  - Never store passwords in plain text

## Decisions
  - Using raw SQL instead of ORM to better understand database behavior
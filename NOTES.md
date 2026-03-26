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

## HTTP
  - HTTP Status Code: Numeric code that indicates the result of a request.
  - 200 OK : Request was successful
  - 201 Created : Resource was successfully created.
  - 401 Unauthorized : Authentication failed or credentials are invalid.
  - 404 Not Found : Requested resource does not exist.
  - 409 Conflict : Request conflicts with current state.
  - 500 Internal Server Error : Unexpected server error.

## FastAPI
  - Request : A request made by the client to the server
  - Endpoint : API access point that executes a function when it receives a request
  - GET : HTTP method used to retrieve data without modifying the system
  - POST : HTTP method used to send data and create resources
  - @app.get() : Defines a GET endpoint
  - @app.post() : Defines a POST endpoint

## Errors
  - "password authentication failed" -> incorrect database credentials
  - UniqueViolation -> triggered when inserting duplicate values in a UNIQUE column.

## Security
  - Passwords are hashed using bcrypt
  - Never store passwords in plain text

## Decisions
  - Using raw SQL instead of ORM to better understand database behavior
  - Keeping endpoints simple first, then refactoring into cleaner structures once the logic is clear
  - Combining multiple behaviors in a single endpoint (e.g. list and filter) before splitting into more RESTful routes
  - Handling authentication manually before introducing abstractions (e.g. dependencies or middleware)
  - Separating security logic (hashing, JWT) from business logic to follow single responsibility principle

## Rules
  - Do not mix responsibilities in a single layer
  - Keep business logic independent from frameworks and databases

## Architecture
  - Clean Architecture : Organizes code into layers to separate responsibilities and improve maintainability
  - Layer : Logical separation of responsibilities in the system (e.g. API, Service, Repository)
  - Separation of Concerns : Each part of the system should handle a single responsibility
  - Abstraction : Hiding implementation details and exposing only necessary behavior

## Layers

  - API Layer : Handles HTTP requests and responses, delegates logic to services
  - Service Layer : Contains business logic and decision-making
  - Repository Layer : Handles database access and queries
  - Core Layer : Contains shared infrastructure (e.g. database connection)

## Flow
  - Request flows from client to database through layers
  - Response flows back from database to client through the same layers

## Principles
  - Business logic should not depend on external tools (e.g., database, frameworks)
  - Depend on abstractions, not implementations
  - Keep layers independent from each other

## Learning

  - Mixing responsibilities leads to hard-to-maintain code
  - Proper structure allows easier scaling and testing
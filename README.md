# Simple CRUD FastAPI Phyton
## Description
This is a simple CRUD API using FastAPI and Python. It is a simple API that allows you to create, read, update and delete actors. The API is connected to a PostgreSQL database. The API has the following endpoints:
- GET / - Returns a welcome message
- GET /actors - Returns a list of all actors
- GET /actors/{actor_id} - Returns a specific actor
- POST /actors - Creates a new actor
- PUT /actors/{actor_id} - Updates an actor
- DELETE /actors/{actor_id} - Deletes an actor

## Installation
1. Clone the repository
2. Create a database in PostgreSQL
3. Modify the database connection string in the file `db.py`
4. Create table with the following SQL command:
```sql
CREATE TABLE actor (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    last_update TIMESTAMP default now()
);
```
5. Run the API with the following command:
```bash
uvicorn main:app --reload
```
6. The API will be running at `http://127.0.0.1:8000`
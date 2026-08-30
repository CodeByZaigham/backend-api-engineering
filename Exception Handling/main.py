from fastapi import FastAPI,HTTPException
from exceptions.custom_exceptions import (
    UserNotFoundException,
    DatabaseException
)
from exceptions.handlers import (
    user_not_found_handler,
    database_exception_handler,
    http_exception_handler
)

app = FastAPI()

app.add_exception_handler(
    UserNotFoundException,
    user_not_found_handler
)

app.add_exception_handler(
    DatabaseException,
    database_exception_handler
)

app.add_exception_handler(
     HTTPException,
     http_exception_handler
)

@app.get("/users/{user_id}")
def users(user_id:str):
     if user_id!="0026": raise UserNotFoundException(user_id)
     return {"user":user_id}


@app.get("/test-database")
def test_database():
     raise DatabaseException


@app.get("/test-http")
def test_http():
     raise HTTPException(
          status_code=404,
          detail="This resource does not exist"
     )
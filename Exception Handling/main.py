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


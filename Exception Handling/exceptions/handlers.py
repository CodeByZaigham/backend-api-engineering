from fastapi import Request,HTTPException
from fastapi.responses import JSONResponse
from .custom_exceptions import (
     UserNotFoundException,
     DatabaseException
)


async def user_not_found_handler(
     request: Request,
     exc: UserNotFoundException
     ):
     return JSONResponse(
          status_code=404,
          content={
               "error": "User not found",
               "user_id": exc.user_id
          }
     )


async def database_exception_handler(
     request: Request,
     exc: DatabaseException
     ):
     return JSONResponse(
          status_code=500,
          content={
               "error": "Database error"
          }
     )

async def http_exception_handler(request: Request, exc: HTTPException):
     return JSONResponse(
          status_code=exc.status_code,
          content={
               "error": "HTTP error",
               "detail": exc.detail
          }
     )
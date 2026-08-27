from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm #Used when the user logs in.
from database.database import engine,get_db
from datetime import timedelta
from database.tables import Base,User
from sqlalchemy.orm import Session
from schema import createuser,token
from authentication import hash_password,verify_password,create_jwt_token


Base.metadata.create_all(bind=engine)

app=FastAPI(title="Login System")

@app.get("/",response_model=dict)
def health():
     return {"message":"test route working"}


          

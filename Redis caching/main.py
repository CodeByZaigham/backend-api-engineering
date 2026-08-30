from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm 
from database.database import engine,get_db
from datetime import timedelta
from database.tables import Base,User
from sqlalchemy.orm import Session
from schema import createuser,token,tokendata,showuser
from authentication import hash_password,verify_password,create_jwt_token
from authorization import decode_jwt
from typing import List
from contextlib import asynccontextmanager
from redis_server import redis
import json

@asynccontextmanager
async def lifespan(app:FastAPI):
     Base.metadata.create_all(bind=engine)
     cache=app.state.redis=redis
     yield
     cache.close()

app=FastAPI(title="Login System" , lifespan=lifespan)

@app.get("/",response_model=dict)
def health():
     return {"message":"test route working"}

@app.post("/createuser")
def create_user(data:createuser,db:Session=Depends(get_db)):
     hashed_password=hash_password(data.password)
     new_user=User(
          username=data.username,
          email=data.email,
          age=data.age,
          disabled=data.disabled,
          role=data.role,
          hash_password=hashed_password
     )
     db.add(new_user)
     db.commit()
     db.refresh(new_user)
     return {"message":"Account created Successfully!"}

@app.post("/login",response_model=token)
def userlogin(data:OAuth2PasswordRequestForm=Depends() , db:Session=Depends(get_db)):
     user=db.query(User).filter(User.username==data.username)
     for u in user:
          if verify_password(data.password,u.hash_password):
               user=u
     if not user: raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Incorrect username or password", 
          headers={"WWW-Authenticate": "Bearer"}
     )

     token_expiry=timedelta(minutes=30)          
     token=create_jwt_token(data={"sub":str(user.userid),"role":user.role},expiry=token_expiry)
     return {"access_token":token , "token_type":"bearer"}

#secured endpoint ->only authorized access
#As a admin, you want to list all the user accounts in the database         
@app.get("/userlist",response_model=List[dict])
def list_users(db:Session=Depends(get_db) , token:tokendata=Depends(decode_jwt)):
     if token.role=="admin":
          tokenbearer=db.query(User).filter(User.userid==token.userid).first()
          if tokenbearer.disabled:
               raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Admin account is disabled", 
                    headers={"WWW-Authenticate": "Bearer"}
               )
          
          userlist=app.state.redis.get("userlist") # Retrieving from redis
          if userlist is None:
               userlist=[]
               users=db.query(User).filter(User.role=="user")
               for u in users:
                    user=showuser(
                         userid=u.userid,
                         username=u.username,
                         email=u.email,
                         age=u.age,
                         role=u.role,
                         disabled=u.disabled,
                    )
                    userlist.append(user.model_dump())
               app.state.redis.set("userlist",json.dumps(userlist)) # -> caching
               return userlist
          return json.loads(userlist)


          
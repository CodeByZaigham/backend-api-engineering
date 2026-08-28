from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from fastapi import Depends
from dotenv import load_dotenv
from schema import tokendata
import os
import jwt
load_dotenv()

encryption_key=os.getenv("SECRET_KEY")
encryption_algorithm=os.getenv("ALGORITHM")

Oauth2_token=OAuth2PasswordBearer(tokenUrl="login")

def decode_jwt(token:str=Depends(Oauth2_token)) -> tokendata:
     try:
          payload=jwt.decode(token,encryption_key,encryption_algorithm)
          userid=int(payload.get("sub"))
          role=payload.get("role")
          data=tokendata(userid=userid,role=role)
          return data
     except InvalidTokenError as e:
          raise InvalidTokenError


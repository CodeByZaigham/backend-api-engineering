import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from datetime import datetime, timedelta , timezone
from dotenv import load_dotenv
import os
load_dotenv()

encryption_key=os.getenv("SECRET_KEY")
encryption_algorithm=os.getenv("ALGORITHM")
encrypt=PasswordHash.recommended()

def hash_password(password:str):
     return encrypt.hash(password)

def verify_password(password,hashed_password)->bool:
     return encrypt.verify(password,hashed_password)

def create_jwt_token(data:dict,expiry:timedelta):
     userdata=data.copy()
     expiry_date=(datetime.now(timezone.utc) + expiry)
     userdata.update({"exp":expiry_date})
     return jwt.encode(userdata,encryption_key,encryption_algorithm)

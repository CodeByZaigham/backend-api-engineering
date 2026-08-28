from pydantic import BaseModel
from typing import List

class token(BaseModel):
    access_token: str
    token_type: str

class tokendata(BaseModel):
    userid: int
    role:str


class userdata(BaseModel):
     username:str
     email:str
     age:int
     role:str
     disabled:bool=False

class showuser(userdata):
     userid:int

class createuser(userdata):
     password:str

class dbuser(userdata):
     hash_password:str

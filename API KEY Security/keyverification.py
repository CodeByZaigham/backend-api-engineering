from fastapi import Security,HTTPException
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os
load_dotenv()

api=os.getenv("SECRET_KEY")

header_api=APIKeyHeader(name="x-api-key")

def verify_api_key(api_given:str=Security(header_api)):
     if api != api_given:
          raise HTTPException(status_code=401 , detail="invalid or none api key")
     return True
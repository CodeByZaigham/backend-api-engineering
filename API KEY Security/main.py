from fastapi import FastAPI,Security
# from schema import inputs
from keyverification import verify_api_key

app=FastAPI(title="Secured Public API")

@app.get("/",response_model=dict)
def health(is_api_valid:bool=Security(verify_api_key)):
     if is_api_valid:
          return {"message":"Authorized"}
     return {"message":"UnAuthorized"}



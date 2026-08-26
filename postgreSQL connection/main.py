from fastapi import FastAPI
from schema import inputs

app=FastAPI(title="Basic Routes Initialization")

@app.get("/",response_model=dict)
def health():
     return {"message":"test route working"}
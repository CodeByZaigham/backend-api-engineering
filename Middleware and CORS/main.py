from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from time import perf_counter
import json

app=FastAPI(title="Basic Routes Initialization")

app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"], #In production we product the list of frontend origins which can access our backend.
     allow_credentials=True, #used for cookies and token based data
     allow_headers=["*"], # in production, allow only the necessary ones such as authorization headers and x-api-key etc...
     allow_methods=["get","post","update","delete"] #allow only which your endpoints actually use
)

@app.middleware("http")
async def get_request_details(resquest:Request , call_next):
     print(resquest["path"])
     print(resquest["method"])
     payload=await resquest.body()
     if payload: print(json.loads(payload))
     start=perf_counter()
     response=await call_next(resquest)
     end=perf_counter() - start
     print(end)
     return response

@app.get("/",response_model=dict)
def health():
     return {"message":"test route working"}
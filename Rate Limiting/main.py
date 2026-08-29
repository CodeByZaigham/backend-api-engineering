from fastapi import FastAPI

app=FastAPI(title="Rate Limiting")

@app.get("/",response_model=dict)
def health():
     return {"message":"test route working"}
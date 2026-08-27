from fastapi import FastAPI,Depends,HTTPException
from database.database import session,engine
from database.tables import Base,Questions,Choices
from sqlalchemy.orm import Session
from schema import Question

app=FastAPI(title="Quiz Application")

Base.metadata.create_all(bind=engine)

def get_db():
     db = session()
     try:
          yield db
     finally:
          db.close()

@app.get("/",response_model=dict)
def health():
     return {"message":"test route working"}


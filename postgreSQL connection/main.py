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

@app.post("/questions")
def add_questions(input:Question,db:Session=Depends(get_db)):
     db_question=Questions(question=input.text)
     db.add(db_question)
     db.commit()
     db.refresh(db_question)
     for choice in input.choices:
          db_choice=Choices(text=choice.text , is_true=choice.is_true , question_id=db_question.id)
          db.add(db_choice)
     db.commit()
     # db.refresh()

@app.get("/get_questions/{id}")
def show_quiz(id:int,db:Session=Depends(get_db)):
     question=db.query(Questions).filter(Questions.id==id).first()
     if not question: raise HTTPException(status_code=404,detail="no question found for the question id!")
     choice=db.query(Choices).filter(Choices.question_id==id).all()
     return {"question: ":question , "choices: ":choice}
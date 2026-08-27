from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean,Integer,Column,ForeignKey,String

Base=declarative_base()

class Questions(Base):
     __tablename__="questions"

     id=Column(Integer , primary_key=True,index=True)
     question=Column(String)

class Choices(Base):
     __tablename__="choices"

     id=Column(Integer , primary_key=True,index=True)
     text=Column(String)
     is_true=Column(Boolean,default=False)
     question_id=Column(Integer,ForeignKey("questions.id"))

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean,Integer,Column,ForeignKey,String

Base=declarative_base()

class User(Base):
     __tablename__="users"

     userid=Column(Integer,primary_key=True,index=True)
     username=Column(String)
     email=Column(String)
     age=Column(Integer)
     role=Column(String,default="user")
     disabled=Column(Boolean,default=False)
     hash_password=Column(String)
     



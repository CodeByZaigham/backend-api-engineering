from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

url=os.getenv("DATABASE_URL")

engine=create_engine(url=url,pool_size=10,max_overflow=5)

session=sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
     db = session()
     try:
          yield db
     finally:
          db.close()
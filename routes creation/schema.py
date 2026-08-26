from pydantic import BaseModel

class inputs(BaseModel):
     name:str
     age:int
     is_engineer:bool
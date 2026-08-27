from pydantic import BaseModel
from typing import List

class Choice(BaseModel):
     text:str
     is_true:bool

class Question(BaseModel):
     text:str
     choices:List[Choice]
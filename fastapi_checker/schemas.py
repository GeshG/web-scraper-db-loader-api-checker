from typing import Union
from pydantic import BaseModel



class News(BaseModel):
    Id : int
    Headline : str
    Link : str
 
    class Config:
        orm_mode = True

class News_Create(BaseModel):
    Headline: str
    Link: str

class News_Update(BaseModel):
    Id : int
    Headline: str 
    Link: str

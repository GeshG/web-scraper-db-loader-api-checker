from typing import Union
from pydantic import BaseModel



class News(BaseModel):
    Headline : str
    Link : str
    
    class Config:
        orm_mode = True
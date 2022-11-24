from typing import Union
from pydantic import BaseModel



class News(BaseModel):
    Headline: str
    Link: str
    Date_Published: str

    #don't think I will use ORM at this moment
    class Config:
        orm_mode = True
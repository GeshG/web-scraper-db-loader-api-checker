from typing import Union
from pydantic import BaseModel



class News(BaseModel):
    headline: str
    link: str
    datetime: str

    class Config:
        orm_mode = True

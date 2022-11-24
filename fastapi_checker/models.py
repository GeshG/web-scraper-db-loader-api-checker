from sqlalchemy import Column, String
from database import Base


class News_Out(Base):
    __tablename__ = "news"
    Id = Column(primary_key = True, index = True)
    Headline = Column(String, unique=True, nullable = False)
    Link = Column(String, unique=True, nullable = False)
    Date_Published = Column(String, unique=True, nullable = True)
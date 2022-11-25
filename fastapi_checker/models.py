from sqlalchemy import Column, String
from database import Base


class News_Out(Base):
    __tablename__ = "news"
    Headline = Column(String, primary_key = True, unique=True, nullable = False)
    Link = Column(String, unique=True, nullable = False)
    
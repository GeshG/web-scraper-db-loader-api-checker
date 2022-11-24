from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:////Users/gginchev/Desktop/news.db" #connecting to the actual database


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} # this is needed only for sqlite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # each instance of the SessionLocal class will be a database session
                                                                            # once an instance is created of SessionLocal it will be the actual db session
Base = declarative_base() # the function will return a class

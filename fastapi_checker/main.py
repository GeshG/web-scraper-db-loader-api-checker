import json
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

import requests


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home():
    return ('It\'s working')


@app.get("/news/headline", response_model=list[schemas.News])
def read_headline(skip: str = 0, limit: int = 100, db: Session = Depends(get_db)):
    headlines = crud.get_news_headline(db, skip=skip, limit=limit)
    return headlines


@app.get("/news/link}", response_model=schemas.News)
def read_link(links: str, db: Session = Depends(get_db)):
    db_link = crud.get_news_link(db, link=links)
    if db_link is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_link


@app.get("/news/date_posted", response_model=list[schemas.News])
def read_date_published(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    published_date = crud.get_date_published(db, skip=skip, limit=limit)
    return published_date


@app.put('/news')
def upload_news():
    api_url = "sqlite:///./sql_app.db"
    response = requests.get(api_url)
    response.json


with open('/Users/gginchev/Downloads/Desktop - 21-10-2022/web-scraper-news/file.json.csv','r') as news_json:
    data = json.load(news_json)


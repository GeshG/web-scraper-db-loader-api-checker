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

@app.get("/news/Headline", response_model=schemas.News)
def read_headline(db: Session = Depends(get_db)):
    get_headline = crud.get_news_headline(db=db)
    return get_headline


@app.get("/news/Link", response_model=schemas.News)
def read_link(db: Session = Depends(get_db)):
    db_link = crud.get_news_link(db=db)
    if db_link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return db_link


@app.get('/news', response_model=list[schemas.News])
def get_all_newss(db: Session = Depends(get_db)):
    get_all = crud.get_all_news(db=db)
    return get_all



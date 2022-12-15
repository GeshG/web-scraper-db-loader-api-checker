import json
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas, database
from database import SessionLocal, engine
from fastapi_pagination import  Page, paginate, add_pagination

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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
def read_headline(id : int, db: Session = Depends(get_db)):
    get_headline = crud.get_news_headline(db=db, id = id)
    if get_headline is None:
        raise HTTPException(status_code=404, detail='No news found')
    return get_headline 

@app.get("/news/Link", response_model=schemas.News)
def read_link(db: Session = Depends(get_db)):
    db_link = crud.get_news_link(db=db)
    if db_link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return db_link

#working
@app.post("/news")
def create_news(create_news : schemas.News_Create, db: Session = Depends(get_db)):
    add_new = crud.create_new_news(db=db, create_news=create_news)
    return (f'News successfully added')

#working
@app.put('/news')
def put_news(id: int, update_param : schemas.News_Update, db: Session = Depends(get_db)):
    details = crud.update_news(db=db, details=update_param, id=id)
    return (f'Successfully updated news')

#working
@app.delete("/news/Headline/id")
def delete_news_id(news_id : int, db: Session = Depends(get_db)):
    delete_news = crud.delete_news(db=db, news_id=news_id)
    if id is None:
        raise HTTPException(status_code=404, detail='Id does not exist')
    return (f'Successfully Deleted News')
    
@app.get('/news', response_model=Page[schemas.News])
def get_news_pages(db: Session = Depends(get_db)):
    news_pagi = paginate(db.query(models.News_Out).all())
    return news_pagi

add_pagination(app)

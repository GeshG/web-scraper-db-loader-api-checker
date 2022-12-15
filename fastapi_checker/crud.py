from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import update

def get_news_headline(db: Session, id : int): 
    return db.query(models.News_Out).filter(models.News_Out.Id == id).first()

def get_news_link(db: Session):
    return db.query(models.News_Out).first()

def get_all_news(db: Session):
    return db.query(models.News_Out).all()

#working
def create_new_news(db: Session, create_news : schemas.News_Create):
    create_news = models.News_Out(Headline = create_news.Headline, Link = create_news.Link)
    db.add(create_news)
    db.commit()
    return create_news

#working
def update_news(db: Session, update_news : schemas.News_Update):
    news = models.News_Out(Id = update_news.Id, Headline = update_news.Headline, Link = update_news.Link)
    news.Id = update_news.Id
    news.Headline = update_news.Headline
    news.Link = update_news.Link
    db.commit()
    return news

def update_news(db: Session, id : int, details : schemas.News_Update):
    db.query(models.News_Out).filter(models.News_Out.Id == id).update(vars(details))
    db.commit()
    return db.query(models.News_Out).filter(models.News_Out.Id == id).first()

#working
def delete_news(db: Session, news_id : int):
    news = db.query(models.News_Out).filter(models.News_Out.Id== news_id).first()
    db.delete(news)
    db.commit()


from sqlalchemy.orm import Session
import models, schemas

def get_news_headline(db: Session, headline_str: str):
    return db.query(models.News).filter(models.News.Headline == headline_str).first()

def get_news_link(db: Session, news_link: str):
    return db.query(models.News).filter(models.News.Link == news_link).first()

def get_date_published(db: Session, publish_date: str):
    return db.query(models.News).filter(models.News.Date_Published == publish_date).first()

def get_all_news(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.News).offset(skip).limit(limit).all()

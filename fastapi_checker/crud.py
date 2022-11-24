from sqlalchemy.orm import Session
import models, schemas

def get_news_headline(db: Session): #declaring the parameters we will query 
    return db.query(models.News_Out).filter(models.News_Out.Headline).first()

def get_news_link(db: Session):
    return db.query(models.News_Out).filter(models.News_Out.Link).first()

def get_date_published(db: Session):
    return db.query(models.News_Out).filter(models.News_Out.Date_Published).first()

def get_all_news(db: Session):
    return db.query(models.News_Out).all()




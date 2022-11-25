from sqlalchemy.orm import Session
import models, schemas

def get_news_headline(db: Session): 
    return db.query(models.News_Out).first()

def get_news_link(db: Session):
    return db.query(models.News_Out).first()

def get_all_news(db: Session):
    return db.query(models.News_Out).all()




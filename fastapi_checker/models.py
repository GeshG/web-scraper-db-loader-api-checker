from sqlalchemy import Column, String


from database import Base


class News(Base):
    __tablename__ = "news"

    Headline = Column(String, unique=True, primary_key=True, nullable = False)
    Link = Column(String, unique=True, nullable = False)
    Date_Published = Column(String, unique=True, nullable = True)



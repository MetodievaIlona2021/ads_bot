from sqlalchemy import (Column, Integer, String, Sequence, BigInteger, TIMESTAMP, Boolean, JSON, Text, ForeignKey)
from sqlalchemy import sql
from utils.db_api.database_gino import db


# Пользователи
class User(db.Model):
    __tablename__ = 'users'

    # id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger, primary_key=True, unique=True)
    name = Column(String(100))
    username = Column(String(50))
    email = Column(String(50))

    query: sql.Select

    def __repr__(self):
        return f"<User(id='{self.id}', name='{self.name}', username='{self.username}')>"


# Статьи
class Article(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, Sequence('article_id_seq'), primary_key=True)
    name = Column(String(1000))
    text = Column(Text)
    url = Column(String(1000))
    thumb_url = Column(String(1000), nullable=True)
    category = Column(String(50))

    query: sql.Select

    def __repr__(self):
        return f"<Article(id='{self.id}', name='{self.name}')>"


# Интервью
class Video(db.Model):
    __tablename__ = 'videos'

    id = Column(Integer, Sequence('video_id_seq'), primary_key=True)
    name = Column(String(100))
    description = Column(String(1000))
    thumb_url = Column(String(100))
    url = Column(String(100))
    category = Column(String(50))

    query: sql.Select

    def __repr__(self):
        return f"<Video(id='{self.id}', name='{self.name}')>"


# Отзывы
class Review(db.Model):
    __tablename__ = 'reviews'

    id = Column(Integer, Sequence('review_id_seq'), primary_key=True)
    name = Column(String(100))
    description = Column(Text)
    thumb_url = Column(String(100))
    url = Column(String(100))
    category = Column(String(50))

    query: sql.Select

    def __repr__(self):
        return f"<Review(id='{self.id}', name='{self.name}')>"


# Новости
class News(db.Model):
    __tablename__ = 'news'

    id = Column(Integer, Sequence('news_id_seq'), primary_key=True)
    title = Column(String(1000))
    description = Column(Text)
    thumb_url = Column(String(1000))
    url = Column(String(1000))
    category = Column(String(50))

    query: sql.Select

    def __repr__(self):
        return f"<News(id='{self.id}', name='{self.name}')>"


# Значимое
class Significant(db.Model):
    __tablename__ = 'significant'

    id = Column(Integer, Sequence('significant_id_seq'), primary_key=True)
    name = Column(String(100))
    text = Column(Text)
    thumb_url = Column(String(1000), nullable=True)
    category = Column(String(50))

    query: sql.Select

    def __repr__(self):
        return f"<Significant(id='{self.id}', name='{self.name}')>"


# Кейсы ADS
class Case(db.Model):
    __tablename__ = 'cases'

    id = Column(Integer, Sequence('case_id_seq'), primary_key=True)
    name = Column(String(100))
    text = Column(Text)
    thumb_url = Column(String(1000), nullable=True)
    category = Column(String(50))

    query: sql.Select

    def __repr__(self):
        return f"<Case(id='{self.id}', name='{self.name}')>"


# Запросы на рекрут
class RecruitQuery(db.Model):
    __tablename__ = 'recruit_query'

    id = Column(Integer, Sequence('recruit_id_seq'), primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    time_stamp = Column(TIMESTAMP)
    company_info = Column(Text)
    research_type = Column(String(100))
    survey_time = Column(String(100))
    target_audience = Column(Text)
    payments_type = Column(String(100))
    budget = Column(Text)
    sources = Column(Text)
    respondent_data = Column(Text)
    stock_respondents_info = Column(Text)

    query: sql.Select

    def __repr__(self):
        return f"<RecruitQuery(id='{self.id}', name='{self.name}')>"

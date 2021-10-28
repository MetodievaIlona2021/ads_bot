import datetime
from typing import List
from aiogram import types, Bot
from asyncpg import Connection
from sqlalchemy import and_

from utils.db_api.models import User, Video, Review, News, Article, Significant, Case, Ask
from utils.db_api.database_gino import db


class DBCommands:

    async def get_user(self, user_id):
        user = await db
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    async def add_new_user(self, referral=None):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.username = user.username
        new_user.full_name = user.full_name

        await new_user.create()
        return new_user

    async def show_items(self):
        # items = await Item.query.gino.all()
        items = await Video.query.order_by(Video.name).gino.all()

        return items

    async def show_sorted_items(self, search_query: str = None):
        if search_query == 'interview':
            search_items = await Video.query.where(Video.category.ilike(f'%{search_query}%')).gino.all()
        elif search_query == 'review':
            search_items = await Review.query.where(Review.category.ilike(f'%{search_query}%')).gino.all()
        elif search_query == 'news':
            search_items = await News.query.where(News.category.ilike(f'%{search_query}%')).gino.all()
        elif search_query == 'articles':
            search_items = await Article.query.where(Article.category.ilike(f'%{search_query}%')).gino.all()
        elif search_query == 'significant':
            search_items = await Significant.query.where(Significant.category.ilike(f'%{search_query}%')).gino.all()
        elif search_query == 'cases':
            search_items = await Case.query.where(Case.category.ilike(f'%{search_query}%')).gino.all()
        elif search_query == 'asks':
            search_items = await Ask.query.where(Ask.category.ilike(f'%{search_query}%')).gino.all()
        else:
            search_items = await Video.query.order_by(Video.name).gino.all()

        return search_items


# Функция для создания нового товара в базе данных. Принимает все возможные аргументы, прописанные в Item
async def add_video(**kwargs):
    new_video = await Video(**kwargs).create()
    return new_video


async def add_review(**kwargs):
    new_review = await Review(**kwargs).create()
    return new_review


async def add_news_item(**kwargs):
    new_news = await News(**kwargs).create()
    return new_news


async def add_article(**kwargs):
    new_articles = await Article(**kwargs).create()
    return new_articles


async def get_articles():
    articles = await Article.query.order_by(Article.id).gino.all()
    return articles


async def add_significant_item(**kwargs):
    new_significant = await Significant(**kwargs).create()
    return new_significant


async def add_case(**kwargs):
    new_case = await Case(**kwargs).create()
    return new_case


async def add_ask(**kwargs):
    new_ask = await Ask(**kwargs).create()
    return new_ask

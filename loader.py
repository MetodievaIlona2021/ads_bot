import os

import django
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config


def setup_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.telegram_bot.settings')
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': 'true'})
    django.setup()


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
ds = setup_django

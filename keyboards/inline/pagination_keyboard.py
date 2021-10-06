from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

pagination_call = CallbackData('paginator', 'key', 'page')


def get_page_keyboard(max_pages: int, key='article', page: int = 1):

    first_page_text = '<1>'
    last_page_text = f'<{max_pages}>'

    previous_page = page - 1
    previous_page_text = '<< '

    current_page_text = f'<{page}>'

    next_page = page + 1
    next_page_text = ' >>'

    articles_markup = InlineKeyboardMarkup(row_width=5)

    articles_markup.insert(
        InlineKeyboardButton(
            text=first_page_text,
            callback_data=pagination_call.new(key=key, page=1)
        )
    )

    if previous_page > 0:
        articles_markup.insert(
            InlineKeyboardButton(
                text=previous_page_text,
                callback_data=pagination_call.new(key=key, page=previous_page)
            )
        )

    articles_markup.insert(
        InlineKeyboardButton(
            text=current_page_text,
            callback_data=pagination_call.new(key=key, page='current_page')
        )
    )

    if next_page < max_pages:
        articles_markup.insert(
            InlineKeyboardButton(
                text=next_page_text,
                callback_data=pagination_call.new(key=key, page=next_page)
            )
        )

    articles_markup.insert(
        InlineKeyboardButton(
            text=last_page_text,
            callback_data=pagination_call.new(key=key, page=max_pages - 1)
        )
    )

    return articles_markup

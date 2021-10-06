from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Клавиатура для оплаты через qiwi
payment_services_keyboard = InlineKeyboardMarkup(row_width=1)

qiwi_btn = InlineKeyboardButton(text='Qiwi', callback_data='qiwi')
youkassa_btn = InlineKeyboardButton(text='ЮKassa', callback_data='youkassa')
go_to_main_page_btn = InlineKeyboardButton(text='На главную', callback_data='on_main')

payment_services_keyboard.add(qiwi_btn, youkassa_btn, go_to_main_page_btn)


# Клавиатура для проверки оплаты через qiwi
paid_keyboard = InlineKeyboardMarkup(row_width=1)

paid_btn = InlineKeyboardButton(text='Оплатил', callback_data='paid')
cancel_btn = InlineKeyboardButton(text='Отмена', callback_data='cancel')

paid_keyboard.add(paid_btn, cancel_btn)

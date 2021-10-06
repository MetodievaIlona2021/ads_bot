from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import LabeledPrice

from data.config import YOUKASSA_TOKEN
from loader import dp, bot
from states.recruiting_states import PaymentService


@dp.callback_query_handler(text='youkassa', state=PaymentService.Payment)
async def payment_youkassa(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await call.message.answer('Введите сумму услуги:')
    await PaymentService.PaymentYOUKASSAAmount.set()


@dp.message_handler(state=PaymentService.PaymentYOUKASSAAmount)
async def get_service_amount(message: types.Message, state: FSMContext):
    try:
        amount = int(message.text)
    except ValueError:
        await message.answer('Неверное значение, введите число')
        return

    currency = 'RUB'
    need_name = True
    need_phone_number = False
    need_email = True
    need_shipping_address = False

    await bot.send_invoice(chat_id=message.from_user.id,
                           title='Услуга рекрутинг',
                           description='Рекрутинг респондентов',
                           payload=str(1),
                           start_parameter=str(1),
                           currency=currency,
                           prices=[
                               LabeledPrice(label='Услуга рекрутинг', amount=amount * 100)
                           ],
                           provider_token=YOUKASSA_TOKEN,
                           need_name=need_name,
                           need_phone_number=need_phone_number,
                           need_email=need_email,
                           need_shipping_address=need_shipping_address)

    await PaymentService.PaymentYOUKASSA.set()


@dp.pre_checkout_query_handler(state=PaymentService.PaymentYOUKASSA)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id, ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id, text="Спасибо за покупку!")


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT, state=PaymentService.PaymentYOUKASSA)
async def process_successful_payment(message: types.Message, state: FSMContext):
    total_amount = message.successful_payment.total_amount // 100
    currency = message.successful_payment.currency

    await bot.send_message(message.chat.id, f'Оплата прошла успешно.\nСпасибо за покупку'
                                            f'\nСтоимость покупки = {total_amount} {currency}')

    await state.reset_state()

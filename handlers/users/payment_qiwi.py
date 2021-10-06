from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink, hcode

from data import config
from keyboards.inline.payment_keyboard import paid_keyboard
from keyboards.inline.recruiting_keyboards import menu_keyboard
from loader import dp
from states.recruiting_states import PaymentService
from utils.misc.qiwi import Payment, NoPaymentFound, NotEnoughMoney


@dp.callback_query_handler(text='qiwi', state=PaymentService.Payment)
async def payment_qiwi(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    await call.message.answer('Введите сумму услуги:')
    await PaymentService.PaymentQIWIAmount.set()


@dp.message_handler(state=PaymentService.PaymentQIWIAmount)
async def get_service_amount(message: types.Message, state: FSMContext):
    try:
        amount = int(message.text)
    except ValueError:
        await message.answer('Неверное значение, введите число')
        return

    payment = Payment(amount=amount)
    payment.create()

    await message.answer(
        '\n'.join([
            f'Оплатите не менее {amount:.2f} по номеру телефона или по адресу',
            '',
            hlink(config.WALLET_QIWI, url=payment.invoice),
            'И обязательно укажите ID платежа:',
            hcode(payment.id)
        ]),
        reply_markup=paid_keyboard)

    await PaymentService.PaymentQIWI.set()
    await state.update_data(payment=payment)


@dp.callback_query_handler(text='cancel', state=PaymentService.PaymentQIWI)
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Отменено', reply_markup=menu_keyboard)
    await state.finish()


@dp.callback_query_handler(text='paid', state=PaymentService.PaymentQIWI)
async def approve_payment(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    payment: Payment = data.get('payment')
    try:
        payment.check_payment()
    except NoPaymentFound:
        await call.message.answer('Транзакция не найдена.')
        return
    except NotEnoughMoney:
        await call.message.answer('Оплаченная сума меньше необходимой.')
        return

    else:
        await call.message.answer('Успешно оплачено')
    await call.message.edit_reply_markup()
    await state.finish()

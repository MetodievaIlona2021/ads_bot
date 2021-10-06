from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram_calendar import SimpleCalendar, simple_cal_callback

from keyboards.inline.recruiting_keyboards import go_to_main_page_markup, zoom_markup, time_zoom_markup
from loader import dp
from states.recruiting_states import OnlineMeeting


@dp.callback_query_handler(text='online_meeting')
async def show_contacts(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    text = 'Есть масштабный исследовательский проект?\n' \
           'Запишитесь на консультацию с руководителем агентства!\n\n' \
           '<b>Описание услуги</b>\n\n' \
           'Если у Вас уже планируется масштабное исследование и Вы хотите получать консультацию по стоимости ' \
           'и срокам подбора , Вы можете написать нам или получить бесплатную консультацию в Zoom с ' \
           'руководителем ADS\n\n' \
           '<b>Правила отмены записи</b>\n\n' \
           'Если вы решите отменить встречу, пожалуйста, свяжитесь с нами по телефону +7 (499) 394-04-65, ' \
           'почте ads@adsrecruiting.com или отмените встречу в личном кабинете (для зарегистрированных пользователей, ' \
           'вход в меню сайта)'
    await call.message.edit_text(text=text, reply_markup=zoom_markup)


@dp.callback_query_handler(text='zoom')
async def vote_datetime_meeting(call: types.CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(text='Выберите дату встречи:', reply_markup=await SimpleCalendar().start_calendar())
    await OnlineMeeting.DateMeeting.set()


@dp.callback_query_handler(simple_cal_callback.filter(), state=OnlineMeeting.DateMeeting)
async def process_simple_calendar(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(call, callback_data)
    # if selected:
    #     await call.message.answer(
    #         f'Вы записаны на {date.strftime("%d/%m/%Y")}')
    await state.update_data(date_meeting=date.strftime("%d/%m/%Y"))
    await call.message.edit_text('Выберите время:', reply_markup=time_zoom_markup)
    await OnlineMeeting.TimeMeeting.set()


@dp.callback_query_handler(state=OnlineMeeting.TimeMeeting)
async def get_time_meeting(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    data = call.data
    if data == 'twelve':
        time_meeting = '12:00'
    elif data == 'twelve_thirty':
        time_meeting = '12:30'
    elif data == 'thirteen':
        time_meeting = '13:00'
    elif data == 'thirteen_thirty':
        time_meeting = '13:30'
    elif data == 'fourteen':
        time_meeting = '14:00'
    elif data == 'fourteen_thirty':
        time_meeting = '14:30'
    elif data == 'fifteen':
        time_meeting = '15:00'
    else:
        time_meeting = '15:30'

    state_data = await state.get_data()
    date_meeting = state_data.get('date_meeting')

    await call.message.answer(text=f'Вы записаны на {date_meeting} {time_meeting}')
    await state.reset_state()

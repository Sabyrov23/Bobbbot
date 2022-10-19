from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from KEyboard.client_cb import cancel_markup
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMINS
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    dir = State()
    age = State()
    group = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id in ADMINS:
            await FSMAdmin.id.set()
            await message.answer('Приветствую\nВведите айди ментора', reply_markup=cancel_markup)
        else:
            await message.answer('Ты не админ!')
    else:
        await message.answer('Нельзя в группе')


async def load_id(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['id'] = int(message.text)
        await FSMAdmin.next()
        await message.answer('Введите имя ментора', reply_markup=cancel_markup)
    except:
        await message.answer('Должны быть только цифры\n Введите айди снова', reply_markup=cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Какое у ментора направление', reply_markup=cancel_markup)


async def load_dir(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dir'] = message.text
    await FSMAdmin.next()
    await message.answer('Возраст ментора', reply_markup=cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if age < 12 or age > 45:
            await message.answer('ментора такого возраста не бывает', reply_markup=cancel_markup)
        else:
            async with state.proxy() as data:
                data['age'] = age
            await FSMAdmin.next()
            await message.answer('Введите группу ментора', reply_markup=cancel_markup)
    except:
        await message.answer('Только числа')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"ID: {data['id']} Name: {data['name']} Direction: {data['dir']} Age: {data['age']}, Group: {data['group']}")
    await state.finish()
    await message.answer('Регистрация завершена')


async def cancel_reg(message: types.Message, state: FSMContext):
    cur_state = await state.get_state()
    if cur_state is not None:
        await state.finish()
        await message.answer('Регистрация отменена')

def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, commands=['cancel'], state='*')
    dp.register_message_handler(cancel_reg, Text(equals='Cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_dir, state=FSMAdmin.dir)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)

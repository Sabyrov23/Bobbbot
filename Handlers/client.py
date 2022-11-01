from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import random
from database.bot_db import sql_create

async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Hello {message.from_user.first_name}!")


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "who is the creator of tik tok?"
    answers = [
        "Hyunjoo Shim",
        "Cho Jeong",
        "Lee Dong He",
        "Jihye Lee",
        "Znang Yiming",
        "Soon Hoe Kim",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="",
        open_period=25,
        reply_markup=markup
    )

async def pin(message:types.Message):
    if not message.reply_to_message:
        await message.reply("Комманда должна быть ответомм на сообщение")
    else:
        await bot.pin_chat_message(message.chat.id, message.message_id)

async def show_random_user(message:types.Message):
    await sql_create.sql_command_random(message)



async def mem(message: types.Message):
    photo = open("media/mem.jpg", 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start','help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'],commands_prefix= "!")
    dp.register_message_handler(show_random_user(), commands=['get'])
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot, dp


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_back = InlineKeyboardButton("NEXT", callback_data="button_call_back")
    markup.add(button_call_back)

    question = "who created atomic energy?"
    answers = [
        "Jhonson",
        "Chadwick",
        "David",
        "Kokeyn",
        "Gilbert",
        "Uilyam",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="",
        open_period=25,
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):
    question = "who created weather?"
    answers = [
        "God",
        "people",
        "I",
        "Cat",
        "Dog",
        "Rat",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="",
        open_period=25
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')
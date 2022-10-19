from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot


async def quiz_2(call: types.CallbackQuery):
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
        open_period=25
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
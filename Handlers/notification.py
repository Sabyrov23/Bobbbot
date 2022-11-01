import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot

async def get_chat_id(message:types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="Команда выполнена")

async def eat():
    await bot.send_message(chat_id=chat_id, text="Покушай")
async def scheduler():
    aioschedule.every().day.at("13:00").do(eat)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp:Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word:"Напомни" in word.text)

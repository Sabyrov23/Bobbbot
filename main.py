from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Handlers import callback, fsm_menu, client, extra
from config import bot, dp
import logging

callback.register_handlers_callback(dp)
client.register_handlers_client(dp)
extra.register_handlers_extra(dp)
fsm_menu.register_handlers_fsm(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = "5785677019:AAHciUQDHHMwkklKf8DlGxtBD4aIGuMdL2s"
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMINS = [772252520, ]

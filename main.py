from aiogram.utils import executor
from config import bot, dp
import logging
from Handlers import callback, client, extra, fsm_menu,notification, inline
from database.bot_db import sql_create
import asyncio

async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()

callback.register_handlers_callback(dp)
client.register_handlers_client(dp)
extra.register_handlers_extra(dp)
fsm_menu.register_handlers_fsm(dp)
inline.register_inline_hendler(dp)
notification.register_handlers_notification(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

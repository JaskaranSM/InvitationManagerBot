from aiogram import executor
from tgbot import dp, LOGGER, BANNED_USERS
from tgbot.utils.db_utils import getAllBannedUsers
from .modules import handlers, admin
import asyncio


async def initDatabase():
    LOGGER.info("Initialing Database.")
    users = await getAllBannedUsers()
    BANNED_USERS.extend(users)

def main():
    asyncio.get_event_loop().run_until_complete(initDatabase())
    executor.start_polling(dp)

main()
import json
import logging

from aiogram import Bot, Dispatcher, types


# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()],
                    level=logging.INFO)

LOGGER = logging.getLogger(__name__)


CONFIG_PATH = "config.json"

BANNED_USERS = []


def getConfig(config_path):
    with open(config_path,"r") as f:
        return json.load(f)

config = getConfig(CONFIG_PATH)

bot = Bot(token=config.get("bot_token"),parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)



from tgbot import LOGGER,config
from tgbot.utils.db_utils import isUserBanned

def bannedUserFilter(message):
    banned = isUserBanned(message.from_user.id)
    if banned:
        LOGGER.info(f"Message from banned user: {message.from_user.id} : {message.from_user.first_name}")
    return not banned

def sudoUserFilter(message):
    return message.from_user.id in config.get("sudo_users")

def isChatPrivate(message):
    return message.chat.type == "private"
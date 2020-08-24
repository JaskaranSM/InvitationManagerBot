from tgbot import config,bot,LOGGER

async def isUserMember(userId):
    LOGGER.info(f"Checking if {userId} is in our kholi!")
    try:
        member = await bot.get_chat_member(config.get("base_chat"),userId)
        if member.status == "left" or member.status == "kicked":
            return False
    except Exception as e:
        LOGGER.error(e)
        return False
    return True

def isUserSudo(userId):
    return userId in config.get("sudo_users")

def extractUserId(message):
    args = message.text.split(" ")
    if message.reply_to_message:
        userId = message.reply_to_message.from_user.id
    elif len(args) >= 2:
        userId = int(args[1])
    else:
        return False
    return userId
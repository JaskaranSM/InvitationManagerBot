from tgbot import bot, dp, LOGGER,config 
from tgbot.utils.bot_utils import isUserMember
from tgbot.utils.filters import bannedUserFilter, isChatPrivate




@dp.message_handler(bannedUserFilter,isChatPrivate,commands=['start'])
async def startPhase(message):
    print(message.reply_to_message)
    user = message.from_user
    LOGGER.info(f"Start from : {user.id} | {user.first_name}")
    if not await isUserMember(user.id):
        return await message.reply(f"Join my group first : {config.get('group_link')}")

    await message.reply("Send your EMAIL-ID.")
old= r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
@dp.message_handler(bannedUserFilter,isChatPrivate,regexp=r"^[a-z0-9]+[\._]?[a-z0-9]+[@]gmail.com")
async def emailPhase(message):
    user = message.from_user 
    LOGGER.info(f"Email from : {user.id} | {user.first_name}")
    if not await isUserMember(user.id):
        return await message.reply("press /start first.")

    email_id = message.text
    out = ""
    out += f"<b>FirstName:</b> <code>{user.first_name}</code>\n"
    if user.last_name:
        out += f"<b>LastName:</b> <code>{user.last_name}</code>\n"
    if user.username:
        out += f"<b>UserName:</b> @{user.username}\n"
    out += f"<b>UserId:</b> <code>{user.id}</code>\n"
    out += f"<b>EmailId:</b> <code>{email_id}</code>\n"
    await bot.send_message(config.get('admin_chat'),out)
    await message.reply("Aight, we received your application now be patient and wait for approval (approval process take upto a week).")

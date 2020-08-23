from tgbot import dp
from tgbot.utils.db_utils import isUserBanned,addBanUser,removeBanUser
from tgbot.utils.filters import sudoUserFilter
from tgbot.utils.bot_utils import extractUserId, isUserSudo

@dp.message_handler(sudoUserFilter,commands=['ban'])
async def banUser(message):
    userId = extractUserId(message)
    if not userId:
        return await message.reply("Provide a userId bruh!")
    if isUserSudo(userId):
        return await message.reply("Cant ban this user, *runs away*")
    if isUserBanned(userId):
        return await message.reply("User is already banned bruh!")
    await addBanUser(userId)
    await message.reply(f"<b>Banned User:</b> <code>{userId}</code>")

@dp.message_handler(sudoUserFilter,commands=['unban'])
async def unBanUser(message):
    userId = extractUserId(message)
    if not userId:
        return await message.reply("Provide a userId bruh!")
    if isUserSudo(userId):
        return await message.reply("Bruh moment, *runs away*")
    if not isUserBanned(userId):
        return await message.reply("User isnt banned in the first place bruh!")
    await removeBanUser(userId)
    await message.reply(f"<b>UnBanned User:</b> <code>{userId}</code>")
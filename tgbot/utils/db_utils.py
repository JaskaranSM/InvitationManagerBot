from tgbot import config,LOGGER, BANNED_USERS
from motor.motor_asyncio import AsyncIOMotorClient



def getClient(mongo_uri):
    return AsyncIOMotorClient(mongo_uri)

db_client = getClient(config.get('mongo_uri'))

db = db_client['test']

bannedUserDb = db.bannedUserDb


async def addBanUser(userId):
    LOGGER.info(f"Banning User: {userId}")
    try:
        result = await bannedUserDb.insert_one({"userId":userId})
        LOGGER.info(result)
    except Exception as e:
        LOGGER.error(e)
        return False
    BANNED_USERS.append(userId)
    return True

async def removeBanUser(userId):
    LOGGER.info(f"UnBanning User: {userId}")
    try:
        result = await bannedUserDb.delete_one({"userId":userId})
        LOGGER.info(result)
    except Exception as e:
        LOGGER.error(e)
        return False 
    BANNED_USERS.remove(userId)
    return True

async def getAllBannedUsers():
    users = []
    try:
        async for user in bannedUserDb.find({}):
            LOGGER.info(f"Adding {user.userId} in banned.")
            users.append(user.userId)
    except Exception as e:
        LOGGER.error(e)
    return users

def isUserBanned(userId):
    return userId in BANNED_USERS

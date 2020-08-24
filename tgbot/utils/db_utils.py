from tgbot import config,LOGGER, BANNED_USERS
from motor.motor_asyncio import AsyncIOMotorClient



def getClient(mongo_uri):
    return AsyncIOMotorClient(mongo_uri)

db_client = getClient(config.get('mongo_uri'))

db = db_client['test']

bannedUserDb = db.bannedUserDb
accessUserDb = db.accessUserDb


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

async def addAccessUser(userId,email):
    LOGGER.info(f"Adding {userId} : {email}")
    try:
        result = await accessUserDb.insert_one({"userId":userId,"email":email})
        LOGGER.info(result)
    except Exception as e:
        LOGGER.error(e)
        return False 
    return True

async def isUserInDb(userId):
    LOGGER.info(f"Checking {userId} in db")
    try:
        result = await accessUserDb.find_one({"userId":userId})
        LOGGER.info(result)
        if result is None:
            return False
    except Exception as e:
        LOGGER.error(e)
        return False
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

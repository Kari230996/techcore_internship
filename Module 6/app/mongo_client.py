from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"

MONGO_URL = "mongodb://root:example@localhost:27017/?authSource=admin"

client = AsyncIOMotorClient(MONGO_URL)

mongo_db = client["books_mongo_db"]

books_collection = mongo_db["books"]

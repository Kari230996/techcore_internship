import asyncio
from app.mongo_client import books_collection


async def test_mongo_connection():
    test_doc = {"title": "Test Book", "author": "Test Author", "year": 2023}
    result = await books_collection.insert_one(test_doc)
    print("Документ добавлен, ID:", result.inserted_id)

    doc = await books_collection.find_one({"_id": result.inserted_id})
    print("Найден документ:", doc)

if __name__ == "__main__":
    asyncio.run(test_mongo_connection())

from bson import ObjectId

from app.mongo_client import reviews_collection


class ReviewRepository:

    @staticmethod
    async def create(review_data: dict):
        result = await reviews_collection.insert_one(review_data)
        return str(result.inserted_id)

    @staticmethod
    async def get_for_product(product_id: int):
        cursor = reviews_collection.find({"product_id": product_id})
        reviews = [doc async for doc in cursor]
        for r in reviews:
            r["_id"] = str(r["_id"])
        return reviews

    @staticmethod
    async def update_review(review_id: str, data: dict):
        result = await reviews_collection.update_one(
            {"_id": ObjectId(review_id)}, {"$set": data}
        )
        return result.modified_count > 0

    @staticmethod
    async def delete_review(review_id: str):
        result = await reviews_collection.delete_one({"_id": ObjectId(review_id)})
        return result.deleted_count > 0

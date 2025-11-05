from fastapi import APIRouter

router = APIRouter(prefix="/api/hello", tags=["Другие"])


@router.get("/")
async def hello():
    return {"message": "Hello, World!"}

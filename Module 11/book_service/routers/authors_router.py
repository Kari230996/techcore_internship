from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db_session
from models import Author
from schemas.authors_schemas import AuthorCreate

router = APIRouter()


@router.post("/authors")
async def create_author(author: AuthorCreate, db: AsyncSession = Depends(get_db_session)):
    new_author = Author(name=author.name)
    db.add(new_author)
    await db.commit()
    await db.refresh(new_author)
    return new_author

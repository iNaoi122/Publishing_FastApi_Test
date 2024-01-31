from typing import List, Any

from sqlalchemy import select, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.author import Author
from db.models.publish import Publish

from utils.password_utils import verify_password


class R_DB:

    @staticmethod
    async def read_author(author_username: str, session: AsyncSession) -> Author:
        return await session.scalar(select(Author).where(Author.username == author_username))

    @staticmethod
    async def read_publish(session: AsyncSession, top: bool = False) -> ScalarResult[Publish]:
        return await session.scalars(
            select(Publish, Author).join(Author, Publish.author_id == Author.id).order_by(Publish.post_data).limit(10))

    @staticmethod
    async def auth_author(username: str, password: str, session: AsyncSession) -> bool | Author:
        author: Author = await session.scalar(select(Author).where(Author.username == username))
        if not author:
            return False
        if not verify_password(password, author.hashed_password):
            return False
        return author

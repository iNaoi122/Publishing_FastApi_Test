from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.author import Author

from utils.password_utils import verify_password


class R_DB:

    @staticmethod
    async def read_author(author_id: str, session: AsyncSession) -> Author:
        return await session.scalar(select(Author).where(Author.id == author_id))

    @staticmethod
    async def read_publish(top: bool = False):
        pass

    @staticmethod
    async def auth_author(username: str, password: str, session: AsyncSession) -> bool:
        author: Author = await session.scalar(select(Author).where(Author.username == username))
        if not author:
            return False
        if not verify_password(password, author.hashed_password):
            return False
        return author

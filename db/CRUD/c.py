import logging

from sqlalchemy.ext.asyncio import AsyncSession

from db.models.author import Author
from db.models.publish import Publish

from utils.password_utils import get_password_hash


class C_DB:

    @staticmethod
    async def add_author(username: str, password: str, session: AsyncSession):
        try:
            author = Author(username=username, hashed_password=get_password_hash(password))
            session.add(author)
            await session.commit()
            await session.refresh(author)
        except Exception as e:
            logging.error(e)

    @staticmethod
    async def add_publishing(text: str, author: Author, session: AsyncSession):
        try:
            publishing = Publish(text=text, author_id=author.id)
            session.add(publishing)

            await session.commit()
            await session.refresh(publishing)
        except Exception as e:
            logging.error(e)

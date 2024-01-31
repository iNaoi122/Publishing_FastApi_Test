import logging

from sqlalchemy.ext.asyncio import AsyncSession

from db.models.author import Author
from db.models.publish import Publish


class C_DB:

    @staticmethod
    async def add_author(username: str, session: AsyncSession):
        try:
            author = Author(username=username)
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

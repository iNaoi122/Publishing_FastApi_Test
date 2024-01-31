import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.models.author import Author
from db.models.publish import Publish


class U_DB:

    @staticmethod
    async def update_vote(publishing_id: int, vote: bool, session: AsyncSession):
        publishing: Publish = await session.scalar(select(Publish).where(Publish.id == publishing_id))
        try:
            if vote:
                publishing.plus_vote = publishing.plus_vote + 1
            else:
                publishing.minus_vote = publishing.minus_vote + 1
        except Exception as e:
            logging.error(e)
        finally:
            await session.commit()

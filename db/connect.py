from typing import AsyncIterator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from db.models.base import Base


class ConnectDB:
    def __init__(self):
        self._sql_echo = True
        self._async_memory_engine = create_async_engine("sqlite+aiosqlite:///authors.db", echo=self._sql_echo)
        self._async_sessionmaker = async_sessionmaker(self._async_memory_engine)

    async def init_db(self):
        async with self._async_memory_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def __call__(self) -> AsyncIterator[AsyncSession]:
        assert self._async_sessionmaker
        async with self._async_sessionmaker() as session:
            yield session

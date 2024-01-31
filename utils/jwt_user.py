from fastapi import HTTPException
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from db.CRUD.crud import CRUD


async def check_user_in_db_by_token(username: str, session: AsyncSession):
    author = await CRUD.read_author(username, session)
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return author
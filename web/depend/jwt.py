import os
from typing import Annotated
from datetime import datetime, timezone, timedelta

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException

from dotenv import load_dotenv

from jose import JWTError, jwt


class JWT:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    load_dotenv()

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
        return encoded_jwt

    @staticmethod
    async def get_current_user_by_token(token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
            username: str = payload.get("username")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        return username

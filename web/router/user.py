import logging
from typing import Annotated

from datetime import timedelta

from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from web.schemas.user import UserReg
from web.schemas.token import Token

from web.depend.jwt import JWT

from db.connect import ConnectDB
from db.CRUD.crud import CRUD

user_router = APIRouter()
conn = ConnectDB()


@user_router.post("/token")
async def token(data: Annotated[OAuth2PasswordRequestForm, Depends()], session=Depends(conn)) -> Token:
    author = await CRUD.auth_author(data.username, data.password, session)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = JWT.create_access_token(data={"username": author.username}, expires_delta=timedelta(minutes=30))
    return Token(access_token=access_token, token_type="bearer")


@user_router.post("/registration", tags=["account"])
async def registration(request: Request, user_info: UserReg, session=Depends(conn)):
    try:
        await CRUD.add_author(user_info.name, user_info.password, session)
        return JSONResponse(status_code=200, content={"msg": "User was created"})
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"msg": "Some error"})

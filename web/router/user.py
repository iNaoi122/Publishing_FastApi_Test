import logging

from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse

from web.schemas.user import UserReg

from db.connect import ConnectDB
from db.CRUD.c import C_DB

user_router = APIRouter()
conn = ConnectDB()


@user_router.post("/token")
async def token()

@user_router.post("/registration", tags=["account"])
async def registration(request: Request, user_info: UserReg, session=Depends(conn)):
    try:
        await C_DB.add_author(user_info.name, session)
        return JSONResponse(status_code=200, content={"msg": "User was created"})

    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"msg": "Some error"})

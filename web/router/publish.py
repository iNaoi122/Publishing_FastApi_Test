import logging
from typing import List

from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse

from web.schemas.publish import Publish

from db.connect import ConnectDB
from db.CRUD.crud import CRUD
publish_router = APIRouter()
conn = ConnectDB()


@publish_router.post("/add", tags=["publish"])
async def add_text(request: Request, text: str, session=Depends(conn)):
    try:
        await CRUD.add_publishing(text=text, author=await CRUD.read_author("1", session), session=session)
        return JSONResponse(status_code=200, content={"msg": "Publish was created"})

    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"msg": "Some error"})


@publish_router.get("/publishes", response_model=List[Publish])
async def publishes(request: Request, top: bool = False):
    try:
        return JSONResponse(status_code=200, content={"publishes": []})
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"msg": "Some error"})


@publish_router.get("/vote")
async def vote_for_publish(request: Request, publish_id: str, vote_up: bool):
    try:
        return JSONResponse(status_code=200, content={"publishes": []})
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"msg": "Some error"})

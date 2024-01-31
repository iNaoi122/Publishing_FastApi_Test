import logging
from typing import List, Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

import db.schemas.publishing
from web.depend.jwt import JWT
from utils.jwt_user import check_user_in_db_by_token

from web.schemas.publish import Publish
from web.schemas.user import User
from pydantic import parse_obj_as

from db.connect import ConnectDB
from db.CRUD.crud import CRUD

publish_router = APIRouter()
conn = ConnectDB()


@publish_router.post("/add", tags=["publish"], response_model=List[db.schemas.publishing.PublishingView])
async def add_text(current_user_name: Annotated[User, Depends(JWT.get_current_user_by_token)], text: str,
                   session=Depends(conn)):
    # fixme Ошибка в модели User, не видит переменные класса
    try:
        author = await check_user_in_db_by_token(current_user_name, session)
        if author:
            await CRUD.add_publishing(text=text, author=await CRUD.read_author(current_user_name, session),
                                      session=session)
            return JSONResponse(status_code=200, content={"msg": "Publish was created"})
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"msg": "Some error"})


@publish_router.get("/publishes", response_model=List[Publish])
async def publishes(top: bool = False,
                    session=Depends(conn)):
    try:
        publishes = await CRUD.read_publish(session)
        return [Publish(text=pub.text, date=pub.post_data,
                        author=pub.author.username, count_votes=int(pub.plus_vote)+int(pub.minus_vote),
                        rating=int(pub.plus_vote)-int(pub.minus_vote)) for pub in publishes]
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"msg": "Some error"})


@publish_router.get("/vote")
async def vote_for_publish(current_user_name: Annotated[User, Depends(JWT.get_current_user_by_token)],
                           publish_id: int, vote_up: bool, session=Depends(conn)):
    try:
        await check_user_in_db_by_token(current_user_name, session)

        await CRUD.update_vote(publishing_id=publish_id, vote=vote_up, session=session)

        return JSONResponse(status_code=200, content={"publishes": []})
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"msg": "Some error"})

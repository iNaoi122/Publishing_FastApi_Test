import logging

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

token_router = APIRouter()


@token_router.post("/token")
async def token(request: Request):
    try:
        return JSONResponse(status_code=200, content={"msg": "Token create"})
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"msg": "Some error"})

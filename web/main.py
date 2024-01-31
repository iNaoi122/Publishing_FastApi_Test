import logging

from fastapi import FastAPI

from web.router.publish import publish_router
from web.router.user import user_router

from db.connect import ConnectDB

logging.basicConfig()

conn = ConnectDB()
app = FastAPI(title="Publishing")


@app.on_event("startup")
async def start_up():
    await conn.init_db()


app.include_router(publish_router)
app.include_router(user_router)

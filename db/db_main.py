import asyncio

from db.connect import DB


if __name__ == '__main__':
    a = DB()
    asyncio.run(a.init_db())

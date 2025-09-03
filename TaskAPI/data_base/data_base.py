from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import dotenv_values

from models import Base, DB_Task


config = dotenv_values(".env")

async_engine = create_async_engine(config.get('DB_CONNECT'), echo=True)

session = async_sessionmaker(async_engine)

async def create_tables() -> None:
    """
    This function creates the tables in the database
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await async_engine.dispose()

async def create_task() -> None:
    """
    This function creates the tasks in the database
    """
    async with session() as sess:
        sess.add_all([])
        await sess.commit()

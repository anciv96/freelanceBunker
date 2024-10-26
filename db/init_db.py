from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config.config import DB_FILE_PATH
from models.base import Base


engine = create_async_engine(f"sqlite+aiosqlite:///{DB_FILE_PATH}", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def init_db() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

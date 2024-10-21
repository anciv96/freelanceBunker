from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.business_logic.db.models import Base


engine = create_async_engine("sqlite+aiosqlite:///app/business_logic/db/projects.db", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def init_db() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

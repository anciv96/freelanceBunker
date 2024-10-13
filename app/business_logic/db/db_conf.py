from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

engine = create_async_engine("sqlite+aiosqlite:///app/business_logic/db/projects.db", echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

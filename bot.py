import asyncio

from selenium import webdriver

from app.business_logic.db.db_conf import engine, async_session
from app.business_logic.repository.kwork_repository import ProjectRepository
from app.business_logic.services.kwork.filter import Filter
from app.business_logic.services.kwork.scraper import KworkScraper
from app.config import URLS
from app.business_logic.db.models import Base


async def init_db() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def run_kwork_parser():
    driver = webdriver.Chrome()
    kwork = KworkScraper(URLS, driver)
    kwork_projects = await kwork.get_projects()

    for r in kwork_projects:
        print(r)


async def main() -> None:
    await init_db()
    await run_kwork_parser()


if __name__ == "__main__":
    asyncio.run(main())

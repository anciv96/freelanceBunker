import asyncio


from app.business_logic.db.init_db import init_db
from app.business_logic.services.kwork.scraper import KworkScraper
from app.config import URLS
from app.telergam_bot.handlers.notifier import send_message


async def run_parsers():
    all_scrapers_list = [KworkScraper(URLS)]
    while True:
        all_projects = await _get_all_projects(all_scrapers_list)
        for project in all_projects:
            await send_message(project)

        await asyncio.sleep(10)


async def _get_all_projects(all_scrapers_list):
    all_projects = []
    for scraper in all_scrapers_list:
        projects = await scraper.get_projects()
        for project in projects:
            if project:
                all_projects.append(project)

    return all_projects


async def main() -> None:
    await init_db()
    await run_parsers()


if __name__ == "__main__":
    asyncio.run(main())

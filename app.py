import asyncio

from bot import AggregatorBot
from config.config import URLS
from config.dispatcher import scheduler
from handlers.notifier import send_message
from db.init_db import init_db
from sources.kwork.scraper import KworkScraper
from config.logger_setup import get_logger


logger = get_logger(__name__)


async def run_parsers():
    bot = AggregatorBot()
    bot.add_parser(KworkScraper(URLS))
    data = await bot.collect_data()

    await _send_messages(data)

    return data


async def _send_messages(projects: list[dict[str, str]]):
    for project in projects:
        await send_message(project)


async def main():
    await init_db()
    scheduler.add_job(run_parsers, "interval", seconds=30, jitter=10, replace_existing=False, max_instances=1)
    scheduler.start()

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())

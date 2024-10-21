from app.business_logic.db.init_db import async_session
from app.business_logic.repository.kwork_repository import ProjectRepository
from app.business_logic.services.base_scraper import Scraper
from app.business_logic.services.browser_manager import WebDriverManager
from app.business_logic.services.kwork.converter import KworkConverter
from app.business_logic.services.kwork.filter import Filter
from app import logger_setup


logger = logger_setup.get_logger(__name__)


class KworkScraper(Scraper):
    """Класс для скрейпинга проектов с Kwork на основе категорий."""
    def __init__(self, categories: list[str]):
        """
        Args:
            categories (list[str]): Список категорий для скрейпинга.
        """
        self.categories: list[str] = categories
        self.web_driver_manager: WebDriverManager = WebDriverManager()
        self.parser: KworkConverter = KworkConverter()

    async def get_projects(self) -> list[dict[str, str]]:
        """Получает список проектов для всех категорий.

        Returns:
            list[dict[str, str]]: Список словарей с данными о проектах.
        """
        logger.info('Scraping...')
        result: list[dict[str, str]] = []
        for category in self.categories:
            page_source: str = await self.web_driver_manager.fetch_page_source(url=category)
            all_projects: list[dict[str, str]] = await self.parser.convert(page_source)
            new_projects: list[dict[str, str]] = await self._get_filtered_projects(all_projects)

            result.extend(new_projects)
        return result

    async def _get_filtered_projects(self, all_projects: list[dict[str, str]]) -> list[dict[str, str]]:
        async with async_session() as session:
            repository = ProjectRepository(session)
            filter_projects = Filter(repository)

            high_cost_projects = await filter_projects.filter_low_cost_project(all_projects)
            new_projects = await filter_projects.filter_old_projects(high_cost_projects)

            return new_projects

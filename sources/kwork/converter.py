import logging

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class KworkConverter:
    """Класс для парсинга HTML-кода страницы и извлечения данных о проектах."""

    @staticmethod
    async def convert(html: str) -> list[dict[str, str]]:
        """Парсит HTML-код и извлекает данные о проектах.

        Args:
            html (str): HTML-код страницы.

        Returns:
            list[dict[str, str]]: Список словарей с данными о проектах.
        """
        soup = BeautifulSoup(html, "html.parser")
        projects = soup.find_all('div', attrs={'class': 'want-card'})
        return [
            await KworkConverter._extract_project_data(p) for p in projects
        ]

    @staticmethod
    async def _extract_project_data(project: BeautifulSoup) -> dict[str, str]:
        """Извлекает данные о проекте из HTML-элемента.

        Args:
            project (BeautifulSoup): HTML-элемент, представляющий проект.

        Returns:
            dict[str, str]: Словарь с данными о проекте.
        """
        try:
            title_tag = project.find('h1', attrs={'class': 'wants-card__header-title'})
            title = title_tag.text if title_tag else ''
            url = 'https://kwork.ru' + title_tag.find('a').get('href') if title_tag else ''
            description = project.find('div', attrs={'class': 'wants-card__description-text'}).text or ''
            price = project.find('div', attrs={'class': 'wants-card__description-higher-price'}).text or ''
        except AttributeError:
            return {}
        return {
            'title': title,
            'url': url,
            'description': description,
            'price': price,
        }


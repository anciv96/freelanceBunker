from abc import ABC, abstractmethod


class Scraper(ABC):
    """Абстрактный базовый класс для скрейперов."""

    @abstractmethod
    def get_projects(self) -> list[dict[str, str]]:
        """Метод для получения списка проектов.

        Returns:
            list[dict[str, str]]: Список словарей, содержащих информацию о проектах.
        """

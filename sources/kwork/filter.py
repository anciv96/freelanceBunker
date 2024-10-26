import re

from repository.kwork_repository import ProjectRepository


class Filter:
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    async def filter_old_projects(self, projects: list[dict[str, str]]):
        """Фильтрует уже отправленные проекты

        Args:
            projects (list[dict[str, str]]): Список всех проектов.

        Returns:
            list[dict[str, str]]: Возвращает уже отфильтрованные данные.
        """
        new_list = []
        for project in projects:
            url = project.get('url')
            if not await self.repository.project_exists(url) and url:
                new_list.append(project)
                await self.repository.add_new_project(url)

        return new_list

    @staticmethod
    async def filter_low_cost_project(projects: list[dict[str, str]]):
        new_list = []
        for project in projects:
            text = project.get('price', '0')
            match = re.search(r'\d{1,3}(?:\s\d{3})*', text)

            if match:
                number = int(match.group(0).replace(' ', ''))
                if number >= 15_000:
                    new_list.append(project)
        return new_list

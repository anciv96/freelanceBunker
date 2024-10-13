from app.business_logic.repository.kwork_repository import ProjectRepository


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
            url = project['url']
            if not await self.repository.project_exists(url):
                new_list.append(project)
                await self.repository.add_new_project(url)

        return new_list


from sqlalchemy import select
from sqlalchemy.exc import StatementError
from sqlalchemy.ext.asyncio import AsyncSession

from app.business_logic.db.models import Project
from app import logger_setup


logger = logger_setup.get_logger(__name__)


class ProjectRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_new_project(self, url: str = None) -> None:
        """Добавляет новый проект в базу данных

        Args:
            url (str): url проекта.
        """
        async with self.session.begin():
            try:
                new_project = Project(url=url)

                self.session.add(new_project)
                await self.session.commit()
            except StatementError as error:
                await self.session.rollback()
                logger.error(f"Error adding new project: {error}")

    async def project_exists(self, url: str) -> bool:
        """
        Проверяет существует ли проект в базе данных.

        Args:
            url (str): url проекта, которую нужно проверить.

        Returns:
             bool
        """
        async with self.session.begin():
            project = await self.session.execute(
                select(Project).where(Project.url == url)
            )
            return bool(len(project.scalars().all()))

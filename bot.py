from typing import List, Dict

from parsers.base_scraper import Scraper


class AggregatorBot:
    def __init__(self):
        self.parsers = []

    def add_parser(self, parser: Scraper):
        """Добавляет новый парсер"""
        self.parsers.append(parser)

    async def collect_data(self) -> List[Dict[str, str]]:
        all_data = []
        for parser in self.parsers:
            projects = await parser.get_projects()
            all_data.extend(projects)
        return all_data

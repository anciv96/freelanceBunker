from selenium.webdriver.chrome.webdriver import WebDriver


class WebDriverManager:
    """Класс для управления WebDriver и получения HTML-кода страницы."""

    def __init__(self, driver: WebDriver):
        """
        Args:
            driver (WebDriver): Экземпляр WebDriver для управления браузером.
        """
        self.driver: WebDriver = driver

    async def fetch_page_source(self, url: str) -> str:
        """Получает исходный код страницы по указанному URL.

        Args:
            url (str): URL страницы.

        Returns:
            str: Исходный HTML-код страницы.
        """
        self.driver.get(url)
        return self.driver.page_source


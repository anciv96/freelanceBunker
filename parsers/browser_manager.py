from selenium.common import WebDriverException
from selenium.webdriver import Chrome

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


class WebDriverManager:
    """Класс для управления WebDriver и получения HTML-кода страницы."""

    async def fetch_page_source(self, url: str) -> str:
        """Получает исходный код страницы по указанному URL.

        Args:
            url (str): URL страницы.

        Returns:
            str: Исходный HTML-код страницы.
        """

        chrome_options = await self._get_options()
        driver: WebDriver = Chrome(options=chrome_options)

        try:
            driver.get(url)
        except WebDriverException:
            driver.quit()
            driver = Chrome(options=chrome_options)
            driver.get(url)

        return driver.page_source

    async def _get_options(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--remote-debugging-port=9222')
        chrome_options.add_argument('--disable-software-rasterizer')
        chrome_options.add_argument('--disable-crash-reporter')
        chrome_options.add_argument('--disable-extensions')

        return chrome_options

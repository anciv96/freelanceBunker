from os import getenv
from dotenv import load_dotenv

load_dotenv()

URLS = [
    'https://kwork.ru/projects?a=1&fc=41',
]
TOKEN = getenv("BOT_TOKEN")
ADMIN_IDS = [238558039]

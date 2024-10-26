from os import getenv
from dotenv import load_dotenv


load_dotenv()

URLS = [
    'https://kwork.ru/projects?a=1&fc=41',
    'https://kwork.ru/projects?a=1&fc=37',
]
TOKEN = getenv("BOT_TOKEN")
ADMIN_IDS = getenv("ADMIN_IDS").split(',')
DB_FILE_PATH = 'db/projects.db'

from app.dispatcher import bot
from app.config import ADMIN_IDS


async def _make_message_text(project: dict[str, str]) -> str:
    message_text = f'<b>{project.get("title", "")}</b>\n'
    message_text += f'{project.get("description", "")}\n'
    message_text += f'{project.get("price", "").replace("\n", "")}\n'
    message_text += f'{project.get("url", "")}\n\n'

    return message_text


async def send_message(project: dict[str, str]) -> None:
    message_text = await _make_message_text(project)
    for admin in ADMIN_IDS:
        await bot.send_message(chat_id=admin, text=message_text, disable_web_page_preview=True)

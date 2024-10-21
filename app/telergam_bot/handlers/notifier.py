from app.dispatcher import bot

msg = {
    'title': 'title',
    'url': 'url',
    'description': 'description',
    'price': 'price',
}


async def _make_message_text(message: dict):
    message_text = f'Н<b>{message["title"]}</b>'


async def send_message(message) -> None:
    await bot.send_message(text=message)

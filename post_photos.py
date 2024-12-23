from time import sleep

import telegram
from send_photo import send_photo


def post_photos(
    bot: 'telegram.bot.Bot',
    chat_id: str,
    delay: int | float,
    photos_file_info: dict[str]
     ) -> None:

    while True:
        send_photo(bot, chat_id, photos_file_info)
        sleep(delay * 3600)

import telegram


def send_photo(
    bot: 'telegram.bot.Bot',
    chat_id: str,
    photo_info: dict[str],
     ) -> None:
    with open(photo_info['photo_path'], 'rb') as path_photo:
        bot.send_photo(
            chat_id,
            photo=path_photo,
            caption=photo_info['photo_name']
        )

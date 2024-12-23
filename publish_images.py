import os
from pathlib import Path

import telegram
from arg_parser import create_parser
from dotenv import load_dotenv
from photo_utils import (get_photo_at_index, get_random_photo)
from post_photos import post_photos


def main():
    load_dotenv()
    token_tg = os.getenv('TG_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')
    bot = telegram.Bot(token_tg)
    delay = 4
    base_dir = Path(__file__).parent / 'images'
    parser = create_parser()
    parsed_args = parser.parse_args()
    photo_names = [photo.name for photo in base_dir.iterdir()]
    photo_info = (
        get_random_photo(base_dir, photo_names)
        if not parsed_args.n
        else get_photo_at_index(photo_names, parsed_args.n)
    )
    post_photos(bot, chat_id, delay, photo_info)


if __name__ == '__main__':
    main()

import os
from pathlib import Path

from arg_parser import create_parser
from dotenv import load_dotenv
from load_spacex_images import get_spacex_launch_images
from load_epic_images import get_epic_images
from load_nasa_images import get_nasa_images
from save_photos import save_photos


def main():
    load_dotenv()
    token = os.getenv('NASA_API_KEY')
    base_dir = Path(__file__).parent / 'images'
    base_dir.mkdir(exist_ok=True)
    parser = create_parser()
    parsed_args = parser.parse_args()
    photos_spacex = get_spacex_launch_images(parsed_args.id)
    photos_nasa = get_nasa_images(token, parsed_args.q)
    photos_epic = get_epic_images(token)
    save_photos(base_dir, (*photos_spacex, *photos_nasa, *photos_epic))


if __name__ == '__main__':
    main()

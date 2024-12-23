from pathlib import Path
from random import choice


def get_random_photo(base_dir: Path, photos_name: list[str]) -> dict[str]:
    photo_name = choice(photos_name)
    return {
        'photo_name': photo_name,
        'photo_path': base_dir/photo_name
        }


def get_photo_at_index(photos_name: list[str], photo_index: str) -> dict[str]:
    return {
        'photo_name': photos_name[int(photo_index)],
        'photo_path': f'images/{photos_name[int(photo_index)]}'
        }

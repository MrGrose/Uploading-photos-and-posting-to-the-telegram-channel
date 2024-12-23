from pathlib import Path


def save_photos(base_dir: Path, photo_bytes: tuple[bytes]) -> None:
    for number, photo in enumerate(photo_bytes, 1):
        with open(base_dir / f'photo_{number}.jpg', 'wb') as file:
            file.write(photo)

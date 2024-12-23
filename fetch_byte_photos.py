import requests


def get_byte_photo(photo_url: str, params: dict[str] = None) -> bytes:
    byte_photo = requests.get(photo_url, params=params)
    byte_photo.raise_for_status()
    return byte_photo.content

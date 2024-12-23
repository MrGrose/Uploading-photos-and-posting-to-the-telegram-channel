import random

import requests
from fetch_byte_photos import get_byte_photo


def get_spacex_launch_images(launch_id: None) -> list[bytes]:
    photo_urls = []
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}' if launch_id else 'https://api.spacexdata.com/v5/launches'
    response = requests.get(url)
    response.raise_for_status()
    if launch_id:
        photo_urls = response.json()['links']['flickr']['original']
    else:
        original_links = [
            link['links']['flickr']['original'] for link in
            response.json() if link['links']['flickr']['original']
            ]
        photo_urls = random.choice(original_links) if original_links else []
    return [get_byte_photo(photo_url) for photo_url in photo_urls]

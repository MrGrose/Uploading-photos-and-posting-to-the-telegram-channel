import os

import requests
from fetch_byte_photos import get_byte_photo


def get_nasa_images(token: str, quantity: int) -> list[bytes]:
    param = {'count': quantity,
             "api_key": token}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=param)
    response.raise_for_status()
    nasa_content = response.json()
    return [
        get_byte_photo(photo_url_nasa['url'])
        for photo_url_nasa in nasa_content
        if os.path.splitext(photo_url_nasa['url'])[1].lower() in ['.jpg', '.jpeg', '.png', '.gif']
    ]

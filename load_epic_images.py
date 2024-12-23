import requests
from fetch_byte_photos import get_byte_photo


def get_epic_images(token: str) -> list[bytes]:
    param = {"api_key": token}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=param)
    response.raise_for_status()
    epic_content = response.json()
    return [
        get_byte_photo(f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{epic_dates["image"]}.png', param)
        for epic_dates in epic_content
        for year, month, day in [epic_dates['date'].split()[0].split('-')]
    ]

# Космический Телеграм
Данный скрипт предназначен для публикации космических фотографий в Telegram канал.

## Описание
Скрипт предоставляет следующие:
- Скачивает фото запуска SpaceX.
- Скачивает EPIC-фото от NASA.
- Скачивает APOD-фото от NASA.
- Публикует указанную фотографию в тг канал. Если “какую” не указано, публикует случайную фотографию из скаченной директории.
- Публикует все фото из директории в бесконечном цикле.
- Вспомогательные скрипты.

## Основные компоненты
Скрипт **download_images**: Загружает изображения из различных источников (SpaceX, NASA APOD, NASA EPIC).

Скрипт **publish_images**: Публикует изображение в Telegram канал с заданным диапазоном времени.

## Вспомогательные скрипты
- arg_parser: запускает скрипт main через консоль.
- load_spacex_images: загружает фотографии запусков SpaceX.
- load_epic_images: загружает изображения Земли из API NASA EPIC (Earth Polychromatic Imaging Camera).
- load_nasa_images: загружает изображения дня (APOD - Astronomy Picture of the Day) с API NASA
- fetch_byte_photos: загружает фотографии по ссылке и возвращает их в виде байтов.
- save_photos: сохраняет фотографии в директорию.
- photo_utils: получение информации о фотографиях.
- post_photos: запускает бесконечный цикла для запуска публикаций.
- send_photo: отправки фотографий в Telegram.


## Как установить
1. Создайте Telegram бота и получите токен бота. Инструкции можно найти [здесь](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html), 
2. Получите API ключ NASA для скачивания фото с сайта api.nasa.gov.
3. Создайте файл .env в корневой директории проекта со следующим содержимым:

    ```bash
    NASA_API_KEY=ваш_api_ключ_nasa
    TG_TOKEN=ваш_токен_telegram_бота
    TG_CHAT_ID=ваш_id_telegram_канала
    ```

4. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```
    
5. Добавьте вашего Telegram бота в канал для публикации. Инструкции [здесь](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)


## Использование
1. Для запуска скачивания фотографий необходимо запустить скрипт download_images.py, он загрузит фотографии в директорию images (она создастся в области запуска главного скрипта)
2. Запустите программу через командную строку:

    2.1. Без дополнительных параметров (рекомендуется):
    ```bash
    python download_images.py
    ```
    
    2.2. С параметром -id для скачивания определенного запуска SpaceX:
    ```bash
    python download_images.py -id 5eb87d47ffd86e000604b38a
    ```

    2.3. С параметром -q для указания количества APOD-фото:
    ```bash
    python download_images.py -q 5
    ```


3. Для запуска публикации фотографий в Telegram канал:

    3.1. Без дополнительных параметров (рекомендуется), начнется публикацию фото из директории скаченных фотографий в случайном порядке:
    ```bash
    python publish_images.py
    ```

    3.2. С параметром -n для указания индекса фото для отправки в Telegram канал:
    ```bash
    python publish_images.py -n 10
    ```
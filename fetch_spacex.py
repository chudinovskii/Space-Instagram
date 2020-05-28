import requests
import shutil
from PIL import Image
from pathlib import Path


def download_pic(url, filename, path_to_save):
    resp = requests.get(url)
    resp.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(resp.content)
    shutil.move(filename, f'{path_to_save}/{filename}')
    size = 1080, 1080
    path_to_file = f'{path_to_save}/{filename}'
    image = Image.open(path_to_file)
    image.thumbnail(size)
    image.save(path_to_file, format='JPEG')


def get_spacex_photo_urls():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    resp = requests.get(url)
    resp.raise_for_status()
    decoded_resp = resp.json()
    urls_list = decoded_resp['links']['flickr_images']
    return urls_list


def fetch_spacex_last_launch_pics(urls_list):
    path_to_save = 'images'
    for url_number, url in enumerate(urls_list):
        filename = f'spacex{url_number}.jpg'
        download_pic(url, filename, path_to_save)
        print(f'{filename} downloaded.')


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    urls_list = get_spacex_photo_urls()
    fetch_spacex_last_launch_pics(urls_list)


if __name__ == '__main__':
    main()

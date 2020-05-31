import requests
from PIL import Image


def download_pic(url, path_to_file):
    resp = requests.get(url)
    resp.raise_for_status()
    with open(path_to_file, 'wb') as file:
        file.write(resp.content)


def resize(path_to_file):
    size = 1080, 1080
    image = Image.open(path_to_file)
    image.thumbnail(size)
    image.save(path_to_file, format='JPEG')

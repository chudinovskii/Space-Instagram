import requests
import service_scripts
from pathlib import Path


def get_spacex_photo_urls():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    resp = requests.get(url)
    resp.raise_for_status()
    decoded_resp = resp.json()
    urls = decoded_resp['links']['flickr_images']
    return urls


def fetch_spacex_last_launch_pics(urls):
    for url_number, url in enumerate(urls):
        path_to_file = Path.cwd().joinpath('images', f'spacex{url_number}.jpg')
        service_scripts.download_pic(url, path_to_file)
        service_scripts.resize(path_to_file)


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    urls = get_spacex_photo_urls()
    fetch_spacex_last_launch_pics(urls)


if __name__ == '__main__':
    main()

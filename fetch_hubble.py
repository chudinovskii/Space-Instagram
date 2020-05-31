import requests
import service_scripts
from pathlib import Path


def get_hubble_img_urls(id):
    url = f'http://hubblesite.org/api/v3/image/{id}'
    resp = requests.get(url)
    resp.raise_for_status()
    decoded_resp = resp.json()
    images = decoded_resp['image_files']
    image_all_urls = [image['file_url'] for image in images]
    return image_all_urls


def fetch_hubble_images_by_id(id):
    best_resolution_url = get_hubble_img_urls(id)[-1]
    url = f'https:{best_resolution_url}'
    extension = Path(url).suffix
    filename = f'image_{id}{extension}'
    path_to_file = Path.cwd().joinpath('images', filename)
    download_script.download_pic(url, path_to_file)
    return filename, path_to_file


def get_hubble_images_collections():
    url = f'http://hubblesite.org/api/v3/images?page=all'
    resp = requests.get(url)
    resp.raise_for_status()
    decoded_resp = resp.json()
    collections = []
    for image in decoded_resp:
        if image['collection'] not in collections:
            collections.append(image['collection'])
    return f'Available collections: {collections}'


def get_hubble_images_id(collection):
    url = f'http://hubblesite.org/api/v3/images/{collection}'
    resp = requests.get(url)
    resp.raise_for_status()
    decoded_resp = resp.json()
    ids = [image['id'] for image in decoded_resp]
    return ids


def fetch_hubble_images_from_collection(collection):
    ids = get_hubble_images_id(collection)
    for id in ids:
        try:
            filename, path_to_file = fetch_hubble_images_by_id(id)
            service_scripts.resize(path_to_file)
        except Exception:
            print(f'While downloading pic by {id} an error occurred')


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    print(get_hubble_images_collections())
    collection = input("Please, choose the collection from above: ")
    fetch_hubble_images_from_collection(collection)


if __name__ == '__main__':
    main()

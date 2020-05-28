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


def get_hubble_img_urls(id):
    url = f'http://hubblesite.org/api/v3/image/{id}'
    resp = requests.get(url)
    resp.raise_for_status()
    decoded_resp = resp.json()
    images = decoded_resp['image_files']
    image_urls = [image['file_url'] for image in images]
    return image_urls


def get_img_extension(url):
    url = url.split('/')
    extension = url[-1].split('.')[-1]
    return extension


def fetch_hubble_images_by_id(id):
    path_to_save = 'images'
    url = f'https:{get_hubble_img_urls(id)[-1]}'
    extension = get_img_extension(url)
    filename = f'image_{id}.{extension}'
    download_pic(url, filename, path_to_save)
    return filename


def get_hubble_images_collections():
    print('Forming the list of collections...')
    url = f'http://hubblesite.org/api/v3/images?page=all'
    resp = requests.get(url)
    resp.raise_for_status()
    decoded_resp = resp.json()
    list_of_collections = []
    for image in decoded_resp:
        if image['collection'] not in list_of_collections:
            list_of_collections.append(image['collection'])
    return f'Available collections: {list_of_collections}'


def get_hubble_images_id(collection):
    url = f'http://hubblesite.org/api/v3/images/{collection}'
    resp = requests.get(url)
    resp.raise_for_status()
    decoded_resp = resp.json()
    list_of_id = [image['id'] for image in decoded_resp]
    print('Available images (id): ', list_of_id)
    return list_of_id


def fetch_hubble_images_from_collection(collection):
    list_of_id = get_hubble_images_id(collection)
    for id in list_of_id:
        try:
            filename = fetch_hubble_images_by_id(id)
            print(f'{filename} downloaded.')
        except Exception:
            print(f'While downloading pic by {id} an error occurred')


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    print(get_hubble_images_collections())
    collection = input("Please, choose the collection from above: ")
    fetch_hubble_images_from_collection(collection)


if __name__ == '__main__':
    main()

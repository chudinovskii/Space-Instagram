import instabot
import os
import random
import time
from dotenv import load_dotenv


def main():
    load_dotenv()
    username = os.getenv('INST_LOGIN')
    password = os.getenv('INST_PWD')

    bot = instabot.Bot()
    bot.login(username=username, password=password)

    images = os.listdir("images")
    print(images)
    for image in images:
        try:
            print(f'Uploading {image}.')
            timeout = random.randint(1, 60)
            bot.upload_photo(f'images/{image}', caption=f'This is images/{image} photo! Nice shot!')
            time.sleep(timeout)
        except Exception:
            print(f'Uploading {image} failed.')
            timeout = random.randint(1, 60)
            time.sleep(timeout)
            continue
    bot.logout()


if __name__ == '__main__':
    main()

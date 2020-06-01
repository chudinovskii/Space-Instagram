import instabot
import time
import os
from dotenv import load_dotenv
from pathlib import Path


def main():
    load_dotenv()
    username = os.getenv('INST_LOGIN')
    password = os.getenv('INST_PWD')

    bot = instabot.Bot()
    bot.login(username=username, password=password)
    timeout = 30
    images = os.listdir("images")

    for image in images:
        path_to_file = Path.cwd().joinpath('images', image)
        try:
            bot.upload_photo(path_to_file, caption=f'This is images/{image} photo! Nice shot!')
            time.sleep(timeout)
        except OSError:
            continue
    bot.logout()


if __name__ == '__main__':
    main()

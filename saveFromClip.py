import datetime
import os
from pathlib import Path
from PIL import ImageGrab


def get_img_from_clip():
    im = ImageGrab.grabclipboard()
    return im


def main():
    try:
        img = get_img_from_clip()
        if(img):
            path = os.getcwd()
            print(f'Image was saved at {path}')
            img.save(
                f'clip-{datetime.datetime.now().year}-{datetime.datetime.now().day}-{datetime.datetime.now().month}.png',
                'PNG')
        else:
            raise Exception
    except Exception:
        print("there's no clip image!")
        # open('log.txt', 'a+').write(str(err))


if __name__ == '__main__':
    main()

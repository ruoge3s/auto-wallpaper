import os
import sys
import get_wallpaper
import change_wallpaper

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WALLPAPER_DIR = BASE_DIR + '/wallpaper'


def runtime():
    if not os.path.exists(WALLPAPER_DIR):
        os.makedirs(WALLPAPER_DIR)


if __name__ == '__main__':
    if sys.argv.__len__() <= 1:
        print('Please execute with parameter "change" or "load"')
        exit()

    command = sys.argv[1]
    runtime()
    if command == 'change':
        change_wallpaper.run(WALLPAPER_DIR)
    elif command == 'load':
        get_wallpaper.run(WALLPAPER_DIR)
    else:
        print("Command error!")
        print('Please execute with parameter "change" or "load".')


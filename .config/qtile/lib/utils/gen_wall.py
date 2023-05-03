import random
import os

home = os.path.expanduser('~')
path = home + "/.config/qtile/lib/utils/index.txt"


def get_random_wallpaper() -> str:
    file_list = []
    with open(path, mode="r") as f:
        file_list = f.read().splitlines()
        idx = random.randrange(len(file_list))
        return file_list[idx]


print(get_random_wallpaper())

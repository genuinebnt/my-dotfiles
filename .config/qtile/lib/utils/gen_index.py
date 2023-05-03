import os
import sys

output_path = os.path.expanduser('~/.config/qtile/lib/utils/index.txt')


def index(folder="/mnt/Files/Important\ Files/Wallpapers/Anime\ Wallpapers/"):
    file_list = []

    for root, dir, files in os.walk(folder):
        for file in files:
            print(file)
            file_list.append(os.path.join(root, file))

    with open(output_path, mode='w') as f:
        f.write("\n".join(file_list))


if len(sys.argv) == 2:
    index(sys.argv[1])
else:
    index()

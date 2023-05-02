from libqtile.lazy import lazy

colors = []
cache = '/home/genuine/.cache/wal/colors'


def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()

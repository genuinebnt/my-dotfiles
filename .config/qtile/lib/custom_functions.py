from libqtile.command import lazy


def latest_group(qtile):
    qtile.current_screen.set_group(qtile.current_screen.previous_group)

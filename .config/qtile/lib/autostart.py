import os
import subprocess

from libqtile import hook

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/scripts/autostart.sh'])

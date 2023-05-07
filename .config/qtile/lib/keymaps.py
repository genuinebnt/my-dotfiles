import os

from libqtile.command import lazy
from libqtile.config import EzClick, EzDrag, EzKey
from libqtile.log_utils import logger

from lib.custom_functions import *

HOME = os.path.expanduser("~")

# Default applications
myTerm = "kitty"
myBrowser = "google-chrome-stable"

SCRIPTS = os.path.expanduser("~/.config/scripts")


EzKey.modifier_keys = {
    "M": "mod4",
    "A": "mod1",
    "S": "shift",
    "C": "control",
    "H": "mod3",
}

# Drag floating layouts.
mouse = [
    EzDrag(
        "M-<Button1>",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    EzDrag(
        "M-<Button3>", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    EzClick("M-<Button2>", lazy.window.bring_to_front()),
]

window_navigation = [
    EzKey("M-h", lazy.layout.left()),
    EzKey("M-j", lazy.layout.down()),
    EzKey("M-k", lazy.layout.up()),
    EzKey("M-l", lazy.layout.right()),
]

window_displacement = [
    # Shift focus -> other window(s) in stack
    # EzKey("M-<Tab>", lazy.layout.next()),
    EzKey("S-<Tab>", lazy.layout.previous()),
    EzKey("M-S-<Return>", lazy.layout.swap_main()),
    EzKey("M-S-h", lazy.layout.swap_left(), lazy.layout.shuffle_left()),
    EzKey("M-S-j", lazy.layout.swap_down(), lazy.layout.shuffle_down()),
    EzKey("M-S-k", lazy.layout.swap_up(), lazy.layout.shuffle_up()),
    EzKey("M-S-l", lazy.layout.swap_right(), lazy.layout.shuffle_right()),
    EzKey("M-<Tab>", lazy.screen.next_group(skip_empty=True)),
    EzKey("A-<Tab>", lazy.screen.toggle_group()),
]

window_dimension = [
    EzKey("M-C-h", lazy.layout.grow_left()),
    EzKey("M-C-j", lazy.layout.grow_down()),
    EzKey("M-C-k", lazy.layout.grow_up()),
    EzKey("M-C-l", lazy.layout.grow_right()),
    EzKey("M-C-n", lazy.layout.normalize()),  # Restore to original size
]

window_toggles = [
    EzKey("M-q", lazy.window.kill()),
    EzKey("M-<space>", lazy.next_layout()),
    EzKey("M-t", lazy.window.toggle_floating()),
    EzKey("M-m", lazy.window.toggle_minimize()),
    EzKey("M-C-<space>", lazy.group.setlayout("max")),
    EzKey("M-S-<space>", lazy.window.toggle_fullscreen()),
]

qtilectl = [
    EzKey("M-S-r", lazy.restart()),
    EzKey("M-S-q", lazy.shutdown()),
]

rofi_spawns = [
    EzKey("A-<Return>", lazy.spawn(f"{SCRIPTS}/rofi_run")),
    EzKey("M-x", lazy.spawn(f"{SCRIPTS}/powermenu")),
    EzKey("M-z", lazy.spawn(f"{SCRIPTS}/rofi_scripts.sh")),
]

custom_functions = [
    EzKey("A-<Insert>", lazy.spawn(
        f"{SCRIPTS}/wal.sh")),
    EzKey("A-<Home>", lazy.spawn(f"{SCRIPTS}/wallhaven.sh"))
]

application_spawns = [
    EzKey("M-<Return>", lazy.spawn(myTerm)),
    EzKey("M-A-f", lazy.spawn(myBrowser)),
]

audioctl = [
    EzKey("<XF86AudioMute>", lazy.spawn("amixer set Master toggle")),
    EzKey("<XF86AudioRaiseVolume>", lazy.spawn("amixer set Master 10%+")),
    EzKey("<XF86AudioLowerVolume>", lazy.spawn("amixer set Master 10%-")),
    EzKey("<XF86AudioMicMute>", lazy.spawn("amixer set Capture toggle")),
]

mediactl = [
    EzKey("M-<Down>", lazy.spawn("playerctl play-pause")),
    EzKey("M-<Right>", lazy.spawn("playerctl next")),
    EzKey("M-<Left>", lazy.spawn("playerctl previous")),
]

scrcapy = [
    EzKey("<Print>", lazy.spawn("scrcapy system --workspace")),
    EzKey("C-<Print>", lazy.spawn("scrcapy clipboard --workspace")),
    EzKey("A-<Print>", lazy.spawn("scrcapy system --active-window")),
    EzKey("C-A-<Print>", lazy.spawn("scrcapy clipboard --active-window")),
    EzKey("S-<Print>", lazy.spawn("scrcapy system --selection")),
    EzKey("C-S-<Print>", lazy.spawn("scrcapy clipboard --selection")),
]

brightnessctl = [
    EzKey("<XF86MonBrightnessUp>", lazy.spawn("brightnessctl set +10%")),
    EzKey("<XF86MonBrightnessDown>", lazy.spawn("brightnessctl set 10%-")),
]

quick_launch = [
    EzKey("<XF86Calculator>", lazy.spawn(
        myTerm, "start --always-new-process kalker")),
]

keys = [
    *window_navigation,
    *window_displacement,
    *window_dimension,
    *window_toggles,
    *qtilectl,
    *rofi_spawns,
    *application_spawns,
    *audioctl,
    *mediactl,
    *scrcapy,
    *brightnessctl,
    *quick_launch,
    *custom_functions,
]

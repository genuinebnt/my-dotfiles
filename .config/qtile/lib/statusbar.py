# credits: the-argus
# TODO: my own statusbar, use this to setup qtile for now.

from lib.groups import borderline
from lib.themes import palette
from lib.pywall import load_colors, colors, cache

# Qtile
from libqtile import bar, qtile, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

fontinfo = dict(
    font="VictorMono Nerd Font Semibold",
    fontsize=12,
    padding=3,
)

ROFI = "rofi -no-lazy-grab -show drun  -theme ~/.config/rofi/config_qtile.rasi"

load_colors(cache)

groupbox = [
    widget.GroupBox,
    {
        "active": colors[1],
        "block_highlight_text_color": colors[1],
        "disable_drag": True,
        "font": fontinfo["font"],
        "fontsize": 16,
        "foreground": colors[2],
        "hide_unused": True,
        "highlight_color": [colors[0], colors[3]],
        "highlight_method": "block",
        "inactive": colors[0],
        "padding": fontinfo["padding"],
        "rounded": True,
        "spacing": 5,
        "this_current_screen_border": colors[6],
        "urgent_alert_method": "block",
        "urgent_border": colors[7],
        "urgent_text": colors[7],
        "use_mouse_wheel": True,
    },
]

windowname = [
    widget.WindowName,
    {
        # "background": colors[2],
        "center_aligned": True,
        "font": fontinfo["font"],
        "fontsize": fontinfo["fontsize"],
        "format": "{name}",
        "max_chars": 35,
        "padding": 3,
        "opacity": 0.7
    },
]

systray = [
    widget.Systray,
    {
        "background": colors[2],
        "foreground": colors[4],
    },
]

spacer_small = [
    widget.Spacer,
    {
        "length": 5,
        # these values are used by style func, not qtile
        "inheirit": True,
        "is_spacer": True,
        "use_separator": False,
    },
]

logo = [
    widget.TextBox,
    {
        "font": fontinfo["font"],
        "background": colors[8],
        "fontsize": 21,
        "foreground": colors[1],
        "mouse_callbacks": {"Button1": lazy.spawn(ROFI)},
        "padding": -1.0,
        "text": " \ue928",
    },
]

layout = [
    widget.CurrentLayoutIcon,
    {
        **fontinfo,
        "background": colors[3],
        "foreground": colors[1],
        "custom_icon_paths": "./icons",
        "scale": 0.63,
    },
]


cpu = [
    widget.CPU,
    {
        **fontinfo,
        "background": colors[8],
        "foreground": colors[1],
        "format": "\ue9aa {freq_current}GHz {load_percent}%",
    },
]

net = [
    widget.Net,
    {
        **fontinfo,
        "background": colors[4],
        "format": "\ue640 {down} \u2191 {up}",
        "interface": "wlan0",
        "update_interval": 3,
    },
]

mem = [
    widget.Memory,
    {
        **fontinfo,
        "background": colors[5],
        "format": "\ue949 {MemUsed:.2f}/{MemTotal:.2f}{mm}",
        "measure_mem": "G",
        "update_interval": 1.0,
    },
]

mpris = [
    widget.Mpris2,
    {
        **fontinfo,
        # "foreground": colors[8],
        # "background": colors[6],
        "scroll": 1,
        "scroll_chars": 10,
        "width": 250,
        "paused_text": "\uf8e4 {track}",
        "playing_text": "\uf90b {track}",
    },
]

batt = [
    widget.Battery,
    {
        **fontinfo,
        "background": colors[8],
        "foreground": colors[0],
        "charge_char": "\ue63c ",
        "discharge_char": "\ue3e6 ",
        "empty_char": "\uf244 ",
        "full_char": "\uf240 ",
        "unknown_char": "\ue645 ",
        "format": "{char} {percent:2.0%} ({watt:.2f}W) ",
        "low_background": colors[7],
        "low_foreground": colors[1],
        "low_percentage": 0.30,
        "show_short_text": False,
    },
    # widget.BatteryIcon,
    # {
    #     "theme_path": "/nix/store/g8pz3vf8ih10h3hw50rv0gpki9k72j2q-Whitesur-icon-theme-2022-03-18/share/icons/WhiteSur",
    # },
]

datetime = [
    widget.Clock,
    {
        **fontinfo,
        "background": colors[6],
        "foreground": colors[8],
        "format": "\ue8df %a, %B %e, %H:%M",
    },
]

wlan = [
    widget.Wlan,
    {
        **fontinfo,
        "background": colors[1],
        "foreground": colors[8],
        "format": "{essid}",
    }
]

mpd = [
    widget.Mpd2,
    {
        **fontinfo,
        "update_interval": 1,
        "idle_message": "No songs playing",
        "max_chars": 15,
        "max_lines": 1,
        "play_states": {
            'play': '▶',
            'pause': '▮▮',
            'stop': '◾',
        },
        "format": "{play_states} {artist} - {title}",
        "scroll_chars": 10,
        "background": colors[7],
        "foreground": colors[2],
    }
]

# volume = [
#     widget.Volume,
#     {

#     }
# ]

pomodoro = [
    widget.Pomodoro,
    {
        **fontinfo,
        "background": colors[8],
        "foreground": colors[1],
        "color_active": colors[1],
        "color_inactive": colors[1],
        "color_break": colors[1],

    }
]


def widgetlist():
    return [
        spacer_small,
        logo,
        groupbox,
        layout,
        pomodoro,
        windowname,
        # mpd,
        # mpris,
        cpu,
        net,
        wlan,
        mem,
        datetime,
        systray,
        batt,
    ]


def style(widgetlist):
    styled = widgetlist[:]

    for index, wid in enumerate(widgetlist):
        end_sep = {
            "font": fontinfo["font"],
            "fontsize": 34,
            "padding": -1,
            "text": " \ue0b6",
        }

        if index < len(widgetlist) - 1:
            # end_sep["background"]=widgetlist[index+1][1].get("background", palette[1])
            # end_sep["foreground"]=wid[1].get("background", palette[1])

            end_sep["foreground"] = widgetlist[index + 1][1].get(
                "background", palette[1]
            )
            end_sep["background"] = wid[1].get("background", palette[1])

            if wid[1].get("is_spacer") and wid[1].get("inheirit"):
                bg = widgetlist[index + 1][1].get("background", palette[1])
                wid[1]["background"] = bg
                end_sep["background"] = bg

            # insert separator before current
            if wid[1].get("use_separator", True):
                styled.insert(styled.index(wid) + 1, (widget.TextBox, end_sep))

    return [w[0](**w[1]) for w in styled]


def my_bar():
    return bar.Bar(
        [*style(widgetlist())],
        34,
        foreground=palette[0],
        background=palette[1],
        opacity=1.0,
        # margin=[
        #     borderline["margin"],
        #     borderline["margin"],
        #     borderline["border_width"],
        #     borderline["margin"],
        # ],
    )


widget_defaults = dict(
    **fontinfo,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(top=my_bar()),
]

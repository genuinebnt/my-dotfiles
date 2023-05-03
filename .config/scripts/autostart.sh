#!/usr/bin/env bash

## Autostart Programs

# Kill already running process
_ps=(mpd xfce4-power-manager pulseaudio mpd nm-applet, xfce-polkit)
for _prs in "${_ps[@]}"; do
	if [[ `pidof ${_prs}` ]]; then
		killall -9 ${_prs}
	fi
done

# Fix cursor
xsetroot -cursor_name left_ptr

# Polkit agent
/usr/lib/xfce-polkit/xfce-polkit &

# Enable power management
xfce4-power-manager &

#start pulseaudio
start-pulseaudio-x11 &

# Lauch compositor
if [[ ! `pidof picom` ]]; then
  $HOME/.config/scripts/picom.sh &
fi

# Start mpd
# exec mpd &

# restore wallpaper
if [[ ! `pidof wal` ]]; then
  wal -R
fi

#nm-applet
nm-applet &

#pulseaudio i think
start-pulseaudio-x11

#mpris
dbus-launch &

# Fix Java problems
wmname "LG3D"
export _JAVA_AWT_WM_NONREPARENTING=1

[[ -f ~/.Xresources  ]] && xrdb -merge -I$HOME ~/.Xresources


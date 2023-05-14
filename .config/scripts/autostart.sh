#!/usr/bin/env bash

## Autostart Programs

# Kill already running process
_ps=(mpd pulseaudio mpd)
for _prs in "${_ps[@]}"; do
	if [[ `pidof ${_prs}` ]]; then
		killall -9 ${_prs}
	fi
done

# Fix cursor
xsetroot -cursor_name left_ptr

# Polkit agent
if [[ ! `pidof xfce-polkit` ]]; then
  /usr/lib/xfce-polkit/xfce-polkit &
fi

# Enable power management
if [[ ! `pidof xfce4-power-manager` ]]; then
  xfce4-power-manager  &
fi

#start pulseaudio
# start-pulseaudio-x11 &

#start pipewire
if [[ ! `pidof pipewire` ]]; then
  pipewire &
fi

if [[ ! `pidof piewire-pulse` ]]; then
  piewire-pulse &
fi

if [[ ! `pidof pipewire-media-session` ]]; then
  pipewire-media-session &
fi

# Lauch compositor
if [[ ! `pidof picom` ]]; then
  $HOME/.config/scripts/picom.sh &
fi

# Start mpd
# exec mpd &

# restore wallpaper
wal -R

#nm-applet
if [[ ! `pidof nm-applet` ]]; then
  nm-applet &
fi

#mpris
if [[ ! `pidof dbus-launch` ]]; then
  dbus-launch &
fi

# Fix Java problems
wmname "LG3D"
export _JAVA_AWT_WM_NONREPARENTING=1

[[ -f ~/.Xresources  ]] && xrdb -merge -I$HOME ~/.Xresources


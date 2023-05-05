#!/usr/bin/env bash

prompt="rofi -dmenu -i -theme ~/.config/rofi/config_qtile.rasi"

# variables
uptime="`uptime -p | sed -e 's/up //g'`"
host=`cat /proc/sys/kernel/hostname`

blur="Blur"
transparency="Transparency"
remove_wall="Delete current wallpaper"
save_wall="Save current wallpaper"

option="$save_wall\n$remove_wall\n$blur\n$transparency"

show_options()
{
  echo -e "$option" | $prompt -p "$host" -mesg "Uptime: $uptime"
}

select="$(show_options)"

case $select in 
    $blur)
        $HOME/.config/scripts/blur.sh
        ;;
    $transparency)
        $HOME/.config/scripts/transparency.sh
        ;;
    $remove_wall)
        cat $HOME/.cache/wal/wal | tail -n 1 | tee >(xargs -I {} notify-send "{}") | xargs -I {} rm -f "{}"
        ;;
    $save_wall)
        cat $HOME/.cache/wal/wal | tail -n 1 | tee >(xargs -I {} notify-send "{}") | xargs -I {} cp "{}" $HOME/.config/fav_walls/
esac

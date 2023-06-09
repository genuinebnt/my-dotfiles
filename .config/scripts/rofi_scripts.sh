#!/usr/bin/env bash

prompt="rofi -dmenu -i -theme ~/.config/rofi/config_qtile.rasi"

# variables
uptime="`uptime -p | sed -e 's/up //g'`"
host=`cat /proc/sys/kernel/hostname`

blur="Toggle Blur"
transparency="Toggle transparency"
remove_wall="Delete current wallpaper"
save_wall="Save current wallpaper to favorites"
preview_set="Set wallpaper"
save_wall_2="Save current wallpaper to other favorites"

option="$save_wall\n$save_wall_2\n$remove_wall\n$preview_set\n$blur\n$transparency"

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
        cat $HOME/.cache/wal/wal | tail -n 1 | tee >(xargs -I {} notify-send "{}") | xargs -I {} cp -n "{}" $HOME/.config/fav_walls/
        ;;
    $preview_set)
        $HOME/.config/scripts/rofi_wallpaper.sh
        ;;
    $save_wall_2)
        cat $HOME/.cache/wal/wal | tail -n 1 | tee >(xargs -I {} notify-send "{}") | xargs -I {} cp -n "{}" $HOME/.config/other_walls/
        ;;
esac

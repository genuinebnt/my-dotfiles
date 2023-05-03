#!/usr/bin/env bash

prompt="rofi -dmenu -i -theme ~/.config/rofi/config_qtile.rasi"

# variables
uptime="`uptime -p | sed -e 's/up //g'`"
host=`cat /proc/sys/kernel/hostname`

blur="Blur"
transparency="Transparency"

option="$blur\n$transparency"

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
esac
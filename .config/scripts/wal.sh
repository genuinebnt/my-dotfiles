#!/usr/bin/env bash 

WALL="/mnt/Files/Important Files/Wallpapers/2020-6-10"

wal -i "$WALL" && qtile cmd-obj -o cmd -f reload_config && echo $wall >> ~/.config/wall.txt

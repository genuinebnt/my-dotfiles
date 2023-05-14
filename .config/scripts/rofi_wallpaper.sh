#!/bin/bash

WALLPAPERS_DIR="$HOME/.config/fav_walls"
COLLECTION_DIR="/mnt/Files/Important Files/Wallpapers/2020-6-10"
WALLHAVEN_DIR="$HOME/.config/wallhaven_pics"

# Define three modes for three directories
mode1="Favorite Wallpapers:$WALLPAPERS_DIR"
mode2="Wallpaper Collection:$COLLECTION_DIR"
mode3="Wallhaven Pics:$WALLHAVEN_DIR"

# Combine the modes into a single list for Rofi
modes_list="$mode1\n$mode2\n$mode3"

# Prompt the user to select a mode
selected_mode=$(echo -e "$modes_list" | rofi -dmenu -i -p "Select wallpaper directory:" -theme config_qtile)

# Rofi command
ROFI_CMD="rofi -dmenu -i -show-icons -theme wallsetter"

# Get the options for the selected mode
if [[ $selected_mode == $mode1 ]]; then
    DIR_PATH="$WALLPAPERS_DIR" && 
    choice=$(ls --escape "$DIR_PATH" | \
        while read A; do echo -en "$A\x00icon\x1f$DIR_PATH/$A\n"; done | \
        $ROFI_CMD -p "Favorite Wallpaper")
elif [[ $selected_mode == $mode2 ]]; then
    DIR_PATH="$COLLECTION_DIR" && 
    choice=$(ls --escape "$DIR_PATH" | \
        while read A; do echo -en "$A\x00icon\x1f$DIR_PATH/$A\n"; done | \
        $ROFI_CMD -p "Wallpaper Collection")
elif [[ $selected_mode == $mode3 ]]; then
    DIR_PATH="$WALLHAVEN_DIR" && 
    choice=$(ls --escape "$DIR_PATH" | \
        while read A; do echo -en "$A\x00icon\x1f$DIR_PATH/$A\n"; done | \
        $ROFI_CMD -p "Wallhaven pics")
else
    exit 1
fi

# Set the selected wallpaper as the desktop background
if [[ $choice ]]; then
    notify-send "Setting wallpaper: $choice"
    wal -i "$DIR_PATH/$choice" && qtile cmd-obj -o cmd -f reload_config
fi

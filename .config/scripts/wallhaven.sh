#!/usr/bin/env bash

notify-send "Downloading wallpaper" && python3 $HOME/.config/scripts/wallhaven/app.py && notify-send "Wallpaper set"


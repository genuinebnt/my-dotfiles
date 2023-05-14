#!/usr/bin/env bash


enable="\"80:class_g = 'kitty'\", # kitty transparency"
disable="\"100:class_g = 'kitty'\", # kitty transparency"
file_path="$HOME/.config/picom.conf"

if grep -q "$enable" "$file_path"; then
  sed -i "s/$enable/$disable/" "$file_path" 
else
  sed -i "s/$disable/$enable/" "$file_path"
fi
  

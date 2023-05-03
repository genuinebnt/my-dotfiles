#!/usr/bin/env bash


enable="strength = 10; # blur strength"
disable="strength = 0; # blur strength"
file_path="$HOME/.config/picom.conf"

if grep -q "$enable" "$file_path"; then
  sed -i "s/$enable/$disable/" "$file_path" 
else
  sed -i "s/$disable/$enable/" "$file_path"
fi
  

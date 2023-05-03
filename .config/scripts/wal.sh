#!/usr/bin/env bash

wal -i "`python3 ~/.config/qtile/lib/utils/gen_wall.py`" && qtile cmd-obj -o cmd -f reload_config 

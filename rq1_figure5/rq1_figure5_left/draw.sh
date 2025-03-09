#!/bin/bash

# These commands generate the file `rflcommits` `rfldevcommits` `commits`
# We had already produced these file, If you want to reproduce, uncomment the lines 6 ~ 16
# 
# apt-get install -y git
# cd <your-rust-for-linux-tree>
# git fetch
# git checkout rust
# git log --oneline > data/rflcommits
# git checkout rust-dev
# git log --online > data/rfldevcommits
# cd <your-linux-mainline-tree>
# git fetch
# git checkout master
# git log --oneline > data/commits
# 
#
cd code
# The script `github.py` takes a long time to run. `github.py` generate the `data.txt` in `data` directory.
# If you want to reproduce the data, uncomment it and run draw.sh
#
# python3 github.py > ../data/github.log

# `draw.py` use the `data.txt` stored in `data` directory.
# We had already produced `data.txt`, If you want to reproduce, uncomment the line 22

# Draw a vertical picture
python3 draw.py

# Draw a horizontal picture
python3 draw_horizontal.py
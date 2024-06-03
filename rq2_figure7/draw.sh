#!/bin/bash
cd code
python3 full_plot.py
python3 only_left_subplot.py

# We use `objdump` to see different sections in object files
# If you want to collect these data, you should first compile rust-for-linux in rust-dev branch. defconfig is enough.
# Just use `objdump` over the object files produced by files in subsystems, which tools to use depending on which compiler you use to build linux. 
# 
# example:
# objdump -h samples/rust/rust_semaphore.o
# objdump -h samples/rust/rust_semaphore_c.o
#
# The output summary the different section in the object file
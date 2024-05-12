#!/bin/bash
cd code
python3 full_plot.py
python3 only_left_subplot.py

# We use `objdump` to see different sections in object files
# If you want to collect these data, you should first compile rust-for-linux in rust-dev branch. defconfig is enough.
# Then after the build, you should refer to the page at path [`All development-process docs` -> `Maintainer information` -> `List of maintainers`] in `docs.kernel.org`
# For example, you can search the `io_uring` at this page, you will see a block titled with `io_uring` and files in `Files` field are files subsystem cared.
# Just use `nm` or `llvm-nm` over the object files produced by these files, which tools to use depending on which compiler you use to build linux. 
# 
# example:
# objdump -h samples/rust/rust_semaphore.o
# objdump -h samples/rust/rust_semaphore_c.o
#
# The output summary the different section in the object file
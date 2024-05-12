# Figure3 AE

## Instructions to reproduce

run `./bash.sh` to generate `figure3.pdf` in directory `./imgs/` and data files in directory `./data`
The `function_total` and `structure_toal` correspond to the total functions and data structures in the Linux kernel.
The `rust_functions` and `rust_structers` correspond to the wrapped rust functions and rust structures.
Then we calculate the percentage of rust functions and rust structures in the total functions and data structures and manually put the number into the `plt.py` to generate `figure3.pdf`.

**During the reproduce process, we found the percentage of wrapped `mm` structures and avg are wrongly plotted. 
The `mm` wrapped percentage should be changed to 1.4% from 4.5%.
Wrapped percentage of functions/structs should be 3.39% and 4.49%.
Other wrapped function percentage values also have slight changes due to the kernel version and config influence.
But this will not change the our insight, that is there exists a long tail of wrapped functions and structures in the Linux kernel.
We will update `figure3` in the camera-ready version.**
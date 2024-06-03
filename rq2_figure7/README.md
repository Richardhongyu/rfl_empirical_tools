# Introduction

## How to produce data

See the comment line in `draw.sh`.

## Tutorial

Run `./draw.sh` to generate the figures `full_plot.pdf` and `only_left_subplot.pdf` in directory `imgs`. `full_plot.pdf` has the `debug section` and `only_left_subplot.pdf` doesn't have the `debug section`

If you want to regenerate data, you can follow the examples in the comments of the `draw.h`.
Among the drivers, 1) gpio/sem/ can be found in the rust-for-linux repo; 2)nblk/binder drivers are sent the lore.kernel.org; 3) e1000 and nvme/ are in https://github.com/fujita/rust-e1000/ and https://github.com/metaspace/linux/tree/rnvme.

We have all the data and log in the mechine.
You can check by using ssh to connect our mechina environemnt. The details is listed in the `Artifact Location` section of the ATC AE system.

The format of `data.txt` stored in `data` is `rust/c`, first 3 columns are `text`, `data`, `bss` respectively. The next two columns are both `debug section`.
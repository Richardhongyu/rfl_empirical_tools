# Introduction

## How to produce data

See the comment line in `draw.sh`.

## Tutorial

Run `./draw.sh` to generate the figures `full_plot.pdf` and `only_left_subplot.pdf` in directory `imgs`. `full_plot.pdf` has the `debug section` and `only_left_subplot.pdf` doesn't have the `debug section`

The format of `data.txt` stored in `data` is `rust/c`, first 3 columns are `text`, `data`, `bss` respectively. The next two columns are both `debug section`.
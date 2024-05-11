# Introduction

Run `./draw.sh` to get the figure9 and figure10 in paper. These two figures are stored in directory `imgs`. 

`code` store some scripts that will be used when executing `draw.sh`. 

`data` store the essential data that will be used in scripts at `code`.

# How Data generated

The data of `null block` driver are produced by following the test in the patch https://lore.kernel.org/rust-for-linux/20230503090708.2524310-1-nmi@metaspace.dk/

The data of `nvme` driver are produced in our physical machine. You can ssh this machine by `ssh -p 9301 rros@149.129.120.139` and you will see corresponding data stored in `/data/nvme*`

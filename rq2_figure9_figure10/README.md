# Introduction

Run `./draw.sh` to get the figure9 and figure10 in paper. These two figures are stored in directory `imgs`. 

`code` store some scripts that will be used when executing `draw.sh`. 

`data` store the essential data that will be used in scripts at `code`.

# How Data generated

## Null Block driver

The data of `null block` driver are produced by following the test in the patch https://lore.kernel.org/rust-for-linux/20230503090708.2524310-1-nmi@metaspace.dk/

We use `fio` tools to test the null block driver. 

For example

```bash
# load the C null block module and Rust null block device
sudo modprobe null_blk \
    queue_mode=2 irqmode=0 hw_queue_depth=256 \
    memory_backed=1 bs=4096 completion_nsec=0 \
    no_sched=1 gb=4;
sudo modprobe rnull_mod
# This test 4 jobs with block size 4k randread for C null block driver.
# If you want to test Rust null block driver, just change the device
fio --filename=/dev/nullb0 --iodepth=64 --ioengine=psync --direct=1 --rw=randread --bs=4k --timebase=1 --numjobs=4 --runtime=120 --group_reporting --output-format=json --name=test-rand-read --output=test_c_randread.log --norandommap --random_generator=lfsr
```

We just run a series of `fio` with different `bs` and `numjobs` in a bash script to produce the raw data in `out_np_1_10.npy` and `out_np.npy`, other arguments are mostly the same.

Note that `out_np_1_10.npy` and `out_np.npy` are produced by extracting the data in massive output json files. There are many way to process the data. We just used `numpy` and `json` to extract them and stored them as `*.npy`. If you want to see the detailed data, just print `data` in `figure9.py`.

There is a difference between `out_np_1_10.npy` and `out_np.npy`. `out_np_1_10.npy` was produced by null block device that `modprobe` with `no_sched=0`, and which in `out_np.npy` is `no_sched=1`

Before you test, if you want to fill the data just run

```bash
# This fill device /dev/nullb0. 
# If you want to fill rust device, change it to rust null block device.
fio --name=prep --rw=write --filename=/dev/nullb0 --bs=4k --direct=1
```

## NVME

The data of `nvme` driver are produced in our physical machine.
You can check by using ssh to connect our mechina environemnt. The details is listed in the `Artifact Location` section.
You will see corresponding data stored in `/data/nvme*`
# Introduction

Run `./draw.sh <path-to-linux>` to generate the corresponing data of *Table 5: The code quality measurement. % means coverage* in paper. We collect the data in `rust-dev` branch, source code can be access at this link [rust-dev](https://github.com/Rust-for-Linux/linux/tree/rust-dev/).

For example, if your linux store in `/home/someone/linux`, then just run `./draw.sh /home/someone/linux` will be ok.

**We provide a rust-for-linux repo in container and its path is `/workspace/linux`, so you can just run `./draw.sh /workspace/linx`**

`code` directory store some scripts that will execute by `draw.sh`, `data` directory store the output log.

## Docs%

Column `Docs%` data is shown at the end of the log file `doc_cov.log` like these contexts:

```plain-text
io_uring: 0.313 [doc/(exported+included)]=[5/16]
ebpf: 0.141 [doc/(exported+included)]=[12/(49+36)]
```

`io_uring: 0.313 [doc/(exported+included)]=[5/16]` means document coverage in io_uring is 33.3% and the number of documented function is `5`.
The number of functions with `EXPORT_SYMBOL` or `EXPORT_SYMBOL_GPL`, and the number of public functions included in header files is `16`. 
Line about ebpf is similar.

> Note: The document coverage of RFL is 100%, because the compile will not pass if there is a function without kernel-doc comment.

## CI errors/10K LoC

After the excution of `draw.sh`, there will be three json file generated in `data` directory.

`ebpf_loc.json` store the information that `cloc` tool reported the loc of files in ebpf subsystem. `io_uring_loc.json` and `rfl-loc.json` are similar.
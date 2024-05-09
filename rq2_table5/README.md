# Introduction

Run `./draw.sh <path-to-linux>` to generate the corresponing data of *Table 5: The code quality measurement. % means coverage* in paper. We collect the data in `rust-dev` branch, source code can be access at this link [rust-dev](https://github.com/Rust-for-Linux/linux/tree/rust-dev/).

For example, if your linux store in `/home/someone/linux`, then just run `./draw.sh /home/someone/linux` will be ok.

`code` directory store some scripts that will execute by `draw.sh`, `data` directory store the output log.

## Docs%

Column `Docs%` data is shown at the end of the log file `doc_cov.log` like these contexts:

```plain-text
io_uring: 0.200 [doc/(exported+included)]=[2/(5+5)]
ebpf: 0.141 [doc/(exported+included)]=[12/(49+36)]
```

`io_uring: 0.200 [doc/(exported+included)]=[2/(5+5)]` means document coverage in io_uring is 20.0% and the number of documented function is `2`, the number of functions with `EXPORT_SYMBOL` or `EXPORT_SYMBOL_GPL` is `5`, the number of functions included in header files is `5`. Line about ebpf is similar.

> Note: We don't need to compute the document coverage of RFL, because the compile will not pass if there is a function without kernel-doc comment.

## CI errors/10K LoC

After the excution of `draw.sh`, there will be three json file generated in `data` directory.

`ebpf_loc.json` store the information that `cloc` tool reported the loc of files in ebpf subsystem. `io_uring_loc.json` and `rfl-loc.json` are similar.
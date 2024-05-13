#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 [linux-root-path]"
    exit 1
fi

linux_tree_path=$1
script_path=$(pwd)
echo "linux-tree-path is ${linux_tree_path}"
echo "script_path is ${script_path}"

# DOC COVERAGE

## Rust
# Rust has to be 100% covered by the documentation, otherwise it will fail to compile
echo "DOC COVERAGE"
echo "Rust 100%"

## ebpf
cp code/doc_cov.py ${linux_tree_path}
cd ${linux_tree_path} && python3 doc_cov.py > ${script_path}/data/doc_cov.log && rm doc_cov.py
echo "ebpf 12/90=13.3%"


## io_uring
# Manually search the related file of io_uring got from the MAINTAINER files
# ```
# F:	fs/io-wq.c
# F:	fs/io-wq.h
# F:	fs/io_uring.c
# F:	include/linux/io_uring.h
# F:	include/uapi/linux/io_uring.h
# F:	tools/io_uring/
# ```

# io_uring.h
# 2/3

# io-wq.h
# 5/8

# grep EXPORT_ io_uring/*
# io_uring/io_uring.c:EXPORT_SYMBOL(io_uring_get_socket);
# io_uring/io_uring.c:EXPORT_SYMBOL(__io_commit_cqring_flush_new)
# io_uring/uring_cmd.c:EXPORT_SYMBOL_GPL(io_uring_cmd_complete_in_task);
# io_uring/uring_cmd.c:EXPORT_SYMBOL_GPL(io_uring_cmd_done);
# io_uring/uring_cmd.c:EXPORT_SYMBOL_GPL(io_uring_cmd_import_fixed);
# 4/5

echo "io_uring 5/16=31.3%"

# CI/10K LOC

pushd /workspace/linux-doc-coverage
echo "CI/10K LOC"

## rust
cloc rust >/workspace/rfl_empirical_tools/rq2_table5/data/rust_ci 2>&1 #68591
cloc rust/bindings >>/workspace/rfl_empirical_tools/rq2_table5/data/rust_ci 2>&1 #46973
# 8 bugs reported by INTEL
# >>> 8/(68591-46973)
echo rust 0.0003700619853825516*10000

## io_uring
cloc io_uring >/workspace/rfl_empirical_tools/rq2_table5/data/io_uring_ci 2>&1  # 12396
# 12 bugs found from lore.kernel.org of the io_uring in the same period(2021/07/24)
# these bugs are repoted by the community CI bots
# >>> 12/12396
echo io_uring 0.000968054211035818*10000

## ebpf
# if you want to check
cloc Documentation/bpf/ networking/filter Documentation/userspace-api/ebpf/ arch/*/net/* include/linux/bpf* include/linux/btf* include/linux/filter.h include/trace/events/xdp.h include/uapi/linux/bpf* include/uapi/linux/btf* include/uapi/linux/filter.h kernel/bpf/ kernel/trace/bpf_trace.c lib/test_bpf.c net/bpf/ net/core/filter.c net/sched/act_bpf.c net/sched/cls_bpf.c samples/bpf >/workspace/rfl_empirical_tools/rq2_table5/data/ebpf_ci 2>&1 # 125694
# 132 bugs found from lore.kernel.org of the io_uring in the same period(2020/09/01)
# these bugs are repoted by the community CI bots
# >>> 132/125694
echo ebpf 0.0010501694591627286*10000
popd
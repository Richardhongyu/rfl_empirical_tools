#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 [linux-root-path]"
    exit 1
fi

linux_tree_path=$1
script_path=$(pwd)
echo "linux-tree-path is ${linux_tree_path}"
echo "script_path is ${script_path}"
cp code/doc_cov.py ${linux_tree_path}
cd ${linux_tree_path} && python3 doc_cov.py > ${script_path}/data/doc_cov.log && rm doc_cov.py

echo "Use cloc tools to compute the code of line in subsystems"
cd ${linux_tree_path}
cloc --json --report-file="${script_path}/data/rfl_loc.json" --include-lang=Rust --fullpath --not-match-d=bindings Documentation/rust/ rust/ samples/rust/ scripts/*rust* tools/testing/selftests/rust/
cloc --json --report-file="${script_path}/data/io_uring_loc.json" --include-lang='C,C/C++ Header' include/linux/io_uring/ include/linux/io_uring.h include/linux/io_uring_types.h include/trace/events/io_uring.h include/uapi/linux/io_uring.h io_uring/
cloc --json --report-file="${script_path}/data/ebpf_loc.json" --include-lang='C,C/C++ Header' Documentation/bpf/ networking/filter Documentation/userspace-api/ebpf/ arch/*/net/* include/linux/bpf* include/linux/btf* include/linux/filter.h include/trace/events/xdp.h include/uapi/linux/bpf* include/uapi/linux/btf* include/uapi/linux/filter.h kernel/bpf/ kernel/trace/bpf_trace.c lib/test_bpf.c net/bpf/ net/core/filter.c net/sched/act_bpf.c net/sched/cls_bpf.c samples/bpf/ scripts/bpf_doc.py scripts/Makefile.btf scripts/pahole-version.sh tools/bpf/ tools/lib/bpf/ tools/testing/selftests/bpf/ 
cd ${script_path}/code && python3 get_loc.py && cd -

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
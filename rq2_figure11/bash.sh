cp code/plot.py /workspace/rq2_experience/
pushd /workspace/rq2_experience

# working...
# pushd linux-rust
# # rfl_commits is selected from `commit_only_in_rfl.json` in rq1_figure5_left repo
# cp data/rfl_commits /workspace/rq2_experience/linux-rust
# cp code/rust.py /workspace/rq2_experience/linux-rust
# cp code/find_rust_time.py /workspace/rq2_experience/linux-rust
# cp code/count.py /workspace/rq2_experience/linux-rust
# python3 rust.py >rfl_names
# python3 find_rust_time.py >rfl_times
# python3 count.py rfl_times >rust_count
# cp rust_count /workspace/rfl_empirical_tools/rq2_figure11/data
# popd

# pushd linux-ebpf
# git rev-list --oneline 830b3c68c1fb^..HEAD >all_gitlog
# cat all_gitlog |grep bpf:>ebpf_data
# python3 ebpf.py > ebpf_authors
# python3 find_time_ebpf.py
# cp ebpf_count /workspace/rfl_empirical_tools/rq2_figure11/data
# popd

# pushd linux-iouring
# git rev-list --oneline 830b3c68c1fb^..HEAD >all_gitlog
# cat all_gitlog |grep io_uring>ebpf_data
# python3 ebpf.py > ebpf_authors
# python3 find_time_ebpf.py
# cp iouring_count /workspace/rfl_empirical_tools/rq2_figure11/data
# popd

python3 plot.py
cp figure11.pdf /workspace/rfl_empirical_tools/rq2_figure11/imgs
popd


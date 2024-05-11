cp code/*.py /workspace/rust-for-linux2/
pushd /workspace/rust-for-linux2
# This is a scrawling script. Commented for saving time. But it's fine to open it. This scrawl process will take a long time, please be patient.
# python3 split.py
python3 even_class.py > mid_value1
python3 generate_data.py > mid_value2
python3 percentage.py > mid_value3
python3 plot.py
cp ./figure4.pdf /workspace/rfl_empirical_tools/rq1_figure4/imgs
cp mid_value* /workspace/rfl_empirical_tools/rq1_figure4/data
popd

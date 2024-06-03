cp code/*.py /workspace/rust-for-linux2/
pushd /workspace/rust-for-linux2
# python3 split.py
# python3 even_class.py > mid_value1
python3 generate_data.py > mid_value2
python3 percetange.py > mid_value3
python3 plot.py
cp ./figure4.pdf /workspace/rfl_empirical_tools/rq1_Figure4/imgs
popd
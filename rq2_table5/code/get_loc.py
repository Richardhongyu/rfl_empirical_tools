import json
import os

file = ['../data/rfl_loc.json', '../data/io_uring_loc.json', '../data/ebpf_loc.json']
# ci error is count in hand
ci_errors = {
    'rfl_loc' : 8,
    'io_uring_loc' : 12,
    'ebpf_loc' : 132
}
file_dic = {}

for f in file:
    with open(f, 'r') as fd:
        file_name = os.path.basename(f).split('.')[0]
        file_dic[file_name] = json.loads(fd.read())

for subsystem, sd in file_dic.items():
    loc = sd['SUM']['code']
    err = ci_errors[subsystem]
    print("CI errors per 10K Loc")
    print(f'{subsystem} : {loc/(10_000*err):.1}')

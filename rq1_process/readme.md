# process

## environment

### merged

https://github.com/Rust-for-Linux/linux/commits/rust-6.4?after=ea76e08f4d901a450619831a255e9e0a4c0ed162+34&branch=rust-6.4&qualified_name=refs%2Ftags%2Frust-6.4

### github

dragon root@be7cdac3875e:/data/bupt-rtos/linux rust-dev branch 9fa041aae0b73be53524413d93f9cd69c4096f96

commit c8d1ae2cbe240789ad402c71fce78a7ea1ebdea5 (origin/rust, origin/HEAD)
Merge: bc22545f38d7 b1b4b5fd90f9
Author: Miguel Ojeda <ojeda@users.noreply.github.com>
Date:   Wed Jun 21 19:43:03 2023 +0200

    Merge pull request #1017 from ojeda/rust-rust-1.70
    
    Rust 1.70.0

### in review

https://github.com/Rust-for-Linux/linux

## merged

### numbers

contains 6.5 but not 6.6

```bash
see the commits in the specific tag by searching "ojeda/fixes"
```

right: 28+28+(35+9)+19+27 = 146
fixes: 1+7+1+3+1 = 13
sum: 159

### col

```bash
# Merge tag 'rust-6.*' of https://github.com/Rust-for-Linux/linux
of https://github.com/Rust-for-Linux/linux


a1257b5e3b7f8a21faf462d0118067fe31e71ffb: 36 files changed, 1658 insertions, 795 deletions
310897659cf056016e2c772a028f9b8abc934928: 35 files changed, 4980 insertions, 24 deletions
69adb0bcb833963050d82e645b6a1a0747662490: 15 files changed, 808 insertions, 503 deletions
96f42635684739cb563aa48d92d0d16b8dc9bda8: 25 files changed, 1667 insertions, 42 deletions
8aebac82933ff1a7c8eede18cab11e1115e2062b: 89 files changed, 12552 insertions, 51 deletions
```

sum change:
    insertions: 1658+4980+808+1667+12552 = 17665
    deletions: 795+24+503+42+51 = 1415
    sum: 17665+1415 = 19080

## github

### numbers

```bash
# commits: commits in the linux branch
# rflcommits: commits in the rust branch
# rfldevcommits: commits in the rust-dev branch


# a.py this script is not woring(trying to scrawl emails)
# find_diff.py a script for testing hash(useless)
# compare.py a test script ploting the indices and date
# commit_log.py a test script for collecting the col in git

# new_com.py rflcommits numbers sum but the time is not correct, they are not sliced
# commit_linus.py refdevcommits/refcommits col sum commit_lines_sum_dev.png
# new_3.py refdevcommits/refcommits numbers sum commit_dates_new.png
# commit_linus_number.py refdevcommits/refcommits col number 
# new_3_number.py refdevcommits/refcommits numbers number

python3 
```

1540

### col

```bash
python3 commit_linus.py
```

112288

## in review

```bash

```

### numbers

```bash

python github.py
# use the github script to collect the github ids
python find_commits.py
ipython
# sum([int(i) for i  in a])
```

524

### col

```bash
python github.py
# use the github script to collect the github ids
python find_col.py
python cal_col.py
```

186356
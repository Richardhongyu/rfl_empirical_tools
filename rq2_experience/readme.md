# experience

## environment

### RFL

root@be7cdac3875e:/data/bupt-rtos/linux# git log
commit aa856cf072fc055fe0d557b5639467490eb6eaf3 (HEAD -> rust-dev)

### netdev

website

extra code is in the root@be7cdac3875e:/data/bupt-rtos/ml-stat#

### ebpf

root@0035f146a62a:/data/bupt-rtos/linux# git log
commit 59e12e432dd843b0e8ecc42f77358c16b7ba8e4a (HEAD -> ebpf_6_4)

### io_uring

root@0035f146a62a:/data/bupt-rtos/linux# git log
commit 59e12e432dd843b0e8ecc42f77358c16b7ba8e4a (HEAD -> ebpf_6_4)

## data

### RFL

see the below

### netdev

see from the website

### ebpf

see the below

### io_uring

1. command

```
# find commits
python3 find_io_ebpf.py  | wc -l
python3 find_the_author_first_commit_io_uring.py >real_time
python3 find_last_io_uring.py >last_time_io_uring
python3 last_one_io_uring.py 
# delete the first line
# change the internal from 3 , 6, 12 to 24, count the number as the time slice from netdev
python3 count.py
```

2. log 
```
 1695  git log --oneline 
 1696  git rev-list --oneline 830b3c68c1fb..HEAD
 1697  git log --oneline 
 1698  git rev-list --oneline 830b3c68c1fb..HEAD |less
 1699  git rev-list --oneline 830b3c68c1fb^..HEAD |less
 1700  git rev-list --oneline 830b3c68c1fb^..HEAD >all_gitlog
 1701  ls fin*
 1702  python3 find_io_ebpf.py 
 1703  python3 find_io_ebpf.py  | wc -l
 1704  mv find_io_ebpf.py find_io_uring.py 
 1705  cp find_io_uring.py find_ebpf.py 
 1706  python3 find_io_ebpf.py  | wc -l
 1707  python3 find_io_uring.py  | wc -l
 1708  python3 find_io_uring.py  | les
 1709  python3 find_io_uring.py  | less
 1710  python3 find_io_uring.py  | wc -l
 1711  python3 find_io_ebpf.py  | wc -l
 1712  python3 find_ebpf.py  | wc -l
 1713  git status
 1714  git add find_*
 1715  git add nohup.out 
 1716  git add all_gitlog 
 1717  git status
 1718  python3 find_ebpf.py  > ebpf_log.py
 1719  python3 find_io_uring.py  >io_uring_log
 1720  mv ebpf_log.py ebpf_log
 1721  ls
 1722  ls -al *_log
 1723  git add *_log
 1724  git status
 1725  python3 find_the_author_first_commit.py 
 1726  python3 find_the_author_first_commit.py >real_time_ebpf
 1727  mv find_last.py find_last_ebpf.py 
 1728  python3 find_last_ebpf.py 
 1729  python3 find_last_ebpf.py >last_time
 1730  cp last_one.py last_one_ebpf.py 
 1731  python3 last_one_ebpf.py 
 1732  python3 find_last_ebpf.py >last_time_ebpf
 1733  python3 last_one_ebpf.py 
 1734  git log
 1735  python3 last_one_ebpf.py 
 1736  python3 print_ebpf_io_uring.py 
 1737  python3 count.py 
 1738  history > commit_time_log
 1739  cp find_the_author_first_commit.py find_the_author_first_commit_ebpf.py 
 1740  cp find_the_author_first_commit_ebpf.py find_the_author_first_commit_io_uring.py
 1741  python3 find_the_author_first_commit_io_uring.py 
 1742  python3 find_the_author_first_commit_io_uring.py >real_time
 1743  mv real_time real_time_io_uring
 1744  python3 find_last_io_uring.py >last_time_io_uring
 1745  mv last_one.py last_one_io_uring.py
 1746  python last_one_io_uring.py 
 1747  python3 last_one_io_uring.py 
 1748  python last_one_io_uring.py 
 1749  python3 last_one_io_uring.py 
 1750  python3 find_last_io_uring.py >last_time_io_uring
 1751  python3 last_one_io_uring.py 
 1752  vim last_one_io_uring.py 
 1753  python3 find_the_author_first_commit_io_uring.py >real_time_io_uring 
 1754  python3 find_last_io_uring.py >last_time_io_uring
 1755  python3 last_one_io_uring.py 
 1756  python print_ebpf_io_uring.py 
 1757  python3 print_ebpf_io_uring.py 
 1758  python3 count.py 
```
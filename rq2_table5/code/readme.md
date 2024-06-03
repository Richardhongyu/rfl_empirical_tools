# development 

## environment

### code coverage

### document coverage

root@be7cdac3875e:/data/bupt-rtos/linux# git commit -m "add the message"
[rust-dev 80180df38821] add the message
 2 files changed, 2000 insertions(+)
 create mode 100644 doc_coverage.sh
 create mode 100644 document.sh
root@be7cdac3875e:/data/bupt-rtos/linux# git log
commit 80180df388211c350c26a5fbd4985a2e2d59e8d5 (HEAD -> rust-dev)

### ci errors

rfl:
root@be7cdac3875e:/data/bupt-rtos/linux# git commit -m "add the message"
[rust-dev 80180df38821] add the message
 2 files changed, 2000 insertions(+)
 create mode 100644 doc_coverage.sh
 create mode 100644 document.sh
root@be7cdac3875e:/data/bupt-rtos/linux# git log
commit 80180df388211c350c26a5fbd4985a2e2d59e8d5 (HEAD -> rust-dev)

ebpf:
root@795ba347cefe:/data/bupt-rtos/linux# git log
commit 68e34488a3ebf67000718bc7f800f36c6b93cf9d (HEAD -> ci_errors_ebpf)

io_uring:
root@795ba347cefe:/data/bupt-rtos/linux# git log
commit 223236274784958004bd5a5a2f1f7f830a2b359e (HEAD -> ci_errors_io-uring)


## docs coverage

### rust

100%

### ebpf

see the find_*.sh

### io_uring


io_uring maintainers

```
F:	fs/io-wq.c
F:	fs/io-wq.h
F:	fs/io_uring.c
F:	include/linux/io_uring.h
F:	include/uapi/linux/io_uring.h
F:	tools/io_uring/
```

io_uring.h
2/3

io-wq.h
5/8

grep EXPORT_ io_uring/*

io_uring/io_uring.c:EXPORT_SYMBOL(io_uring_get_socket);
io_uring/io_uring.c:EXPORT_SYMBOL(__io_commit_cqring_flush_new)
io_uring/uring_cmd.c:EXPORT_SYMBOL_GPL(io_uring_cmd_complete_in_task);
io_uring/uring_cmd.c:EXPORT_SYMBOL_GPL(io_uring_cmd_done);
io_uring/uring_cmd.c:EXPORT_SYMBOL_GPL(io_uring_cmd_import_fixed);

4/5

1-11/16=31.3%

## ci errors

count by hand

### RFL

1. ci errors

    8

2. lines from rust branch 

```
root@be7cdac3875e:/data/bupt-rtos/linux# git log
commit 409b3498e6fa53994ca3940ef801a25638c52cea (HEAD -> rust)

18364

root@be7cdac3875e:/data/bupt-rtos/linux# cloc rust/
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
     128 text files.
     128 unique files.                                          
      13 files ignored.
github.com/AlDanial/cloc v 1.74  T=3.41 s (34.0 files/s, 25536.6 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Rust                            97           3177          15841          63204

root@be7cdac3875e:/data/bupt-rtos/linux# cloc rust/bindings
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
       6 text files.
       6 unique files.                              
       0 files ignored.

github.com/AlDanial/cloc v 1.74  T=0.18 s (33.7 files/s, 265469.6 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Rust                             3              9             17          44840

root@be7cdac3875e:/data/bupt-rtos/linux# python3
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 63204-44840
18364

```

### ebpf

1. ci errors
    
    132

2. lines read from rq3

this has problem, need to sync with the date 2020/09/01

```
Processing: BPF (Safe dynamic programs and tools) 
 Total C/C++ Header lines in BPF (Safe dynamic programs and tools): 176138
 Total number of fixes in BPF (Safe dynamic programs and tools): 119
```

### io_uring

1. ci errors

    12

2. lines read from rq3

this has problem, need to sync with the date 2021/07/24

```
Processing: IO_URING 
 Total C/C++ Header lines in IO_URING: 10102
 Total number of fixes in IO_URING: 83
```

### cal

>>> 132/176138
0.0007494123925558369
>>> 12/10102
0.001187883587408434
>>> 8/18364
0.00038118057068176867

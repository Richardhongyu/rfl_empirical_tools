# subsystem

## environment

root@be7cdac3875e:/data/bupt-rtos/linux#
commit be908b2fead5d9e73b92d20a65fafbe66df3d325 (HEAD -> rust-dev)

## overhead

### loc

```
cloc foo
```

## benifits

### bugs

```
git log --oneline -- /path | grep "keywords"
```

## plot

```
python3 rq3_4.py > result.text
python3 color5.py # change the result.txt file path
```

## record

### overhead

#### loc

cat result_12_21_2.txt  | grep C/C++ | awk -F ":" 'BEGIN {sum=0}; {print $2; sum+=$2}; END {print sum}' |less

```
drivers:
C                             18907        2097325        1687367       10462555
C/C++ Header                   8766         336553         613093        3678151

kernel:
C                                    32359        3040343        2670378       15248719
C/C++ Header                         22287         626434        1134251        5237326

file
C                             1417         153667         232034         869230
C/C++ Header                   545          16849          26732          95768

net
C                             1938         177988         124735         838428
C/C++ Header                   249           7103           8407          34958

12170213/15248719
3808877/5237326

root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc drivers/
   39302 text files.
   38918 unique files.
    7444 files ignored.

github.com/AlDanial/cloc v 1.74  T=239.02 s (134.7 files/s, 79173.7 lines/s)
--------------------------------------------------------------------------------
Language                      files          blank        comment           code
--------------------------------------------------------------------------------
C                             18907        2097325        1687367       10462555
C/C++ Header                   8766         336553         613093        3678151
make                           1425           3151           5006          18552
Perl                              8            641            366           4996
Assembly                         16           1010            972           3565
DOS Batch                      3048              8              0           3056
Rust                             10            461            403           2632
yacc                              2            240            241           1679
lex                               2             57            157            557
Python                            6            140            318            409
YAML                              4             83             23            302
Bourne Again Shell                1              1             12             18
--------------------------------------------------------------------------------
SUM:                          32195        2439670        2307958       14176472
--------------------------------------------------------------------------------
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc^C
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# ls
 0001-Introduce-Opaque-type-and-use-it-in-sync-module.patch        5_7_rrb         Module.symvers                                       'by0922(1).tar'         gdb_arm                     kill_qemu.py              modules.order       test.py          vmlinux.o
 0001-lab4-answers.patch                                           5_8_rrb         Quectel_Linux_USB_Serial_Option_Driver_20230814.tgz   certs                  gdb_remote.sh               lab3.patch                net                 test.qcow2       vmlinux.symvers
 0001-raspi_patches.patch                                          COPYING         README                                                compile.sh             gdbarm                      lab3_v2.patch             qemu.test           test1.py         work_kernel
 0001-rros-one-big-patch.patch                                     CREDITS         README.md                                             compile.txt            git                         lhy_0504_syscall          result              test_vm
 0001-rust-add-support-for-static-synchronisation-primitiv.patch   Documentation   System.map                                            copy_to_raspberry.sh   gr                          lhy_syscall_0504_2        rust                tools
 0001-task1.patch                                                  Kbuild          a.patch                                               crypto                 include                     lib                       rust-project.json   try.py
 0001-task2.patch                                                  Kconfig         arch                                                  drivers                init                        mm                        samples             usr
 0001-test.patch                                                   LICENSES        arm-himix100-linux.tgz                                extract_error.py       ipc                         modules-only.symvers      scripts             virt
 1                                                                 MAINTAINERS     block                                                 finderr.py             kernel                      modules.builtin           security            vmlinux
 4gdriver                                                          Makefile        bos.tar                                               fs                     kernel_3516ev200_ec20.tgz   modules.builtin.modinfo   sound               vmlinux-gdb.py
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./
   98212 text files.
   96810 unique files.
   33047 files ignored.

github.com/AlDanial/cloc v 1.74  T=558.31 s (124.0 files/s, 53407.7 lines/s)
---------------------------------------------------------------------------------------
Language                             files          blank        comment           code
---------------------------------------------------------------------------------------
C                                    32359        3040343        2670378       15248719
C/C++ Header                         22287         626434        1134251        5237326
Assembly                              1291          46330          98832         716418
JSON                                   341              3              0         258130
Rust                                   180           5877          18545         238556
YAML                                  1698          29543           7786         132272
Bourne Shell                           729          20744          14004          80797
make                                  2641          10238          11247          46309
Perl                                    66           7139           4995          36270
Python                                 133           5586           5046          28805
DOS Batch                             7379           1123              0          14586
yacc                                     9            693            355           4760
PO File                                  5            791            918           3077
lex                                      9            345            303           2104
C++                                      8            330             91           1876
Bourne Again Shell                      51            297            247           1304
awk                                     11            155            126           1111
Glade                                    1             58              0            603
NAnt script                              2            147              0            583
Markdown                                 3             69              0            195
Cucumber                                 1             30             50            183
Windows Module Definition                2             15              0            109
m4                                       1             15              1             95
CSS                                      1             28             29             80
XSLT                                     5             13             26             61
vim script                               1              3             12             27
Ruby                                     1              4              0             25
D                                        2              0              0             13
INI                                      1              1              0              6
sed                                      1              2              5              5
TOML                                     1              1              9              2
---------------------------------------------------------------------------------------
SUM:                                 69220        3796357        3967256       22054407
---------------------------------------------------------------------------------------
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./f
finderr.py  fs/
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./f
finderr.py  fs/
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./fs
    4127 text files.
    4119 unique files.
    1737 files ignored.

github.com/AlDanial/cloc v 1.74  T=25.04 s (96.7 files/s, 55759.6 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
C                             1417         153667         232034         869230
C/C++ Header                   545          16849          26732          95768
make                            88            226            302            921
DOS Batch                      372              0              0            372
-------------------------------------------------------------------------------
SUM:                          2422         170742         259068         966291
-------------------------------------------------------------------------------
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./k
kernel/                    kernel_3516ev200_ec20.tgz  kill_qemu.py
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./k
kernel/                    kernel_3516ev200_ec20.tgz  kill_qemu.py
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./kernel
kernel/                    kernel_3516ev200_ec20.tgz
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./kernel/
Display all 295 possibilities? (y or n)
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./kernel/f
fail_function.c  fork.c           fork.c.rej       fork.o           freezer.c        freezer.o        futex.c          futex.o
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./k
kernel/                    kernel_3516ev200_ec20.tgz  kill_qemu.py
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./kernel/d
debug/       delayacct.c  delayacct.o  dma/         dma.c        dovetail.c   dovetail.o
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./kernel/d
debug/       delayacct.c  delayacct.o  dma/         dma.c        dovetail.c   dovetail.o
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase# cloc ./net/
    6073 text files.
    6061 unique files.
    2685 files ignored.

github.com/AlDanial/cloc v 1.74  T=31.05 s (109.7 files/s, 38468.9 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
C                             1938         177988         124735         838428
C/C++ Header                   249           7103           8407          34958
make                            88            285            348           1215
DOS Batch                     1130              0              0           1130
Assembly                         1              0              1              6
-------------------------------------------------------------------------------
SUM:                          3406         185376         133491         875737
-------------------------------------------------------------------------------
root@795ba347cefe:/data/bupt-rtos/linux-dovetail-v5.13-dovetail-rebase#
```


### numbers 

above

1. linux-ext4@vger.kernel.org
2. 

root@be7cdac3875e:/data/bupt-rtos/linux# python3 find_drivers.py 
linux-hams@vger.kernel.org
9

linux-block@vger.kernel.org
9

cgroups@vger.kernel.org
4

linux-ext4@vger.kernel.org
3

linux-hardening@vger.kernel.org
5

linux-nfs@vger.kernel.org
2

rcu@vger.kernel.org
3

root@be7cdac3875e:/data/bupt-rtos/linux# python3
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 9+9+4+3+5+2+3
35
>>> 35-7
28
>>> 28/2500
0.0112
>>> 
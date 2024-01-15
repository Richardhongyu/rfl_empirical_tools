# overhead

## environment

### size

1. binder
  root@0035f146a62a:/data/bupt-rtos/linux# 
  rust-binder branch

  root@be7cdac3875e:/data/bupt-rtos/linux# git log
  commit b6f85e6d037d985271d9a26277e8699f0c953a68 (HEAD -> rust-binder-rfc)
  Author: Li Hongyu <lihongyu1999@bupt.edu.cn>
  Date:   Mon Jan 15 16:15:48 2024 +0800

      tmp

  root@0035f146a62a:/data/bupt-rtos/linux# git log
  commit a110917dae00b2868e48ffcaa05da8f197100aae (HEAD -> ebpf_6_4)
  Author: Li Hongyu <lihongyu1999@bupt.edu.cn>
  Date:   Mon Jan 15 16:18:46 2024 +0800

### time

### performance

## sise

### nvme

### null blk

### e1000

### binder

size for segment

```
size -A -t drivers/android/binder*.o

nm --print-size --size-sort --radix=d drivers_binder_debug/*.o

pahole

size drivers/android/binder*

 1539  llvm-strip drivers_binder_binder_nodebug/*.o
 1540  llvm-strip drivers_binder_binder_nodebug/
 1541  llvm-strip drivers_binder_nodebug/*.o

  1579  apt-get install dwarves
 1580  pahole vmlinux -C task_struct
 1581  pahole drivers_binder_debug/binder_internal.h -C binder_proc
 1582  pahole drivers_binder_debug/binder.o -C binder_proc
 1583  pahole drivers_binder_debug/rust_binder.o -C binder_proc
 1584  pahole drivers_binder_debug/rust_binder.o -C Process
 1585  nm --print-size --size-sort --radix=d drivers_binder_debug/*.o
 1586  size -t drivers/android/*.o
 1587  size -A -d  drivers_binder_debug/*.o
 1588  size -d  -t drivers/android/*.o
 1589  size -A  -t drivers/android/*.oq
 1590  objdump --dwarf=info drivers/android/binder.o |less

```

### gpio_pl061

### semaphore

## time

### binder

 1463  ls drivers/gpio/*.rs
 1464  vim drivers/gpio/Makefile
 1465  time make LLVM=1 CONFIG_GPIO_PL061_RUST=m drivers/gpio/gpio_pl061_rust.o
 1466  ls drivers/gpio/gpio-pl061.*
 1467  ls drivers/gpio/gpio-pl061*
 1468  rm drivers/gpio/gpio-pl061.o
 1469  vim drivers/gpio/Makefile
 1470  time make LLVM=1 CONFIG_GPIO_PL061=m drivers/gpio/gpio-pl061.o
 1471  ls drivers/android/rust_binder.*
 1472  rm drivers/android/rust_binder.o
 1473  rm drivers/android/*.o
 1474  vim drivers/android/Makefile
 1475  rm drivers/android/rust_binder.o
 1476  time make LLVM=1 CONFIG_ANDROID_BINDER_IPC_RUST=1 drivers/android/rust_binder.o
 1477  time make LLVM=1 CONFIG_ANDROID_BINDER_IPC=1 drivers/android/binder.o drivers/android/binder_alloc.o

## performance

### binder

#### c

Total time: 26.844060652
Total time: 26.850842993
Total time: 27.455477773
Total time: 28.054080080
Total time: 28.911260447

a= [26.844060652,26.850842993,27.455477773,28.054080080,28.911260447,]
max(a)
min(a)
sum(a)/len(a)

>>> max(a)
28.911260447
>>> min(a)
26.844060652
>>> avg(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'avg' is not defined
>>> sum(a)/len(a)
27.623144388999997


#### rust 

Total time: 32.005682759
Total time: 31.429996962
Total time: 32.710689671
Total time: 30.919446299
Total time: 32.051573856

a = [32.005682759,31.429996962,32.710689671,30.919446299,32.051573856,]

32.710689671
>>> min(a)
30.919446299
>>> sum(a)/len(a)
31.823477909399998
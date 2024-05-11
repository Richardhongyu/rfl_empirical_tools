# wrapped

## environment

dragon root@be7cdac3875e:/data/bupt-rtos/linux rust branch 409b3498e6fa53994ca3940ef801a25638c52cea

commit c8d1ae2cbe240789ad402c71fce78a7ea1ebdea5 (origin/rust, origin/HEAD)
Merge: bc22545f38d7 b1b4b5fd90f9
Author: Miguel Ojeda <ojeda@users.noreply.github.com>
Date:   Wed Jun 21 19:43:03 2023 +0200

    Merge pull request #1017 from ojeda/rust-rust-1.70
    
    Rust 1.70.0

## function

1. find all the functions
```bash
nm -l vmlinux | grep " T " > functions.txt && cat functions.txt | grep -v "_RN" | wc -l

28805
```

2. find the rust functions
```bash
find rust/kernel/ -name *.rs | xargs cat | grep 'bindings::[A-Za-z_]*(' -o | sort | uniq |wc -l
```

188

3. classify the functions in different subsystems

```bash
python3 find.py

cat function_info.txt | grep linux/kernel/sched/ |wc -l
cat function_info.txt | grep kernel/locking |wc -l
329+59=388

cat function_info.txt | grep linux/mm |wc -l
1050

cat function_info.txt | grep linux/fs |wc -l
2760

cat function_info.txt | grep linux/net/ |wc -l
4526

cat function_info.txt | grep linux/drivers |wc -l
8766

cat function_info.txt | grep linux/kernel/time |wc -l
333

cat function_info.txt | grep linux/kernel/irq |wc -l
234

cat function_info.txt | grep kernel/cred |wc -l
cat function_info.txt | grep linux/security |wc -l
16+519=535

cat function_info.txt | grep arch |wc -l
2334

sum:388+1050+2760+4526+8766+333+535+2334=20732

```

4. classify the functions in the rust systems

```bash
find rust/kernel/ -name *.rs | xargs cat | grep 'bindings::[A-Za-z_]*(' -o | sort | uniq  > rust_wrapped_functions.txt

python3 rust.py > result.bat

python3 count.py
```

result
    - sched && sync
      - sched
        - 'rust/kernel/task.rs': 6,
        - 'rust/kernel/sync.rs': 1,
        - 'rust/kernel/workqueue.rs': 5,
        - 12
      - lock
        - 'rust/kernel/sync/spinlock.rs': 10,
        - 'rust/kernel/sync/mutex.rs': 3,
        - 'rust/kernel/sync/condvar.rs': 6,
        - 'rust/kernel/sync/rwsem.rs': 5,
        - 'rust/kernel/sync/smutex.rs': 3,
        - 'rust/kernel/sync/rcu.rs': 2,
        - 'rust/kernel/sync/seqlock.rs': 5,
        - 'rust/kernel/revocable.rs': 1
        - 'rust/kernel/lib.rs': 3
        - 38
      - 50
    - memory
      - 'rust/kernel/sync/arc.rs': 3,
      - 'rust/kernel/allocator.rs': 2
      - 'rust/kernel/pages.rs': 4,
      - 'rust/kernel/mm.rs': 1,
      - 'rust/kernel/io_mem.rs': 3,
      - 13
    - file
      - 'rust/kernel/file.rs': 6,
      - 'rust/kernel/fs.rs': 21,
      - 27
    - net
      - 'rust/kernel/net/filter.rs': 3,
      - 'rust/kernel/net.rs': 15,
      - 'rust/kernel/kasync/net.rs': 3,
      - 21
    - driver
        - device
          - 'rust/kernel/device.rs': 5,
          - 'rust/kernel/miscdev.rs': 2,
          - 'rust/kernel/chrdev.rs': 5,
          - 12
        - driver
          - 'rust/kernel/module_param.rs': 1,
        - platform
          - 'rust/kernel/platform.rs': 5,
        - bus
          - 'rust/kernel/amba.rs': 4,
        - 'rust/kernel/power.rs': 1,
        - 'rust/kernel/gpio.rs': 3,
        - 'rust/kernel/hwrng.rs': 2,
        - 'rust/kernel/iov_iter.rs': 3,
        - 'rust/kernel/sysctl.rs': 2,
        - 33
    - clock && irq
      - 'rust/kernel/clk.rs': 4,
      - 'rust/kernel/irq.rs': 10,
      - 'rust/kernel/delay.rs': 1,
      - 15
    - security
      - 'rust/kernel/cred.rs': 2
      - 'rust/kernel/security.rs': 4,
      - 6
    - others
      - structers
        - 'rust/kernel/rbtree.rs': 8,
        - 'rust/kernel/str.rs': 2,
      - 'rust/kernel/error.rs': 4,
      - 'rust/kernel/print.rs': 1,
      - 'rust/kernel/kunit.rs': 1,
      - 'rust/kernel/user_ptr.rs': 3,
      - 'rust/kernel/random.rs': 4,
      - 23


5. subsystems result
    - sched && sync
      - 50/388
    - mm
      - 10/1050
    - file
      - 27/2760
    - net
      - 21/4526
    - driver
      - 36/8766
    - clock && irq
      - 15/333
    - security
      - 6/535
    - others(sounds, trace, arch, lib, ipc)
      - 23/(28805-20732)=23/8073

## struct

1. find all the structuers

```bash
find ./include -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
find kernel/ -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
find net -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
find mm -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
find fs -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
find security/ -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
```

16490
158
701
32
2031
194
16490+158+701+32+2031+194=19106

2. find all the rust structers

```bash
find rust/kernel/ -name *.rs | xargs cat | grep 'bindings::[A-Za-z_]*' -o | sort | uniq |wc -l
```

472-188-1=283

```bash
find rust/kernel/ -name *.rs | xargs cat | grep 'bindings::[A-Za-z_]*' -o | sort | uniq > struct_info.txt

python3 diff.py

## delete the upper variable (macros)

wc -l  rust_wrapped_structers.txt

python3 rust2.py
```

141->71

3. classify the functions in different subsystems

```bash

find kernel/sched -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
28
find kernel/locking -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
7
find ./include/linux/sched* -name *.h | xargs cat [typedef ]*| grep '^struct [A-Za-z_0-9]* {' | sort | uniq |  
wc -l
35
find ./include/linux/*lock* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
54

find mm -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
32
find ./include/memory/ -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
2

find fs -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
2031
find ./include/linux/fs* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
101
find ./include/linux/file* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
7

find net -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
701
find ./include/net -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
2043

find ./include/linux/*driver* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
20
find ./include/linux/*dev* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
197
find ./include/linux/*platform* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
568
find ./include/linux/*bus* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
235
find ./include/linux/*pci* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
47
find ./include/linux/*usb* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
196
find ./include/linux/*amba* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
17
find ./include/linux/*gpio* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
20


find kernel/time -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
3
find ./include/clocksource/ -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
7
find ./include/linux/*time* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
39
find ./include/linux/*clock* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
10

find kernel/irq -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
1
find ./include/linux/*irq* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort  uniq |  wc -l
27

find security/ -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
194
find ./include/linux/*security* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
0
find ./include/linux/*cred* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
2

sum
    - sched && sync
      - sched
        - 28+35=63
      - lock
        - 54+7=61
      - 124
    - memory
        - 32+2=34
    - file
        - 2031+101+7=2139
    - net
        - 701+2043=2744
    - driver
        - driver
          - 20
        - device
          - 197
        - platform
          - 568
        - bus
          - 235
        - pci
          - 47
        - usb
          - 196
        - amba
          - 17
        - gpio
          - 20
        - 1280
    - clock && irq
        - clock
          - 59
        - irq
          - 28
        - 87
    - security
        - 196
    - 124+34+2139+2744+1280+87+196=6664

```

4. classify the functions in the rust systems

result
    - sched && sync
      - sched
        - include/linux/completion.h:26:struct completion {
        - include/linux/sched.h:737:struct task_struct {
        - include/linux/wait.h:30:struct wait_queue_entry {
        - include/linux/wait.h:37:struct wait_queue_head {
        - include/linux/workqueue.h:97:struct work_struct {
        - kernel/workqueue.c:260:struct workqueue_struct {
        - 6
      - lock
        - arch/alpha/include/asm/spinlock_types.h:struct arch_spinlock {
        - include/linux/lockdep_types.h:74:struct lock_class_key {
        - include/linux/mutex.h:63:struct mutex {
        - include/linux/spinlock_types_raw.h:14:typedef struct raw_spinlock {
        - include/linux/rwsem.h:47:struct rw_semaphore {
        - include/linux/seqlock.h:64:typedef struct seqcount {
        - include/linux/spinlock_types.h:17:typedef struct spinlock {
        - 7
      - 13
    - memory
        - include/linux/dcache.h:82:struct dentry {
        - include/linux/mm_types.h:74:struct page {
        - include/linux/refcount.h:111:typedef struct refcount_struct {
        - include/linux/mm_types.h:480:struct vm_area_struct {
        - 4
    - file
        - include/linux/fs_parser.h:15:struct constant_table {
        - include/linux/fs.h:942:struct file {
        - include/linux/fs.h:1754:struct file_operations {
        - include/linux/fs.h:2189:struct file_system_type {
        - include/linux/fs.h:2291:struct filename {
        - include/linux/fs_context.h:90:struct fs_context {
        - include/linux/fs_context.h:115:struct fs_context_operations {
        - include/linux/fs_context.h:63:struct fs_parameter {
        - include/linux/fs_parser.h:39:struct fs_parameter_spec {
        - include/linux/fs_parser.h:53:struct fs_parse_result {
        - include/linux/fs.h:595:struct inode {
        - include/linux/fs.h:343:struct kiocb {
        - include/linux/poll.h:41:typedef struct poll_table_struct {
        - include/linux/fs.h:1136:struct super_block {
        - include/linux/fs.h:1886:struct super_operations {
        - 15
    - net
        - include/uapi/linux/in.h:92:struct in_addr {
        - include/linux/socket.h:55:struct msghdr {
        - include/net/net_namespace.h:60:struct net {
        - include/linux/netfilter.h:85:struct nf_hook_ops {
        - include/linux/netfilter.h:67:struct nf_hook_state {
        - include/linux/skbuff.h:851:struct sk_buff {
        - include/uapi/linux/in.h:255:struct sockaddr_in {
        - include/linux/net.h:116:struct socket {
        - 8
    - driver
        - device
          - include/linux/cdev.h:14:struct cdev {
          - include/linux/device.h:555:struct device {
          - include/linux/netdevice.h:2033:struct net_device {
          - include/linux/mod_devicetable.h:268:struct of_device_id {
        - driver
        - platform
          - include/linux/platform_device.h:23:struct platform_device {
          - include/linux/platform_device.h:208:struct platform_driver {
        - bus
          - include/linux/amba/bus.h:64:struct amba_device {
          - include/linux/amba/bus.h:81:struct amba_driver {
          - include/linux/mod_devicetable.h:649:struct amba_id {
        - include/linux/sysctl.h:135:struct ctl_table {
        - include/linux/pm.h:286:struct dev_pm_ops {
        - include/linux/gpio/driver.h:407:struct gpio_chip {
        - include/linux/hw_random.h:39:struct hwrng {
        - include/linux/uio.h:43:struct iov_iter {
        - include/linux/moduleparam.h:69:struct kernel_param {
        - include/linux/moduleparam.h:47:struct kernel_param_ops {
        - include/linux/uio.h:18:struct kvec {
        - include/linux/module.h:371:struct module {
        - 18
    - clock && irq
        - clock
          - include/linux/irqdesc.h:55:struct irq_desc {
          - include/linux/irqdomain.h:150:struct irq_domain {
          - include/linux/sh_clk.h:38:struct clk {
          - include/linux/irq.h:179:struct irq_data {
          - include/linux/irq.h:506:struct irq_chip {
        - 5
    - security
        - include/linux/cred.h:110:struct cred {
        - 1
    - others
        - include/kunit/assert.h:49:struct kunit_assert {};
        - include/kunit/assert.h:36:struct kunit_loc {
        - include/linux/rbtree_types.h:5:struct rb_node {
        - include/linux/rbtree_types.h:12:struct rb_root {
        - 4
    - total
        - 71

5. subsystem results
    - sched && sync
      - 13/124
    - mm
      - 4/34
    - file
      - 15/2139
    - net
      - 8/2744
    - driver
      - 18/1280
    - clock && irq
      - 5/87
    - security
      - 1/196
    - others(sounds, trace, arch, lib, ipc)
      - 4/(19106-6664)=4/12442

## plot the result


```bash
python3 new_plt_struct.py
python3 new_plt_function.py
```


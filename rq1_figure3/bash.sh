cp code/*.py /workspace/wrapped_func_structures/linux
pushd /workspace/wrapped_func_structures/linux
# functions

# This step consumes huge time, use the old data in the default mode. If you would like test this, you can uncomment the following lines and select the right config manual.
# make LLVM=1 defconfig
# export ARCH=x86_64
# export CROSS_COMPILE=
# make LLVM=1 -j
# make LLVM=1 defconfig
# ./scripts/config -e DEBUG_INFO_DWARF_TOOLCHAIN_DEFAULT
# ./scripts/config -e RUST
# make LLVM=1 olddefconfig
# nm -l vmlinux | grep " T " > functions.txt && cat functions.txt | grep -v "_RN" | wc -l > functions_count
find rust/kernel/ -name *.rs | xargs cat | grep 'bindings::[A-Za-z_]*(' -o | sort | uniq |wc -l > rust_functions_count
python3 find.py
cat function_info.txt | grep linux/kernel/sched/ |wc -l > function_total
cat function_info.txt | grep kernel/locking |wc -l >> function_total
cat function_info.txt | grep linux/mm |wc -l >> function_total
cat function_info.txt | grep linux/fs |wc -l >> function_total
cat function_info.txt | grep linux/net/ |wc -l >> function_total
cat function_info.txt | grep linux/drivers |wc -l >> function_total
cat function_info.txt | grep linux/kernel/time |wc -l >> function_total
cat function_info.txt | grep linux/kernel/irq |wc -l >> function_total
cat function_info.txt | grep kernel/cred |wc -l >> function_total
cat function_info.txt | grep linux/security |wc -l >> function_total
cat function_info.txt | grep arch |wc -l >> function_total

# Data1: Manually check the rust structures in the function_total
# linux/kernel/sched/ 
# kernel/locking 
# 329+59=388

# linux/mm 
# 1050

# linux/fs 
# 2760

# linux/net/ 
# 4526

# linux/drivers 
# 8766

# linux/kernel/time 
# 333

# linux/kernel/irq 
# 234

# kernel/cred 
# linux/security 
# 16+519=535

# arch 
# 2334

find rust/kernel/ -name *.rs | xargs cat | grep 'bindings::[A-Za-z_]*(' -o | sort | uniq  > rust_wrapped_functions.txt
python3 rust.py > result.bat
python3 count.py > rust_functions_total

# Data2: Manually check the rust structures in the rust_structers
# result
#     - sched && sync
#       - sched
#         - 'rust/kernel/task.rs': 6,
#         - 'rust/kernel/sync.rs': 1,
#         - 'rust/kernel/workqueue.rs': 5,
#         - 12
#       - lock
#         - 'rust/kernel/sync/spinlock.rs': 10,
#         - 'rust/kernel/sync/mutex.rs': 3,
#         - 'rust/kernel/sync/condvar.rs': 6,
#         - 'rust/kernel/sync/rwsem.rs': 5,
#         - 'rust/kernel/sync/smutex.rs': 3,
#         - 'rust/kernel/sync/rcu.rs': 2,
#         - 'rust/kernel/sync/seqlock.rs': 5,
#         - 'rust/kernel/revocable.rs': 1
#         - 'rust/kernel/lib.rs': 3
#         - 38
#       - 50
#     - memory
#       - 'rust/kernel/sync/arc.rs': 3,
#       - 'rust/kernel/allocator.rs': 2
#       - 'rust/kernel/pages.rs': 4,
#       - 'rust/kernel/mm.rs': 1,
#       - 'rust/kernel/io_mem.rs': 3,
#       - 13
#     - file
#       - 'rust/kernel/file.rs': 6,
#       - 'rust/kernel/fs.rs': 21,
#       - 27
#     - net
#       - 'rust/kernel/net/filter.rs': 3,
#       - 'rust/kernel/net.rs': 15,
#       - 'rust/kernel/kasync/net.rs': 3,
#       - 21
#     - driver
#         - device
#           - 'rust/kernel/device.rs': 5,
#           - 'rust/kernel/miscdev.rs': 2,
#           - 'rust/kernel/chrdev.rs': 5,
#           - 12
#         - driver
#           - 'rust/kernel/module_param.rs': 1,
#         - platform
#           - 'rust/kernel/platform.rs': 5,
#         - bus
#           - 'rust/kernel/amba.rs': 4,
#         - 'rust/kernel/power.rs': 1,
#         - 'rust/kernel/gpio.rs': 3,
#         - 'rust/kernel/hwrng.rs': 2,
#         - 'rust/kernel/iov_iter.rs': 3,
#         - 'rust/kernel/sysctl.rs': 2,
#         - 33
#     - clock && irq
#       - 'rust/kernel/clk.rs': 4,
#       - 'rust/kernel/irq.rs': 10,
#       - 'rust/kernel/delay.rs': 1,
#       - 15
#     - security
#       - 'rust/kernel/cred.rs': 2
#       - 'rust/kernel/security.rs': 4,
#       - 6
#     - others
#       - structers
#         - 'rust/kernel/rbtree.rs': 8,
#         - 'rust/kernel/str.rs': 2,
#       - 'rust/kernel/error.rs': 4,
#       - 'rust/kernel/print.rs': 1,
#       - 'rust/kernel/kunit.rs': 1,
#       - 'rust/kernel/user_ptr.rs': 3,
#       - 'rust/kernel/random.rs': 4,
#       - 23

# structures
find rust/kernel/ -name *.rs | xargs cat | grep 'bindings::[A-Za-z_]*' -o | sort | uniq |wc -l
find rust/kernel/ -name *.rs | xargs cat | grep 'bindings::[A-Za-z_]*' -o | sort | uniq > struct_info.txt
python3 diff.py
## delete the upper variable (because they are macros, not)
tail -n 325 rust_wrapped_structers.txt > rust_wrapped_structers2.txt
wc -l  rust_wrapped_structers2.txt
python3 rust2.py

# Data1: Manually check the rust structures in the rust_structers
    # - sched && sync
    #   - sched
    #     - include/linux/completion.h:26:struct completion {
    #     - include/linux/sched.h:737:struct task_struct {
    #     - include/linux/wait.h:30:struct wait_queue_entry {
    #     - include/linux/wait.h:37:struct wait_queue_head {
    #     - include/linux/workqueue.h:97:struct work_struct {
    #     - kernel/workqueue.c:260:struct workqueue_struct {
    #     - 6
    #   - lock
    #     - arch/alpha/include/asm/spinlock_types.h:struct arch_spinlock {
    #     - include/linux/lockdep_types.h:74:struct lock_class_key {
    #     - include/linux/mutex.h:63:struct mutex {
    #     - include/linux/spinlock_types_raw.h:14:typedef struct raw_spinlock {
    #     - include/linux/rwsem.h:47:struct rw_semaphore {
    #     - include/linux/seqlock.h:64:typedef struct seqcount {
    #     - include/linux/spinlock_types.h:17:typedef struct spinlock {
    #     - 7
    #   - 13
    # - memory
    #     - include/linux/dcache.h:82:struct dentry {
    #     - include/linux/mm_types.h:74:struct page {
    #     - include/linux/refcount.h:111:typedef struct refcount_struct {
    #     - include/linux/mm_types.h:480:struct vm_area_struct {
    #     - 4
    # - file
    #     - include/linux/fs_parser.h:15:struct constant_table {
    #     - include/linux/fs.h:942:struct file {
    #     - include/linux/fs.h:1754:struct file_operations {
    #     - include/linux/fs.h:2189:struct file_system_type {
    #     - include/linux/fs.h:2291:struct filename {
    #     - include/linux/fs_context.h:90:struct fs_context {
    #     - include/linux/fs_context.h:115:struct fs_context_operations {
    #     - include/linux/fs_context.h:63:struct fs_parameter {
    #     - include/linux/fs_parser.h:39:struct fs_parameter_spec {
    #     - include/linux/fs_parser.h:53:struct fs_parse_result {
    #     - include/linux/fs.h:595:struct inode {
    #     - include/linux/fs.h:343:struct kiocb {
    #     - include/linux/poll.h:41:typedef struct poll_table_struct {
    #     - include/linux/fs.h:1136:struct super_block {
    #     - include/linux/fs.h:1886:struct super_operations {
    #     - 15
    # - net
    #     - include/uapi/linux/in.h:92:struct in_addr {
    #     - include/linux/socket.h:55:struct msghdr {
    #     - include/net/net_namespace.h:60:struct net {
    #     - include/linux/netfilter.h:85:struct nf_hook_ops {
    #     - include/linux/netfilter.h:67:struct nf_hook_state {
    #     - include/linux/skbuff.h:851:struct sk_buff {
    #     - include/uapi/linux/in.h:255:struct sockaddr_in {
    #     - include/linux/net.h:116:struct socket {
    #     - 8
    # - driver
    #     - device
    #       - include/linux/cdev.h:14:struct cdev {
    #       - include/linux/device.h:555:struct device {
    #       - include/linux/netdevice.h:2033:struct net_device {
    #       - include/linux/mod_devicetable.h:268:struct of_device_id {
    #     - driver
    #     - platform
    #       - include/linux/platform_device.h:23:struct platform_device {
    #       - include/linux/platform_device.h:208:struct platform_driver {
    #     - bus
    #       - include/linux/amba/bus.h:64:struct amba_device {
    #       - include/linux/amba/bus.h:81:struct amba_driver {
    #       - include/linux/mod_devicetable.h:649:struct amba_id {
    #     - include/linux/sysctl.h:135:struct ctl_table {
    #     - include/linux/pm.h:286:struct dev_pm_ops {
    #     - include/linux/gpio/driver.h:407:struct gpio_chip {
    #     - include/linux/hw_random.h:39:struct hwrng {
    #     - include/linux/uio.h:43:struct iov_iter {
    #     - include/linux/moduleparam.h:69:struct kernel_param {
    #     - include/linux/moduleparam.h:47:struct kernel_param_ops {
    #     - include/linux/uio.h:18:struct kvec {
    #     - include/linux/module.h:371:struct module {
    #     - 18
    # - clock && irq
    #     - clock
    #       - include/linux/irqdesc.h:55:struct irq_desc {
    #       - include/linux/irqdomain.h:150:struct irq_domain {
    #       - include/linux/sh_clk.h:38:struct clk {
    #       - include/linux/irq.h:179:struct irq_data {
    #       - include/linux/irq.h:506:struct irq_chip {
    #     - 5
    # - security
    #     - include/linux/cred.h:110:struct cred {
    #     - 1
    # - others
    #     - include/kunit/assert.h:49:struct kunit_assert {};
    #     - include/kunit/assert.h:36:struct kunit_loc {
    #     - include/linux/rbtree_types.h:5:struct rb_node {
    #     - include/linux/rbtree_types.h:12:struct rb_root {
    #     - 4
    # - total
    #     - 71

find kernel/sched -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >rust_structures_values
find kernel/locking -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/sched* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq | wc -l  >>rust_structures_values
find ./include/linux/*lock* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find mm -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/memory/ -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find fs -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/fs* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/file* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find net -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/net -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/*driver* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l>>rust_structures_values
find ./include/linux/*dev* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/*platform* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/*bus* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/*pci* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/*usb* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/*amba* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/*gpio* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find kernel/time -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/clocksource/ -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/*time* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/*clock* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find kernel/irq -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/*irq* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find security/ -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/*security* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values
find ./include/linux/*cred* -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l >>rust_structures_values

# Data2: Manually count the number of structures in the structure_total
# the log is as follows
# sum
#     - sched && sync
#       - sched
#         - 28+35=63
#       - lock
#         - 57+7=64
#       - 127
#     - memory
#         - 32+2=34
#     - file
#         - 2200+101+7=2308
#     - net
#         - 702+2043=2745
#     - driver
#         - driver
#           - 20
#         - device
#           - 197
#         - platform
#           - 568
#         - bus
#           - 235
#         - pci
#           - 47
#         - usb
#           - 196
#         - amba
#           - 17
#         - gpio
#           - 20
#         - 1280
#     - clock && irq
#         - clock
#           - 59
#         - irq
#           - 28
#         - 87
#     - security
#         - 196
#     - 127+34+2308+2745+1280+87+196=6664

# plot
# manually put the above data into the plt.py
python3 plt.py

# copy data
cp rust_functions_total /workspace/rfl_empirical_tools/rq1_figure3/data/rust_functions
cp function_total /workspace/rfl_empirical_tools/rq1_figure3/data
cp rust_wrapped_structers_info.txt /workspace/rfl_empirical_tools/rq1_figure3/data/rust_structers
cp rust_structures_values /workspace/rfl_empirical_tools/rq1_figure3/data/structure_total
cp ./figure3.pdf /workspace/rfl_empirical_tools/rq1_figure3/imgs
popd
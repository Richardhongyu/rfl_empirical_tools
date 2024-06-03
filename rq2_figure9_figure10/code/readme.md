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

- probe
  - 1200(1104/96)/396
  - 668
- mask/unmask
  - 256(152/104)/148
- get_direction
  - 372/182
- irq_type
  - 798(652/136)/496
- resume
  - 628(556/72)/392
- suspend
  - 368(296/72)/320
- set_wake
  - 324(208/116)/56
- ack
  - 136+106/92

```
0000000000001148 0000000000000208 t _RINvNtCs8YfjL7j61RY_6kernel3irq21irq_set_wake_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1v_
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep ack 
0000000000002248 0000000000000072 t _RINvNtCs8YfjL7j61RY_6kernel5power15freeze_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBO_
0000000000002320 0000000000000072 t _RINvNtCs8YfjL7j61RY_6kernel5power15resume_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBO_
0000000000002392 0000000000000072 t _RINvNtCs8YfjL7j61RY_6kernel5power16restore_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBP_
0000000000002464 0000000000000072 t _RINvNtCs8YfjL7j61RY_6kernel5power16suspend_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBP_
0000000000001784 0000000000000080 t _RINvNtCs8YfjL7j61RY_6kernel4gpio12set_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBK_
0000000000002060 0000000000000088 t _RINvNtCs8YfjL7j61RY_6kernel4gpio24direction_input_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBW_
0000000000001356 0000000000000096 t _RINvNtCs8YfjL7j61RY_6kernel4amba14probe_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBM_
0000000000001688 0000000000000096 t _RINvNtCs8YfjL7j61RY_6kernel4gpio12get_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBK_
0000000000002148 0000000000000100 t _RINvNtCs8YfjL7j61RY_6kernel4gpio25direction_output_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBX_
0000000000000572 0000000000000104 t _RINvNtCs8YfjL7j61RY_6kernel3irq16irq_ack_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1q_
0000000000000804 0000000000000104 t _RINvNtCs8YfjL7j61RY_6kernel3irq17irq_mask_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1r_
0000000000000908 0000000000000104 t _RINvNtCs8YfjL7j61RY_6kernel3irq19irq_unmask_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1t_
0000000000001012 0000000000000136 t _RINvNtCs8YfjL7j61RY_6kernel3irq21irq_set_type_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1v_
0000000000008128 0000000000000136 T _RNvXs4_Cs5J4rE82acbO_15gpio_pl061_rustNtB5_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel3irq4Chip3ack
0000000000001864 0000000000000196 t _RINvNtCs8YfjL7j61RY_6kernel4gpio22get_direction_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBU_
0000000000001148 0000000000000208 t _RINvNtCs8YfjL7j61RY_6kernel3irq21irq_set_wake_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1v_
0000000000001452 0000000000000236 t _RINvNtCs8YfjL7j61RY_6kernel4amba15remove_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBN_
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep ack_ 
0000000000000572 0000000000000104 t _RINvNtCs8YfjL7j61RY_6kernel3irq16irq_ack_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1q_
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep _ack 
0000000000000572 0000000000000104 t _RINvNtCs8YfjL7j61RY_6kernel3irq16irq_ack_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1q_
root@0035f146a62a:/data/bupt-rto
root@0035f146a62a:/data/bupt-rtos/linux# git branch
  20230503_nmi_metaspace_dk
  binder
  e1000
* ebpf_6_4
  rust
  rust-binder
  rust-dev
  rust-next
root@0035f146a62a:/data/bupt-rtos/linux# 
root@0035f146a62a:/data/bupt-rtos/linux# 
root@0035f146a62a:/data/bupt-rtos/linux# 
root@0035f146a62a:/data/bupt-rtos/linux# 
root@0035f146a62a:/data/bupt-rtos/linux# 
root@0035f146a62a:/data/bupt-rtos/linux# 
root@0035f146a62a:/data/bupt-rtos/linux# 
root@0035f146a62a:/data/bupt-rtos/linux# 

root@0035f146a62a:/data/bupt-rtos/linux# 
root@0035f146a62a:/data/bupt-rtos/linux# 
root@0035f146a62a:/data/bupt-rtos/linux# 
root@0035f146a62a:/data/bupt-rtos/linux# 
root@0035f146a62a:/data/bupt-rtos/linux# nm --print-size --size-sort --radix=d samples/rust/rust_semaphore.o | grep open
0000000000003184 0000000000000116 T _RNvXs2_CsebR9u8RMPFf_14rust_semaphoreNtB5_9FileStateNtNtCs8YfjL7j61RY_6kernel4file10Operations4open
0000000000000132 0000000000000128 t _RNvMs3_NtCs8YfjL7j61RY_6kernel4fileINtB5_16OperationsVtableINtNtB7_7miscdev12RegistrationNtCsebR9u8RMPFf_14rust_semaphore9FileStateEB1p_E13open_callbackB1r_
root@0035f146a62a:/data/bupt-rtos/linux# nm --print-size --size-sort --radix=d samples/rust/rust_semaphore.o | grep write
0000000000002792 0000000000000096 T _RNvXs1_CsebR9u8RMPFf_14rust_semaphoreNtB5_9FileStateNtNtCs8YfjL7j61RY_6kernel4file12IoctlHandler5write
0000000000001112 0000000000000272 t _RNvMs3_NtCs8YfjL7j61RY_6kernel4fileINtB5_16OperationsVtableINtNtB7_7miscdev12RegistrationNtCsebR9u8RMPFf_14rust_semaphore9FileStateEB1p_E19write_iter_callbackB1r_
0000000000000508 0000000000000284 t _RNvMs3_NtCs8YfjL7j61RY_6kernel4fileINtB5_16OperationsVtableINtNtB7_7miscdev12RegistrationNtCsebR9u8RMPFf_14rust_semaphore9FileStateEB1p_E14write_callbackB1r_
root@0035f146a62a:/data/bupt-rtos/linux# nm --print-size --size-sort --radix=d samples/rust/rust_semaphore.o | grep read 
0000000000002700 0000000000000092 T _RNvXs1_CsebR9u8RMPFf_14rust_semaphoreNtB5_9FileStateNtNtCs8YfjL7j61RY_6kernel4file12IoctlHandler4read
0000000000000884 0000000000000228 t _RNvMs3_NtCs8YfjL7j61RY_6kernel4fileINtB5_16OperationsVtableINtNtB7_7miscdev12RegistrationNtCsebR9u8RMPFf_14rust_semaphore9FileStateEB1p_E18read_iter_callbackB1r_
0000000000000260 0000000000000248 t _RNvMs3_NtCs8YfjL7j61RY_6kernel4fileINtB5_16OperationsVtableINtNtB7_7miscdev12RegistrationNtCsebR9u8RMPFf_14rust_semaphore9FileStateEB1p_E13read_callbackB1r_
root@0035f146a62a:/data/bupt-rtos/linux# nm --print-size --size-sort --radix=d samples/rust/rust_semaphore.o | grep release
0000000000000792 0000000000000092 t _RNvMs3_NtCs8YfjL7j61RY_6kernel4fileINtB5_16OperationsVtableINtNtB7_7miscdev12RegistrationNtCsebR9u8RMPFf_14rust_semaphore9FileStateEB1p_E16release_callbackB1r_
root@0035f146a62a:/data/bupt-rtos/linux# nm --print-size --size-sort --radix=d samples/rust/rust_semaphore.o | grep cosume 
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep probe
cat: drivers_gpio_rust: No such file or directory
(failed reverse-i-search)`grep probe': cat drivers_gpio_rust | ^Cep probe
(reverse-i-search)`': ^C
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep resume
cat: drivers_gpio_rust: No such file or directory
root@0035f146a62a:/data/bupt-rtos/linux# nm --print-size --size-sort --radix=d drivers/gpio/gpio_pl061_rust.o > drivers_gpio_rust
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep resume
0000000000002320 0000000000000072 t _RINvNtCs8YfjL7j61RY_6kernel5power15resume_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBO_
0000000000005384 0000000000000556 T _RNvXs0_Cs5J4rE82acbO_15gpio_pl061_rustNtB5_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel5power10Operations6resume
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep suspend
0000000000002464 0000000000000072 t _RINvNtCs8YfjL7j61RY_6kernel5power16suspend_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBP_
0000000000005088 0000000000000296 T _RNvXs0_Cs5J4rE82acbO_15gpio_pl061_rustNtB5_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel5power10Operations7suspend
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep mask   
0000000000000804 0000000000000104 t _RINvNtCs8YfjL7j61RY_6kernel3irq17irq_mask_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1r_
0000000000000908 0000000000000104 t _RINvNtCs8YfjL7j61RY_6kernel3irq19irq_unmask_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1t_
0000000000007824 0000000000000152 T _RNvXs4_Cs5J4rE82acbO_15gpio_pl061_rustNtB5_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel3irq4Chip4mask
0000000000007976 0000000000000152 T _RNvXs4_Cs5J4rE82acbO_15gpio_pl061_rustNtB5_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel3irq4Chip6unmask
(reverse-i-search)`': ^C
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep probe
0000000000000000 0000000000000001 b _RNvNvXs_Cs5J4rE82acbO_15gpio_pl061_rustNtB6_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel4amba6Driver5probe6CLASS1
0000000000000002 0000000000000001 b _RNvNvXs_Cs5J4rE82acbO_15gpio_pl061_rustNtB6_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel4amba6Driver5probes0_6CLASS1
0000000000000003 0000000000000001 b _RNvNvXs_Cs5J4rE82acbO_15gpio_pl061_rustNtB6_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel4amba6Driver5probes0_6CLASS2
0000000000000001 0000000000000001 b _RNvNvXs_Cs5J4rE82acbO_15gpio_pl061_rustNtB6_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel4amba6Driver5probes_6CLASS1
0000000000001356 0000000000000096 t _RINvNtCs8YfjL7j61RY_6kernel4amba14probe_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBM_
0000000000003984 0000000000001104 T _RNvXs_Cs5J4rE82acbO_15gpio_pl061_rustNtB4_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel4amba6Driver5probe
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep irq_type
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep _type
0000000000001012 0000000000000136 t _RINvNtCs8YfjL7j61RY_6kernel3irq21irq_set_type_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1v_
0000000000007172 0000000000000652 T _RNvXs4_Cs5J4rE82acbO_15gpio_pl061_rustNtB5_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel3irq4Chip8set_type
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep wake 
0000000000008264 0000000000000116 T _RNvXs4_Cs5J4rE82acbO_15gpio_pl061_rustNtB5_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel3irq4Chip8set_wake
0000000000001148 0000000000000208 t _RINvNtCs8YfjL7j61RY_6kernel3irq21irq_set_wake_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1v_
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep ack 
0000000000002248 0000000000000072 t _RINvNtCs8YfjL7j61RY_6kernel5power15freeze_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBO_
0000000000002320 0000000000000072 t _RINvNtCs8YfjL7j61RY_6kernel5power15resume_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBO_
0000000000002392 0000000000000072 t _RINvNtCs8YfjL7j61RY_6kernel5power16restore_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBP_
0000000000002464 0000000000000072 t _RINvNtCs8YfjL7j61RY_6kernel5power16suspend_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBP_
0000000000001784 0000000000000080 t _RINvNtCs8YfjL7j61RY_6kernel4gpio12set_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBK_
0000000000002060 0000000000000088 t _RINvNtCs8YfjL7j61RY_6kernel4gpio24direction_input_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBW_
0000000000001356 0000000000000096 t _RINvNtCs8YfjL7j61RY_6kernel4amba14probe_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBM_
0000000000001688 0000000000000096 t _RINvNtCs8YfjL7j61RY_6kernel4gpio12get_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBK_
0000000000002148 0000000000000100 t _RINvNtCs8YfjL7j61RY_6kernel4gpio25direction_output_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBX_
0000000000000572 0000000000000104 t _RINvNtCs8YfjL7j61RY_6kernel3irq16irq_ack_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1q_
0000000000000804 0000000000000104 t _RINvNtCs8YfjL7j61RY_6kernel3irq17irq_mask_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1r_
0000000000000908 0000000000000104 t _RINvNtCs8YfjL7j61RY_6kernel3irq19irq_unmask_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1t_
0000000000001012 0000000000000136 t _RINvNtCs8YfjL7j61RY_6kernel3irq21irq_set_type_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1v_
0000000000008128 0000000000000136 T _RNvXs4_Cs5J4rE82acbO_15gpio_pl061_rustNtB5_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel3irq4Chip3ack
0000000000001864 0000000000000196 t _RINvNtCs8YfjL7j61RY_6kernel4gpio22get_direction_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBU_
0000000000001148 0000000000000208 t _RINvNtCs8YfjL7j61RY_6kernel3irq21irq_set_wake_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1v_
0000000000001452 0000000000000236 t _RINvNtCs8YfjL7j61RY_6kernel4amba15remove_callbackNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEBN_
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep ack | grep 106
root@0035f146a62a:/data/bupt-rtos/linux# cat drivers_gpio_rust | grep ack | grep 136
0000000000001012 0000000000000136 t _RINvNtCs8YfjL7j61RY_6kernel3irq21irq_set_type_callbackINtNtNtB4_4gpio7irqchip14IrqChipAdapterNtCs5J4rE82acbO_15gpio_pl061_rust11PL061DeviceEEB1v_
0000000000008128 0000000000000136 T _RNvXs4_Cs5J4rE82acbO_15gpio_pl061_rustNtB5_11PL061DeviceNtNtCs8YfjL7j61RY_6kernel3irq4Chip3ack
root@0035f146a62a:/data/bupt-rtos/linux# python3
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 96/396
0.24242424242424243
>>> 104/148
0.7027027027027027
>>> 136/496
0.27419354838709675
>>> 72/392
0.1836734693877551
>>> 72/320
0.225
>>> 116/56
2.0714285714285716
>>> 0.24242424242424243+0.7027027027027027+0.27419354838709675+0.1836734693877551+0.225
1.627993962901797
>>> 1.627993962901797/5
0.3255987925803594
>>> 
```

remote: Resolving deltas: 100% (11/11), completed with 11 local objects.
To https://github.com/Richardhongyu/rfl-empirical-study.git
   f8db7a5..044a44e  main -> main
PS D:\RFL empirical study> python3
Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/2.6
0.3846153846153846
>>> 1/0.6
1.6666666666666667
>>> 668-396
272
>>> 272/396
0.6868686868686869
>>> 272
KeyboardInterrupt
>>> 668/396
1.6868686868686869
>>> 272/121
2.2479338842975207
>>> 228/268
0.8507462686567164
>>> 1.6868686868686869+2.2479338842975207+0.8507462686567164
4.7855488398229244
>>> 4.7855488398229244/3
1.5951829466076415
>>> 1104/396
2.787878787878788
>>> 152/148
1.027027027027027
>>> 652/496
1.314516129032258
>>> 556/392
1.4183673469387754
>>> 296/320
0.925
>>> 208/56
3.7142857142857144
>>> 296/320
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 1.6868686868686869+2.2479338842975207+0.8507462686567164+3.7142857142857144+0.925+1.4183673469387754+1.314516129032258+1.027027027027027+2.787878787878788
15.972623844985488
>>> 15.9/8
1.9875

### semaphore

- open
  - 244(116/128)/184
- write
  - 284/121
  - 272
- read
  - 248/268
  - 228
- ioctl(read write)
  - 92+96+216+104/324
- init
  - 176/208
  - 900
- exit
  - 120/148
  - 16, 116
- release
  - 92/140
- consume
  - 200/248
- ops
  - 84/272

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
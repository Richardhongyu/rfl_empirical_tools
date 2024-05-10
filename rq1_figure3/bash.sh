cp code/*.py /workspace/wrapped_func_structures/linux
pushd /workspace/wrapped_func_structures/linux
# functions
nm -l vmlinux | grep " T " > functions.txt && cat functions.txt | grep -v "_RN" | wc -l > functions_count
find rust/kernel/ -name *.rs | xargs cat | grep 'bindings::[A-Za-z_]*(' -o | sort | uniq |wc -l > rust_functions_count
python3 find.py
cat function_info.txt | grep linux/kernel/sched/ |wc -l
cat function_info.txt | grep kernel/locking |wc -l
cat function_info.txt | grep linux/mm |wc -l
cat function_info.txt | grep linux/fs |wc -l
cat function_info.txt | grep linux/net/ |wc -l
cat function_info.txt | grep linux/drivers |wc -l
cat function_info.txt | grep linux/kernel/time |wc -l
cat function_info.txt | grep linux/kernel/irq |wc -l
cat function_info.txt | grep kernel/cred |wc -l
cat function_info.txt | grep linux/secutiry |wc -l
cat function_info.txt | grep arch |wc -l

find rust/kernel/ -name *.rs | xargs cat | grep 'bindings::[A-Za-z_]*(' -o | sort | uniq  > rust_wrapped_functions.txt
python3 rust.py > result.bat
python3 count.py

# structures
find ./include -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
find kernel/ -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
find net -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
find mm -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
find fs -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l
find security/ -name *.h | xargs cat | grep '^[typedef ]*struct [A-Za-z_0-9]* {' | sort | uniq |  wc -l


popd
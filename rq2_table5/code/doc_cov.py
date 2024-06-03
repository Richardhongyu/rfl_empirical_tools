import re
import os
import glob

def find_function_declaration(file_content, function_name):
    # 通过反向查找找到函数名之前的最近一行
    lines = file_content.split('\n')
    has_meet_symbol = False
    for i, line in reversed(list(enumerate(lines))):
        regex = r'(?<![a-zA-Z0-9_]){}(?![a-zA-Z0-9_])'.format(re.escape(function_name))
        match = re.search(regex, line)
        if match:
            if has_meet_symbol:
                return lines[i-1].strip() if i > 0 else None
            else:
                if "EXPORT_SYMBOL" in lines[i]:
                    has_meet_symbol = True
    return None

def find_exported_functions_with_context(file_path, indent=''):
    export_num = 0
    with open(file_path, 'r') as file:
        content = file.read()

    # 匹配EXPORT_SYMBOL_GPL后面的函数名
    pattern = r'EXPORT_SYMBOL_GPL\(\s*([a-zA-Z_]\w*)\s*\);'
    matches = re.finditer(pattern, content)
    
    functions_with_context = []

    for match in matches:
        export_num += 1
        function_name = match.group(1)
        print(f'{indent}{function_name} is exported.')
        context = find_function_declaration(content, function_name)
        if context:
            functions_with_context.append((function_name, context))

    return (functions_with_context, export_num)

def has_doc(c: str) -> bool:
    if "*/" in c:
        return True
    else:
        return False

def count_num_in_file_path(file_path, indent=''):
    exported_functions_with_context, export_num = find_exported_functions_with_context(file_path, indent)
    doc_num = 0

    for function_name, context in exported_functions_with_context:
        print("{}Function '{}' is exported and its previous line is: {}".format(indent, function_name, context))
        if has_doc(context):
            doc_num += 1
            print(f'{indent}{function_name} has doc.')
    
    if doc_num != 0 or export_num != 0:
        print(f'{indent}{doc_num} functions of {export_num} exported functions have doc in {file_path}.')

    return (doc_num, export_num)

def count_num_in_directory(directory_path):
    print(f'In directory {directory_path}:')
    total_num_count = 0
    total_export_count = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.c'):
                file_path = os.path.join(root, file)
                num_count, export_num = count_num_in_file_path(file_path, indent='\t')
                total_num_count += num_count
                total_export_count += export_num
    print(f"{total_num_count} functions of {total_export_count} exported functions have doc in {directory_path}.")
    return (total_num_count, total_export_count)

def count_num_in_path(path):
    total_num_count = 0
    total_export_count = 0
    function_signatures = []
    if glob.has_magic(path):
        matching_files = glob.glob(path)
        for file_path in matching_files:
            if file_path.endswith('.c'):
                total_num_count, total_export_count = count_num_in_file_path(file_path)
            elif file_path.endswith('.h'):
                function_signatures = extract_function_signatures(file_path)
    else:
        if os.path.isdir(path):
            total_num_count, total_export_count = count_num_in_directory(path)
        elif os.path.isfile(path) and os.path.splitext(path)[1] in ['.h', '.c']:
            if path.endswith('.c'):
                total_num_count, total_export_count = count_num_in_file_path(path)
            else:
                function_signatures = extract_function_signatures(path)
        else:
            print(f"Error: {path} is not a valid file or directory path.")
    return (total_num_count, total_export_count, function_signatures)

def count_in_subsystem(path_list):
    doc_count = 0
    export_count = 0
    define_count = 0
    sig_list = []
    subsystem_name = path_list[0]
    for i in path_list[1:]:
        script_parent = os.path.dirname(os.path.realpath(__file__))
        real_path = os.path.join(script_parent, i)
        tdoc, texport, tsig_list = count_num_in_path(real_path)
        sig_list += tsig_list
        doc_count += tdoc
        export_count += texport

    # 处理.h中的函数签名是否有文档，然后将结果加到doc_count 和 export_count
    for i in path_list[1:]:
        tdefine, tdoc = find_function_definitions_in_path(i, sig_list)
        doc_count += tdoc
        define_count += tdefine

    print(f'In subsystem {subsystem_name} total export {export_count} functions and {doc_count} functions have doc.')
    return (subsystem_name, doc_count, export_count, define_count)

def find_function_definitions(c_file_path, function_signatures):
    with open(c_file_path, 'r') as file:
        content = file.read().splitlines()

    function_definitions = {}

    for signature, _, _ in function_signatures:
        # 构建函数定义的正则表达式
        pattern = re.escape(signature[:-1])
        for i, line in enumerate(content):
            match = re.search(pattern, line)
            if match:
                function_definitions[match.group(0)] = (i + 1, c_file_path, True if content[i-1] == "*/" else False)  # 行号从1开始

    return function_definitions

def find_function_definitions_in_path(path, function_signatures):
    function_definitions = {}
    if os.path.isfile(path) and os.path.splitext(path)[1] == '.c':
        function_definitions.update(find_function_definitions(path, function_signatures))
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.c'):
                    file_path = os.path.join(root, file)
                    function_definitions.update(find_function_definitions(file_path, function_signatures))
    
    defintion_count = len(function_definitions)
    doc_count = sum(1 for value in function_definitions.values() if value[2])
    return (defintion_count, doc_count)
    
def extract_function_signatures(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # 正则表达式匹配函数签名
    pattern = r'\b(?:\w+\s+)+(\w+)\s*\([^)]*\)\s*;'
    matches = re.finditer(pattern, content)

    function_signatures = []

    for match in matches:
        function_signature = match.group(0)
        if "static" not in function_signature:
            function_signatures.append((function_signature, match.start(), match.end()))

    return function_signatures

def main(subsystem_list: list):
    res = {}
    for subsystem in subsystem_list:
        subsystem_name, doc_count, export_count, define_count = count_in_subsystem(subsystem)
        res[subsystem_name] = (doc_count, export_count, define_count, doc_count/(export_count+define_count) if (export_count+define_count) != 0 else 0)

    for i in res.items():
        print(f'{i[0]}: {i[1][3]:.3f} [doc/(exported+included)]=[{i[1][0]}/({i[1][1]}+{i[1][2]})]')


if __name__ == '__main__':
    ebpf_list = """ebpf Documentation/bpf/ networking/filter Documentation/userspace-api/ebpf/ arch/*/net/* include/linux/bpf* include/linux/btf* include/linux/filter.h include/trace/events/xdp.h include/uapi/linux/bpf* include/uapi/linux/btf* include/uapi/linux/filter.h kernel/bpf/ kernel/trace/bpf_trace.c lib/test_bpf.c net/bpf/ net/core/filter.c net/sched/act_bpf.c net/sched/cls_bpf.c samples/bpf/ scripts/bpf_doc.py scripts/Makefile.btf scripts/pahole-version.sh tools/bpf/ tools/lib/bpf/ tools/testing/selftests/bpf/""".split()
    subsystem_list = [ebpf_list]
    main(subsystem_list)

import asyncio
import subprocess
import re
from concurrent.futures import ProcessPoolExecutor

async def run_command(command):
    """异步运行命令并返回输出"""
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return stdout.decode('utf-8', errors='ignore')

def extract_c_cloc(cloc_output):
    """从cloc输出中提取C和C/C++头文件的代码行数"""
    lines = cloc_output.split('\n')
    c_lines = 0
    cpp_header_lines = 0
    for line in lines:
        if 'C ' in line:
            c_lines += int(line.split()[4])
        elif 'C/C++ Header' in line:
            cpp_header_lines += int(line.split()[4])
    return c_lines, cpp_header_lines

def sync_process_path(path, keywords):
    """同步处理单个路径：统计代码行数和修复的bugs数量"""
    cloc_output = asyncio.run(run_command(f"cloc {path}"))
    c_lines, cpp_header_lines = extract_c_cloc(cloc_output)
    fixes_output = asyncio.run(run_command(f"git log --oneline -- {path}"))
    fixes_count = sum(len(re.findall(f"{keyword}", fixes_output, re.IGNORECASE)) for keyword in keywords)
    return path, c_lines, cpp_header_lines, fixes_count

async def process_block(block, keywords):
    lines = block.split('\n')
    block_name = lines[0]

    file_paths = [line.split('\t')[1] for line in lines if line.startswith('F:')]

    with ProcessPoolExecutor(max_workers=80) as executor:
        loop = asyncio.get_event_loop()
        tasks = [loop.run_in_executor(executor, sync_process_path, path, keywords) for path in file_paths]
        results = await asyncio.gather(*tasks)

    total_fixes = 0
    total_c_lines = 0
    total_cpp_header_lines = 0
    for result in results:
        path, c_lines, cpp_header_lines, fixes_count = result
        total_fixes += fixes_count
        total_c_lines += c_lines
        total_cpp_header_lines += cpp_header_lines

    print(f"Processing: {block_name} \n Total C/C++ Header lines in {block_name}: {total_c_lines+total_cpp_header_lines}\n Total number of fixes in {block_name}: {total_fixes}")

async def main():
    keywords = ["memory bugs", " oops" "wild point", "null point", "freed point", "freed-point", "accessing freed", "freeing","dereference", "out of array", "out-of-array", "out of range", "out-of-range", "out of bound", "out-of-bound", " oob", "use after free", " uaf", "use-after-free", "double free", "double-free", "overflow", "thread bugs", "data race", " race", "deadlock", "undefined behaviour", " UB "]

    with open('data.txt', 'r') as file:
        content = file.read()
    blocks = content.strip().split('\n\n')

    await asyncio.gather(*(process_block(block, keywords) for block in blocks))

asyncio.run(main())
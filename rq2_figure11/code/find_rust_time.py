import subprocess

with open("rfl_names", "r") as f:
    io_uring = f.readlines()

def bash_shell(cmd_l):
    try:
        result = subprocess.check_output(cmd_l, shell=True, stderr=subprocess.STDOUT).decode("utf-8")
        return result
                # print(j[0])
        # source_info = result.strip().split()[-1]  # Extract the last part (source file:line number)
    except subprocess.CalledProcessError as e:
        source_info = "ERROR: {}".format(e.output.decode('utf-8').strip())

names = set()
print(io_uring)
commands = []

for i in io_uring:
    print(i)
    name = i.strip()
    res = "git log --reverse --author="+name + " --pretty=format:\"%ad\" | head -n 1"
    commands.append(res)
    # email = bash_shell(res)
    # # print(email)
    # # names.append(email)
    # names.add(email)

with ThreadPoolExecutor(max_workers=60) as executor:
    results = executor.map(bash_shell, commands)
    for result in results:
        # print(result)
        names.add(result)

for i in names:
    print(i)

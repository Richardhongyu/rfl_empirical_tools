import subprocess

with open("rfl_commits", "r") as f:
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
for i in io_uring:
    name = i.strip()
    # if "Merge" in i.split(" ")[1]:
        # continue
    res = "git log --pretty=format:\"%ae\" "+name+" -1"
    email = bash_shell(res)
    # print(email)
    # names.append(email)
    names.add(email)

for i in names:
    print("\""+i+"\"")

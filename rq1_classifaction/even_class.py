import re
liness = []
with open("my_file_2022-07.txt", 'r', encoding='utf-8') as f:
    liness = f.readlines()

elines = []
olines = []

for i,j in enumerate(liness):
    if i % 2 == 0:
        elines.append(j)
        # print(j)
    else:
        olines.append(j)
        # print(j)

print(elines[0], olines[0])

year = [2022, 2022, 2022, 2022, 2023, 2023, 2023,]
month = [1, 4, 7, 10, 1, 4, 7]

for w in range(0,7):
    lines = []
    for i in range(len(elines)):
        if "Reply" not in olines[i]:
            # print(olines[i])
            # print(olines[i][:4], olines[i][-3:])
            if int(olines[i][:4]) < year[w] or (int(olines[i][:4]) <= year[w] and int(olines[i][-3:]) <= month[w]):
                lines.append(elines[i])

    # without_re_lines = without_v_lines
    # without_re_lines = []
    # for line in lines:
    #     if "Re:" not in line and "RE:" not in line:
    #         without_re_lines.append(line)

    # without_v_lines = []
    # for line in without_re_lines:
    #     match1 = re.match("\[PATCH v\d+ \d+\/\d+\]", line)
    #     match2 = re.match("\[PATCH v\d+]", line)
    #     if not match1 and not match2:
    #         without_v_lines.append(line)

    safety_abstraction = []
    drivers = []
    build = []
    bugs = []
    rust = []
    docs = []
    linux = []
    questions =[]
    community = []
    others = []

    for line in lines:
        if "Kbuild" in line or "kbuild" in line or "kallsyms" in line or "scripts: add" in line or "build" in line or "scripts: " in line or "Build" in line or "scripts" in line or "fixdep" in line or "modpost" in line or "kconfig" in line or "Kconfig" in line or "config" in line:
            build.append(line)
        elif "] rust: alloc:" in line or "compiler-builtin" in line or "upgrade" in line or "pin" in line :
            rust.append(line)
        elif "sample" in line or "Samples" in line or "driver" in line or "Rust V4L2 support" in line or "binder: " in line or "TLS" in line or "puzzlefs" in line:
            drivers.append(line)
        elif "docs" in line or "Documentation" in line:
            docs.append(line)
        elif "[GIT PULL]" in line:
            linux.append(line)
        elif "] rust: " in line or "abstractions" in line or "Bindings " in line or "KUnit" in line or "print" in line:
            safety_abstraction.append(line)
        elif "error" in line or " warning: " in line:
            bugs.append(line)
        elif "?" in line:
            questions.append(line)
        elif "MAINTAINERS" in line or "Reminder" in line:
            community.append(line)
        else:
            others.append(line)
            
    print("-----------------------------------------------------------")    
    print("safety_abstraction length is ", len(safety_abstraction))
    print("drivers length is ", len(drivers))
    print("build length is ", len(build))
    print("bugs length is ", len(bugs))
    print("docs length is ", len(docs))
    print("rust length is ", len(rust))
    print("linux length is ", len(linux))
    print("questions length is ", len(questions))
    print("others length is ", len(others))
    print("-----------------------------------------------------------")


    with open('safety_abstraction.txt', 'w') as f:
        # 将列表的所有元素写入文件
        f.writelines(safety_abstraction)

    with open('drivers.txt', 'w') as f:
        # 将列表的所有元素写入文件
        f.writelines(drivers)

    with open('build.txt', 'w') as f:
        # 将列表的所有元素写入文件
        f.writelines(build)

    with open('bugs.txt', 'w') as f:
        # 将列表的所有元素写入文件
        f.writelines(bugs)

    with open('docs.txt', 'w') as f:
        # 将列表的所有元素写入文件
        f.writelines(docs)

    with open('linux.txt', 'w') as f:
        # 将列表的所有元素写入文件
        f.writelines(linux)

    with open('rust.txt', 'w') as f:
        # 将列表的所有元素写入文件
        f.writelines(rust)

    with open('questions.txt', 'w') as f:
        # 将列表的所有元素写入文件
        f.writelines(questions)

    with open('others.txt', 'w') as f:
        # 将列表的所有元素写入文件
        f.writelines(others)
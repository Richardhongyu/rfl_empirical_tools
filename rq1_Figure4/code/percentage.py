with open('mid_value2', 'r') as f:
    a = f.read()

res = a.split("-----------------------------------------------------------")
for i in range(1,len(res)):
#    print(res[i])
    print("-----------------------------------------------------------")
    lines = res[i].split("\n")
    total = 0
    for j, k in enumerate(lines):
        total += int(k)
    for j, k in enumerate(lines):
        print(int(k.split(" ")[-1])/total*100)
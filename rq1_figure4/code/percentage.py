with open('mid_value2', 'r') as f:
    a = f.read()

res = a.split("-----------------------------------------------------------")
print(res)
for i in range(1,len(res)):
#    print(res[i])
    print("-----------------------------------------------------------")
    lines = res[i].split("\n")
    total = 0
#    print(lines)
    if lines != "":
        for j, k in enumerate(lines):
            if k!= "":
                total += int(k)
        for j, k in enumerate(lines):
            if k!= "":
                print(int(k.split(" ")[-1])/total*100)

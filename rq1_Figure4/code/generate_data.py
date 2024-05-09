with open('mid_value1', 'r') as f:
    a = f.read()
middle_values = []

res = a.split("-----------------------------------------------------------")
for i in range(1,len(res)-1):
#    print(res[i])
    print("-----------------------------------------------------------")
    lines = res[i].split("\n")
    total = 0
    for j, k in enumerate(lines):
        if "is" in k and (j<5 or j==6):
            # total += int(k.split(" ")[-1])
            if i == 1:
                middle_values.append(int(k.split(" ")[-1]))
                print(k.split(" ")[-1])
            else:
                print(k.split(" ")[-1] - middle_values[j-1])
# a = '''-----------------------------------------------------------
# safety_abstraction length is  39
# drivers length is  40
# build length is  122
# bugs length is  6
# docs length is  15
# rust length is  0
# linux length is  0
# questions length is  44
# others length is  376
# -----------------------------------------------------------
# -----------------------------------------------------------
# safety_abstraction length is  77
# drivers length is  46
# build length is  144
# bugs length is  6
# docs length is  22
# rust length is  0
# linux length is  0
# questions length is  48
# others length is  413
# -----------------------------------------------------------
# -----------------------------------------------------------
# safety_abstraction length is  102
# drivers length is  61
# build length is  199
# bugs length is  6
# docs length is  38
# rust length is  0
# linux length is  0
# questions length is  48
# others length is  466
# -----------------------------------------------------------
# -----------------------------------------------------------
# safety_abstraction length is  195
# drivers length is  97
# build length is  303
# bugs length is  8
# docs length is  88
# rust length is  4
# linux length is  0
# questions length is  48
# others length is  509
# -----------------------------------------------------------
# -----------------------------------------------------------
# safety_abstraction length is  419
# drivers length is  116
# build length is  437
# bugs length is  21
# docs length is  96
# rust length is  19
# linux length is  6
# questions length is  48
# others length is  539
# -----------------------------------------------------------
# -----------------------------------------------------------
# safety_abstraction length is  1040
# drivers length is  202
# build length is  507
# bugs length is  31
# docs length is  117
# rust length is  174
# linux length is  14
# questions length is  48
# others length is  644
# -----------------------------------------------------------
# -----------------------------------------------------------
# safety_abstraction length is  1436
# drivers length is  384
# build length is  595
# bugs length is  35
# docs length is  124
# rust length is  192
# linux length is  15
# questions length is  48
# others length is  677
# -----------------------------------------------------------\
# '''
# generate code to read each block in variable a, and calculte the percentage of each length in the total length of the same tiem of all the blocks
# generate the following data form the above text
# oop1 = np.array([22,36,48,73,149,345,462])
# oop2 = np.array([12,16,22,28,33,43,76])
# oop3 = np.array([29,43,69,111,148,161,187])
# oop4 = np.array([2,2,2,3,4,5,5])
# oop5 = np.array([0,0,0,2,8,60,65])

# op1 = []
# op2 = []
# op3 = []
# op4 = []
# op5 = []

# for i in range(0,7):

# middle_values = []

# res = a.split("-----------------------------------------------------------")
# for i in range(1,len(res)-1):
# #    print(res[i])
#     print("-----------------------------------------------------------")
#     lines = res[i].split("\n")
#     total = 0
#     for j, k in enumerate(lines):
#         if "is" in k and (j<5 or j==6):
#             # total += int(k.split(" ")[-1])
#             if i == 1:
#                 middle_values.append(int(k.split(" ")[-1]))
#                 print(k.split(" ")[-1])
#             else:
#                 print(k.split(" ")[-1] - middle_values[j-1])
    # for j, k in enumerate(lines):
    #     if "is" in k and (j<5 or j==6):
    #         print(int(k.split(" ")[-1])/total*100)


# res = a.split("-----------------------------------------------------------")
# for i in range(1,len(res)-1):
# #    print(res[i])
#     print("-----------------------------------------------------------")
#     lines = res[i].split("\n")
#     total = 0
#     for j, k in enumerate(lines):
#         if "is" in k and (j<5 or j==6):
#             total += int(k.split(" ")[-1])
#     for j, k in enumerate(lines):
#         if "is" in k and (j<5 or j==6):
#             print(int(k.split(" ")[-1])/total*100)

# generate code to read each block in variable a, and calculte the percentage of each length in the total length of the blocks
# for i in range(1,len(res)-1):
#     print(res[i])
#     print("-----------------------------------------------------------")
#     lines = res[i].split("\n")
#     total = 0
#     for j, k in enumerate(lines):
#         if "is" in k:
#             if i == 1:
#                 total += int(k.split(" ")[-1])
#             else:
#                 total += int(k.split(" ")[-1])
#     for j, k in enumerate(lines):
#         if "is" in k:
#             print(k.split(" ")[-1]/total*100)


# res = a.split("-----------------------------------------------------------")
# blocks = []
# for i in range(1,len(res)-1):
#     print(res[i])
#     print("-----------------------------------------------------------")
#     lines = res[i].split("\n")
#     for j, k in enumerate(lines):
#         if i == 1:
#             blocks.append(j)
#         else:
#             blocks[j] += int(k.split(" ")[-1])
# for i in range(1,len(res)-1):
#     lines = res[i].split("\n")
#     for j, k in enumerate(lines):
#         print(k/blocks[j]*100)
#     # print(blocks[i]/blocks[0]*100)
#     # print("-----------------------------------------------------------")


# generate the following data form the above text
# oop1 = np.array([22,36,48,73,149,345,462])
# oop2 = np.array([12,16,22,28,33,43,76])
# oop3 = np.array([29,43,69,111,148,161,187])
# oop4 = np.array([2,2,2,3,4,5,5])
# oop5 = np.array([0,0,0,2,8,60,65])

# op1 = []
# op2 = []
# op3 = []
# op4 = []
# op5 = []

# for i in range(0,7):
    
# res = a.split("-----------------------------------------------------------")
# blocks = []
# for i in range(1,len(res)-1):
#     print(res[i])
#     print("-----------------------------------------------------------")
#     lines = res[i].split("\n")
#     for j, k in enumerate(lines):
#         if "is" in k:
#             if i == 1:
#                 print(j)
#                 print(k.split("  ")[-1])
#                 blocks.append(int(k.split("  ")[-1]))
#             else:
#                 print(j)
#                 print(k.split("  ")[-1])
#                 blocks[j-1] += int(k.split("  ")[-1])
# for i in range(1,len(res)-1):
#     lines = res[i].split("\n")
#     for j, k in enumerate(lines):
#         if "is" in k:
#             print(int(k.split("  ")[-1])/blocks[j-1]*100)
#     # print(blocks[i]/blocks[0]*100)
#     # print("-----------------------------------------------------------")


# generate the following data form the above text
# oop1 = np.array([22,36,48,73,149,345,462])
# oop2 = np.array([12,16,22,28,33,43,76])
# oop3 = np.array([29,43,69,111,148,161,187])
# oop4 = np.array([2,2,2,3,4,5,5])
# oop5 = np.array([0,0,0,2,8,60,65])

# op1 = []
# op2 = []
# op3 = []
# op4 = []
# op5 = []

# for i in range(0,7):
import matplotlib.pyplot as plt
lines1 = [
    "#############################",
    "#",
    "####",
    "##",
    "###########",
    "#####",
    "###",
    "##",
    "###",
    "##",
    "0",
    "0",
    "0"
]

lines2 = [
    "########################",
    "########",
    "##############",
    "#################################",
    "###############################",
    "#################################",
    "####################",
    "#####################",
    "############",
    "################",
    "##############",
    "#####################",
    "####################",
]

time_line = [3,6,12,24,48,72,96,120,144,168,192,216,240]
commit_count1 = [] 
commit_count2 = []

for line in lines1:
    count = line.count("#")
    print(count)
    commit_count1.append(count)

print("---------------")

for line in lines2:
    count = line.count("#")
    print(count)
    commit_count2.append(count)




fig, ax = plt.subplots()
ax.plot(time_line, commit_count1, marker='o', label="RFL", linestyle='-', color='b')
ax.plot(time_line, commit_count2, marker='x', label="netdev", linestyle='-', color='r')

# Format the x-axis as dates
# ax.xaxis.set_major_locator(mdates.AutoDateLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Set labels and title
fs= 20
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
ax.set_xlabel('Date(month)',fontsize=fs)
ax.set_ylabel('The developer experiences',fontsize=fs)
# ax.set_title('Developers distribution',font)

# Rotate and align the x-axis labels
fig.autofmt_xdate()

image_file = 'distribution_developers_two.png'
plt.legend(fontsize=fs, loc=4, ncol=4, bbox_to_anchor=(0.8, 1), frameon=False)
plt.savefig(image_file, bbox_inches="tight")
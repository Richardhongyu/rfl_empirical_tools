import matplotlib.pyplot as plt

# Define the data
positive_opinions_1 = 148
negative_opinions_1 = 216

positive_opinions_2 = 40
negative_opinions_2 = 63

# Create labels for the pie chart
labels = ['Y Positive',  'lwn Positive',  'lwn Negative', 'Y Negative',]

fontsize = 23

# Define the sizes of the pie chart slices
sizes = [positive_opinions_1, positive_opinions_2,  negative_opinions_2, negative_opinions_1,]

# Define colors for the pie chart
colors = ["green", "coral", 'lightgreen', 'lightcoral']

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 20})
# plt.title('Opinions Distribution', fon)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()
plt.savefig("opioions.png", bbox_inches="tight")

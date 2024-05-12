import git
import json
import sys
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from datetime import datetime
from collections import Counter
from datetime import datetime, timedelta

# Read the first file
filename1 = '../data/rflcommits' # rflcommits rfldevcommits
with open(filename1, 'r', encoding="ISO-8859-1") as file1:
    lines1 = file1.readlines()

# Read the second file
filename2 = '../data/commits'
with open(filename2, 'r', encoding="ISO-8859-1") as file2:
    lines2 = file2.readlines()

# Process each line in the first file
hash_codes1 = set()
for line in lines1:
    line = line.strip()
    if line:
        parts = line.split(' ', 1)
        if len(parts) == 2:
            hash_code = parts[0]
            hash_codes1.add(hash_code)

# Process each line in the second file
hash_codes2 = set()
for line in lines2:
    line = line.strip()
    if line:
        parts = line.split(' ', 1)
        if len(parts) == 2:
            hash_code = parts[0]
            hash_codes2.add(hash_code)

# Find the commits in the first file but not in the second file
commits_only_in_first = hash_codes1 - hash_codes2
commits_only_in_first = list(commits_only_in_first)

# Print the commits only in the first file
print("Commits only in the first file:")
for commit in commits_only_in_first:
    print(commit)

# Define the repository path
repo_path = '/home/yyx/rfl'

# Create a Git repository object
repo = git.Repo(repo_path)

# Initialize lists to store commit dates and their corresponding indices
commit_dates = []
indices = []

def generate_date_ranges(start_date, end_date, delta):
    current_date = start_date
    while current_date < end_date:
        yield current_date
        current_date += delta

# 设置起始和结束日期
start_date = datetime(2021, 7, 1)
end_date = datetime(2023, 5, 30)

# 设置时间段长度为4周
period_length = timedelta(weeks=1)

# Define the basic unit as a week
# unit = timedelta(weeks=4)

# Initialize lists to store the dates and commit counts
dates = []
commit_counts = []

# Initialize variables for counting commits within each week
current_date = start_date
commit_count = 0

# commits_only_in_first.reverse()

commit_data = []

for i, commit_id in enumerate(commits_only_in_first):
    current_date = start_date
    try:
        commit_date = repo.commit(commit_id).authored_datetime.date()
        commit_date = datetime.combine(commit_date, datetime.min.time())
        commit_data.append((commit_id, commit_date))
    except git.exc.BadName:
        print(f"Commit ID {commit_id} does not exist in the repository.")

# commit_data.sort(key=lambda x: x[1])

# Sort the commit data based on commit date
commit_data.sort(key=lambda x: x[1])

# Extract the sorted dates and corresponding commit counts
sorted_commit_dates = [date for _, date in commit_data]
commit_count_values = list(range(1, len(commit_data) + 1))

date_ranges = list(generate_date_ranges(start_date, end_date, period_length))
# commit_count_values = list(range(1, len(date_ranges) + 1))
commit_count_values = [0]
j_i = 0 
for i in range(1, len(date_ranges)):
    # [i]
    number_commits = 0
    for j in range(0, len(sorted_commit_dates)):
        if sorted_commit_dates[j]>date_ranges[i-1] and   sorted_commit_dates[j] <date_ranges[i]:
            number_commits += 1
        # else:
        #     break
    commit_count_values.append(number_commits)

# Plot the number of commits against the date
fig, ax = plt.subplots()
ax.plot(date_ranges, commit_count_values, marker='o', linestyle='-', color='b')

# Format the x-axis as dates
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Set labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Number of Commits')
ax.set_title('Rfl Commits')

# Rotate and align the x-axis labels
fig.autofmt_xdate()

# Show the plot
script_name = sys.argv[0]
image_file = f'../imgs/{script_name}.pdf'
plt.savefig(image_file)

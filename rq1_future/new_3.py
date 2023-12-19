import git
import json
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from datetime import datetime
from collections import Counter
from datetime import datetime, timedelta

# Read the first file
filename1 = 'rflcommits' # rflcommits rfldevcommits
with open(filename1, 'r', encoding="ISO-8859-1") as file1:
    lines1 = file1.readlines()

# Read the second file
filename2 = 'commits'
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
# # commits_only_in_first = []
# for hash_code in hash_codes1:
#     if hash_code not in hash_codes2:
#         commits_only_in_first.append(hash_code)

# Print the commits only in the first file
print("Commits only in the first file:")
for commit in commits_only_in_first:
    print(commit)

json_file = 'commit_dates2.json'
with open(json_file, 'w') as file:
    json.dump(commits_only_in_first, file, indent=4)

print(f"Commit dates saved to {json_file}.")

# Define the repository path
repo_path = './'

# Create a Git repository object
repo = git.Repo(repo_path)

# Initialize lists to store commit dates and their corresponding indices
commit_dates = []
indices = []

# Define the start and end dates of the analysis period
start_date = datetime(2021, 7, 1)  # Replace with your desired start date
end_date = datetime(2023, 5, 30)  # Replace with your desired end date

# Define the basic unit as a week
unit = timedelta(weeks=4)

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
        commit_date = git.Repo().commit(commit_id).authored_datetime.date()
        commit_date = datetime.combine(commit_date, datetime.min.time())
        commit_data.append((commit_id, commit_date))
        # if start_date <= commit_date <= end_date:
            # while commit_date >= current_date + unit:
                # commit_data.append((commit_id, commit_date))
                # dates.append(current_date)
                # commit_counts.append(commit_count)
                # current_date += unit
                # commit_count = 0
            # commit_count += 1
    except git.exc.BadName:
        print(f"Commit ID {commit_id} does not exist in the repository.")

# commit_data.sort(key=lambda x: x[1])


# Sort the commit data based on commit date
commit_data.sort(key=lambda x: x[1])

json_file = 'commit_dates3.json'
with open(json_file, 'w') as file:
    json.dump([i[0] for i in commit_data], file, indent=4)

# Extract the sorted dates and corresponding commit counts
sorted_commit_dates = [mdates.date2num(date) for _, date in commit_data]
commit_count_values = list(range(1, len(commit_data) + 1))

# Plot the number of commits against the date
fig, ax = plt.subplots()
ax.plot(sorted_commit_dates, commit_count_values, marker='o', linestyle='-', color='b')

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
# plt.show()

# for i, commit_id in enumerate(commits_only_in_first):
#     current_date = start_date
#     try:
#         commit_date = git.Repo().commit(commit_id).authored_datetime.date()
#         commit_date = datetime.combine(commit_date, datetime.min.time())
#         if start_date <= commit_date <= end_date:
#             while commit_date >= current_date + unit:
#                 dates.append(current_date)
#                 commit_counts.append(commit_count)
#                 current_date += unit
#                 commit_count = 0
#             commit_count += 1
#     except git.exc.BadName:
#         print(f"Commit ID {commit_id} does not exist in the repository.")

# # # Iterate over the commit IDs
# # for i, commit_id in enumerate(commits_only_in_first):
# #     try:
# #         commit = repo.commit(commit_id)
# #         commit_dates.append(commit.authored_datetime)
# #         indices.append(i)
# #     except git.exc.BadName:
# #         print(f"Commit ID {commit_id} does not exist in the repository.")

# # Append the last week's data if it has commits
# if commit_count > 0:
#     dates.append(current_date)
#     commit_counts.append(commit_count)

# # Convert dates to matplotlib date format
# plot_dates = mdates.date2num(dates)

# # Plot the number of commits against the date
# fig, ax = plt.subplots()
# ax.plot_date(plot_dates, commit_counts, marker='o', linestyle='-', color='b')

# # Format the x-axis as dates
# ax.xaxis.set_major_locator(mdates.AutoDateLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# # Set labels and title
# ax.set_xlabel('Date')
# ax.set_ylabel('Number of Commits')
# ax.set_title('Commits in file1 but not in file2 (per week)')

# # Rotate and align the x-axis labels
# fig.autofmt_xdate()

# Show the plot
image_file = 'commit_dates_new.png'
plt.savefig(image_file)




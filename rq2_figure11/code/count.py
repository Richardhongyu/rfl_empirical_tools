from datetime import datetime

# List of timestamps
timestamps = [
    "Sat Sep 21 15:23:04 2019 -0700",
    "Tue Mar 22 10:49:45 2022 -0400",
    "Sat Nov 21 01:55:09 2020 +0000",
    "Wed Dec 11 17:45:11 2019 +0000",
    "Thu Jul 23 17:30:02 2020 +0800",
    "Mon Nov 23 15:15:33 2020 +0100",
    "Fri Jan 13 14:29:07 2006 -0800",
    "Wed Mar 9 14:08:04 2016 -0800",
    "Wed Dec 7 10:43:05 2022 +0900",
    "Wed Feb 3 10:44:30 2021 +0800",
    "Wed Feb 24 10:16:31 2021 -0300",
    "Wed Sep 8 16:38:28 2021 +0800",
    "Sun May 1 08:58:36 2005 -0700",
    "Sun Dec 1 16:08:46 2019 +0900",
    "Thu Nov 10 17:41:21 2022 +0100",
    "Tue Jan 3 13:33:31 2006 +0100",
    "Wed Nov 20 11:05:01 2013 +1100",
    "Tue Jan 31 20:02:00 2012 -0800",
    "Sat Nov 27 11:28:53 2021 +0100",
    "Mon Sep 18 22:21:25 2017 -0700",
    "Wed Jan 11 12:20:50 2023 -0300",
    "Thu Nov 10 17:41:35 2022 +0100",
    "Thu Jul 2 22:25:52 2015 +0800",
    "Tue Sep 17 12:37:27 2019 +0200",
    "Fri Jul 4 09:59:33 2008 -0700",
    "Fri Mar 5 13:26:02 2021 +0800",
    "Fri Aug 12 09:10:27 2016 -0400",
    "Thu Oct 24 15:46:31 2019 -0700",
    "Wed Mar 27 00:41:25 2019 +0000",
    "Thu Apr 6 01:54:35 2023 -0300",
    "Sat Aug 17 03:07:02 2019 +0530",
    "Sun Jun 23 23:33:48 2013 -0700",
]

# Convert all timestamps to datetime objects, normalizing all to be offset-naive
dates = []
for ts in timestamps:
    try:
        # Parse with timezone, then convert to offset-naive by stripping the timezone
        date = datetime.strptime(ts.strip(), date_format).replace(tzinfo=None)
    except ValueError:
        # If fails, parse without timezone directly
        date = datetime.strptime(ts.strip(), date_format_without_tz)
    dates.append(date)

# Reference date (also made offset-naive to match others)
reference_date = datetime.strptime("Sun Dec 11 14:15:18 2021", date_format_without_tz)

# Calculate differences in months
differences_in_months = [(reference_date - date).days // 30 for date in dates[:-1]]

# Define month bins
month_bins = [0, 3, 6, 12, 24, 48, 72, 96, 120, 144, 168, 192, 216, 240]

# Count differences into month bins
counts = {bin: 0 for bin in month_bins}
for diff in differences_in_months:
    for bin in sorted(month_bins, reverse=True):
        if diff >= bin:
            counts[bin] += 1
            break

counts

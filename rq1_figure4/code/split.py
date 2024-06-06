import sqlite3
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import defaultdict
i = 0
async def fetch_email_time(session, mid):
    url = f"https://lore.kernel.org/rust-for-linux/{mid}/"

    try:
        async with session.get(url) as response:
            content = await response.text()
            soup = BeautifulSoup(content, "html.parser")
            time_element = soup.find(id='t')
            time_element_real = soup.find_all("b")[2]
            if time_element:
                global i
                i+=1
                print(i)
                print(time_element.text+"\n"+time_element_real.text.strip().split("`")[0].split(" ")[0][:7]+"\n")
                # print(time_element_real.text.strip().split("`")[0].split(" ")[0][:7])
                # return time_element.text.strip().split("`")[0].split(" ")[0][:7]
                return time_element.text+"\n"+time_element_real.text.strip().split("`")[0].split(" ")[0][:7]+"\n"
                # if time_element_real.text.strip().split("`")[0].split(" ")[0][:7] < "2022-07":
                #     return time_element.text+"\n"
                # else:
                #     return None
            else:
                return None
    except:
        async with session.get(url) as response:
            content = await response.text()
            soup = BeautifulSoup(content, "html.parser")
            time_element = soup.find(id='t')
            time_element_real = soup.find_all("b")[2]

            if time_element:
                # global i
                i+=1
                print(i)
                print(time_element.text+"\n"+time_element_real.text.strip().split("`")[0].split(" ")[0][:7]+"\n")
                # print(time_element_real.text.strip().split("`")[0].split(" ")[0][:7])
                # return time_element.text.strip().split("`")[0].split(" ")[0][:7]
                return time_element.text+"\n"+time_element_real.text.strip().split("`")[0].split(" ")[0][:7]+"\n"
                # if time_element_real.text.strip().split("`")[0].split(" ")[0][:7] < "2022-07":
                #     return time_element.text+"\n"
                # else:
                #     return None
            else:
                return None

async def retrieve_email_times_and_plot_counts():
    # Connect to the SQLite database
    conn = sqlite3.connect('msgmap.sqlite3')  # Replace 'your_database_file.db' with the actual file path

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Fetch all rows from the msgmap table
    cursor.execute("SELECT mid FROM msgmap")
    rows = cursor.fetchall()

    # Dictionary to store the email count per time
    email_counts = defaultdict(int)

    async with aiohttp.ClientSession() as session:
        tasks = []

        # Create a list of tasks for each message ID
        number  = 0
        for row in rows:
            mid = row[0]
            taskss = asyncio.ensure_future(fetch_email_time(session, mid))
            number+=1
            # if number > 3000:
                # break
            # print(taskss)
            # task = taskss[0]
            # time = taskss[1]
            # if time < "2023-07":
            tasks.append(taskss)

        # Gather results from the tasks
        results = await asyncio.gather(*tasks)

        # Iterate over the results and increment the email count for each time
        # for time in results:
        #     if time:
        #         email_counts[time] += 1

    
    with open('my_file_2022-07.txt', 'w') as f:
        # 将列表的所有元素写入文件
        f.writelines(results)
    # # Plotting the figure
    # times = list(email_counts.keys())
    # counts = list(email_counts.values())

    # for i,d in enumerate(counts):
    #     if i >0:
    #         counts[i]+=counts[i-1]

    # plt.plot(times, counts)
    # plt.xlabel("Time")
    # plt.ylabel("Email Count")
    # plt.title("Sum Number of Emails over Time - Rust-for-Linux Mailing List")
    # plt.xticks(rotation=45, ha="right")
    # plt.tight_layout()
    # plt.savefig("rust_for_linux_email_counts.png")

    # # Close the cursor and the database connection
    # cursor.close()
    # conn.close()

# Run the async function to retrieve email times and plot email counts over time
loop = asyncio.get_event_loop()
loop.run_until_complete(retrieve_email_times_and_plot_counts())

import requests
from bs4 import BeautifulSoup
import time

def get_pr_date_list(url, i, proxies=None) -> list:
    pr_dates = []
     # Make an HTTP GET request to the URL using the provided proxies (if any)
    params  = {
        'page':i,
        "q":"is:pr"
    }
    response = requests.get(url, params=params,  proxies=proxies)
    
    # Check if the request was successful
    while response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        time.sleep(1)
        response = requests.get(url, params=params,  proxies=proxies)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    commits_tab_counter_element = soup.select('.opened-by')
    date = soup.select('relative-time[datetime]')
    for i in range(0, len(commits_tab_counter_element)):
        d = date[i].attrs['datetime']
        index = commits_tab_counter_element[i].text.split("\n")[1].split("#")[1]
        is_merged = ("merged" in commits_tab_counter_element[i].text)
        print(is_merged)
        pr_dates.append((index, d, is_merged))
    print(pr_dates)
    return pr_dates

def find_commits_tab_counter(url, proxies=None):
    # Make an HTTP GET request to the URL using the provided proxies (if any)
    response = requests.get(url, proxies=proxies)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element with the ID 'commits_tab_counter'
    commits_tab_counter_element = soup.find(id='commits_tab_counter')

    if commits_tab_counter_element:
        return commits_tab_counter_element.text.strip()
    else:
        return None

if __name__ == "__main__":
    # Replace 'YOUR_PROXY_URL' with the actual proxy URL you want to use
    proxy_url = 'http://172.27.240.1:7890'  # Example: 'http://123.456.789.10:8080'
    proxies = {
        'http': proxy_url,
        'https': proxy_url
    }

    # url = "https://github.com/Rust-for-Linux/linux/pull/1009/commits"
    url = "https://github.com/Rust-for-Linux/linux/pulls"
    pr_dates = []
    for i in range(1,33):
        print(i)
        pr_dates.extend(get_pr_date_list(url.format(i), i, proxies))
        time.sleep(0.5)

    date_count = {}
    with open('../data/data.txt', 'w') as f:
        for pr_index, date, is_merged in pr_dates:
            url = "https://github.com/Rust-for-Linux/linux/pull/{}/commits".format(pr_index)
            commits_tab_counter = int(find_commits_tab_counter(url, proxies))
            if commits_tab_counter:
                print(f"{commits_tab_counter} commits in PR {pr_index}")
                date_count[pr_index] = (date, commits_tab_counter)
                print((pr_index, date, commits_tab_counter, is_merged), file=f)
            else:
                print("Commits tab counter not found.")
    print(f'Total commits number under review: {date_count.items()}')

import requests
from bs4 import BeautifulSoup

def get_pr_numbers(url, i, proxies=None) -> list:
    pr_numbers = []
     # Make an HTTP GET request to the URL using the provided proxies (if any)
    params  = {
        'page':i,
        "q":"is:pr is:open"
    }
    response = requests.get(url, params=params,  proxies=proxies)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    commits_tab_counter_element = soup.select('.opened-by')
    for i in range(0, len(commits_tab_counter_element)):
        num = commits_tab_counter_element[i].text.split("opened")[0].split("\n")[1].split("#")[1]
        pr_numbers.append(num)
    
    return pr_numbers

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
    pr_numbers = []
    for i in range(1, 6):
        pr_numbers.extend(get_pr_numbers(url.format(i), i, proxies))

    numebrs = []
    for pr in pr_numbers:
        url = "https://github.com/Rust-for-Linux/linux/pull/{}/commits".format(pr)
        commits_tab_counter = find_commits_tab_counter(url, proxies)
        if commits_tab_counter:
            print(f"{commits_tab_counter} commits in PR {pr}")
            numebrs.append(int(commits_tab_counter))
        else:
            print("Commits tab counter not found.")
    print(f'Total commits number under review: {sum(numebrs)}')

import requests
from bs4 import BeautifulSoup

def find_commits_tab_counter(url, i, proxies=None):
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
    # print(response.text)

    # Find the element with the class 'commits_tab_counter'
    # commits_tab_counter_element = soup.find(id = 'commits_tab_counter')
    commits_tab_counter_element = soup.select('.opened-by')
    for i in range(0, len(commits_tab_counter_element)):
        print(commits_tab_counter_element[i].text.split("opened")[0].split("\n")[1].split("#")[1])

    # if commits_tab_counter_element:
    #     return commits_tab_counter_element.text.strip()
    # else:
    #     return None

if __name__ == "__main__":
    # Replace 'YOUR_PROXY_URL' with the actual proxy URL you want to use
    proxy_url = 'http://127.0.0.1:10809'  # Example: 'http://123.456.789.10:8080'
    proxies = {
        'http': proxy_url,
        'https': proxy_url
    }

    # url = "https://github.com/Rust-for-Linux/linux/pull/1009/commits"
    url = "https://github.com/Rust-for-Linux/linux/pulls"

    for i in range(1, 6):
        print(url.format(i), i)
        commits_tab_counter = find_commits_tab_counter(url.format(i), i, proxies=proxies)
    if commits_tab_counter:
        print(f"Number of commits: {commits_tab_counter}")
    else:
        print("Commits tab counter not found.")

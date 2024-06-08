import requests
from bs4 import BeautifulSoup

def find_commits_tab_counter(url, proxies=None):
    # Make an HTTP GET request to the URL using the provided proxies (if any)
    response = requests.get(url, proxies=proxies)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return

    # Parse the HTML content using BeautifulSoup
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element with the ID 'commits_tab_counter'
    commits_tab_counter_element = soup.find(id="diffstat")
    print(commits_tab_counter_element.text.strip())

    if commits_tab_counter_element:
        return commits_tab_counter_element.text.strip()
    else:
        return None

if __name__ == "__main__":
    # Replace 'YOUR_PROXY_URL' with the actual proxy URL you want to use
    proxy_url = 'http://127.0.0.1:10809'  # Example: 'http://123.456.789.10:8080'
    proxies = {
        'http': proxy_url,
        'https': proxy_url
    }
    
    # commits = [1025,1021,1019,1018,1014,1009,1007,997,995,994,990,982,977,969,967,966,964,963,958,956,955,954,952,950,946,938,937,935,933,932,925,923,921,920,919,914,913,911,910,909,906,904,903,901,900,898,893,888,886,885,884,880,877,876,875,873,866,864,863,861,857,856,854,851,841,840,824,817,816,815,808,807,803,801,779,768,764,753,751,747,729,728,726,701,700,682,645,643,582,578,563,554,548,484,478,476,472,459,457,450,448,443,439,430,423,409,374,368,300,282,278,269,264,258,143,109,]
    commits = [1025,1021,1019,1018,1014,1009,1007,997,990,982,977,969,966,964,963,958,956,955,954,952,950,946,938,937,935,933,932,925,923,920,919,914,913,911,910,906,904,903,901,900,898,893,888,886,885,884,880,877,876,875,873,866,864,863,861,857,856,854,851,841,840,824,817,816,815,808,807,803,801,779,768,764,753,751,747,729,728,726,701,700,682,643,582,578,563,554,548,484,478,476,472,459,457,450,448,443,439,430,423,409,374,368,300,282,278,269,264,258,143,109,]
    numebrs = []
    for commit in commits:
        url = "https://github.com/Rust-for-Linux/linux/pull/{}/partials/tabs".format(commit)
        commits_tab_counter = find_commits_tab_counter(url, proxies=proxies)
        if commits_tab_counter:
            print(f"Number of commits: {commits_tab_counter}")
            numebrs.append(commits_tab_counter)
        else:
            print("Commits tab counter not found.")
    print(numebrs)
    

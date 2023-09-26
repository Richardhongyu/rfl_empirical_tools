import requests
from bs4 import BeautifulSoup

def crawl_lwn_search_page(search_query, offset=0):
    base_url = 'https://lwn.net/Search/DoTextSearch'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # Fill in the 'Content-Length' header based on the actual length of the form data
        'Content-Length': '156',
        'Cookie': 'LWNSession1="qoz0QBeIL87HGs0c_MXLmg"; sub_nag="Support LWN.net"',
        'Host': 'lwn.net',
        'Origin': 'https://lwn.net',
        'Referer': 'https://lwn.net/Search/DoTextSearch',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows'
    }
    form_data = {
        'query': search_query,
        'ctypes': '11,8,3,12,1,2,50',
        'cats': '79,271,56,25,21,1,8,2,84,72,3',
        'relevance': '0',
        'offset': offset,
        'more': 'See more results'
    }

    try:
        response = requests.post(base_url, headers=headers, data=form_data)
        if response.status_code == 200:
            # Process the response content to extract relevant data about Rust-for-Linux
            data = response.content
            # Your code to extract specific data about Rust-for-Linux from the response goes here
            extract_data_from_search_results(data)
            # p_elements, blockquote_elements = extract_data_from_search_results(data)
            # for p_element, blockquote_element in zip(p_elements, blockquote_elements):
            #     print("P block:")
            #     print(p_element)
            #     print("Blockquote:")
            #     print(blockquote_element)
            #     print("-" * 50)
        else:
            print(f"Failed to retrieve search results for '{search_query}'")
    except requests.RequestException as e:
        print(f"Error during the request: {e}")

p_blocks = []
p_herfs = []
p_titles = []
blockquote_blocks = []

right_titles = ["Rust for embedded","Three Questions and Answers: Rust for Linux (Heise)","The rest of the 6.3 merge window","Kernel time APIs for Rust","Rust Keyword Generics Progress Report: February 2023","Rust bandwagon","KernelCI now testing Linux Rust code (Collabora blog)","To all the \"why bother\" rustaceans","Rust support coming to GCC","Memory Safe Languages in Android 13 (Google security blog)","Lina: Tales of the M1 GPU","Rust in the 6.2 kernel","Rust 1.65.0 released","A first look at Rust in the 6.1 kernel","Compiling Rust for Linux with rustc_codegen_gcc","A deeper look into the GCC Rust front-end","The first half of the 6.1 merge window","Some 6.0 development statistics","Compiling Rust with GCC: an update","Safer flexible arrays for the kernel","Next steps for Rust in the kernel","The 2022 Linux Kernel Maintainers Summit","A pair of Rust kernel modules","Rust 1.62.0 released","The Linux Foundation's \"security mobilization plan\"","Huang: Rust: A Critical Retrospective","Rust 1.61.0 released","Supporting Linux kernel development in Rust","Rustaceans at the border","The kernel radar: folios, multi-generational LRU, and Rust","Moving the kernel to modern C","Rust","Recommendations for Rust and read-copy-update","Rust and GCC, two different ways","McKenney: So You Want to Rust the Linux Kernel?","More Rust concepts for the kernel","The Rust for Linux project","Using Rust for kernel development","Key Rust concepts for the kernel","Rust for Linux redux","A GPIO driver in Rust","Rust noise","Supporting Miguel Ojeda’s Work on Rust in the Linux Kernel (Prossimo blog)","Rustls: memory safety for TLS","Rust in the Linux kernel (Google security blog)","Rust heads into the kernel?","Rust support hits linux-next","Rust is the future of systems programming, C is the new Assembly (Packt)","tl;dr: Rust is NFG. Try again in 2030.","C, still?","Grover: Why Rust for Low-level Linux programming?"]
right_blockquote_blocks = []
right_links = []

def save_blocks_to_file(blocks, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for block in blocks:
            # print(block)
            file.write(block+'\n')

def save_right_blocks_to_file(blocks, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for block in blocks:
            # print(block)
            file.write(block+'\n')
            file.write("------------------------\n")

def find_anchor_tags_in_p_blocks(soup):
    p_blocks = soup.find_all_next('p')[:25]
    anchor_tags = []

    for p in p_blocks:
        for a in p.find_all('a', href=True):
            anchor_tags.append(a['href'])

    return anchor_tags

def find_title_tags_in_p_blocks(soup):
    p_blocks = soup.find_all_next('p')[:25]
    anchor_tags = []

    for p in p_blocks:
        for a in p.find_all('a'):
            anchor_tags.append(a.text)

    return anchor_tags

def extract_data_from_search_results(content):
    # Use BeautifulSoup to parse the HTML content and extract relevant data
    soup = BeautifulSoup(content, 'html5lib')
    fix_soup = soup.prettify()

    # soup = BeautifulSoup(html, 'html.parser')

    article_content = soup.find('div', class_='ArticleText')

    if article_content:
        h4_element = article_content.find('h4', text='Search results')
        if h4_element:
            # Find all <p> elements after the <h4> element
            p_elements = h4_element.find_all_next('p')[:25]
            print(len(p_elements))

            # Find all <blockquote> elements after the <h4> element
            blockquote_elements = h4_element.find_all_next('blockquote')
            print(len(blockquote_elements))

            # Find all <a> elements after the <h4> element
            p_herfs_elements = find_anchor_tags_in_p_blocks(h4_element)
            print(len(p_herfs_elements))

            # Find all <br> elements after the <h4> element
            p_titles_elements = find_title_tags_in_p_blocks(h4_element)
            print(len(p_titles_elements))
            
            # Process and store the <p> and <blockquote> blocks
            p_blocks.extend([p.get_text(strip=True) for p in p_elements])
            blockquote_blocks.extend([blockquote.get_text(strip=True) for blockquote in blockquote_elements])
            p_herfs.extend([herf for herf in p_herfs_elements])
            p_titles.extend([title for title in p_titles_elements])
            for i,title in enumerate(p_titles_elements):
                if title in right_titles:
                    print(i, title, blockquote_blocks[-len(blockquote_elements):][i])
                    right_blockquote_blocks.append(blockquote_blocks[-len(blockquote_elements):][i])
                    right_links.append(p_herfs_elements[i])
            # print(len(right_blockquote_blocks))

def main():
    search_query = 'rust for linux'  # Replace with the actual search query you want to use
    # Set the offset to 0 to start from the beginning or adjust it for pagination
    offset = 0
    for offset in range(0, 1000, 25):  # Will iterate from 0 to 300 with step size of 25 /301
        print("-----------------------------------")
        crawl_lwn_search_page(search_query, offset)

    # Save <p> blocks to a file
    save_blocks_to_file(p_blocks, 'p_blocks.txt')
    print(f"Saved {len(p_blocks)} <p> blocks to 'p_blocks.txt'.")

    # Save <p> <a> blocks to a file
    save_blocks_to_file(p_herfs, 'p_herfs.txt')
    print(f"Saved {len(p_herfs)} <a> blocks to 'p_herfs.txt'.")

    # Save <p> <br> blocks to a file
    save_blocks_to_file(p_titles, 'p_titles.txt')
    print(f"Saved {len(p_titles)} <br> blocks to 'p_titles.txt'.")

    # Save <blockquote> blocks to a file
    save_blocks_to_file(blockquote_blocks, 'blockquote_blocks.txt')
    print(f"Saved {len(blockquote_blocks)} <blockquote> blocks to 'blockquote_blocks.txt'.")

    # Save right <blockquote> blocks to a file
    save_right_blocks_to_file(right_blockquote_blocks, 'right_blockquote_blocks.txt')
    print(f"Saved {len(right_blockquote_blocks)} <blockquote> blocks to 'right_blockquote_blocks.txt'.")

    # Save right <herf> blocks to a file
    save_blocks_to_file(right_links, 'right_p_herfs.txt')
    print(f"Saved {len(right_links)} <blockquote> blocks to 'right_p_herfs.txt'.")

if __name__ == '__main__':
    main()

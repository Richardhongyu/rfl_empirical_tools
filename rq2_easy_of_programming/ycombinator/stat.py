import os
import re
from bs4 import BeautifulSoup

def parse_html_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    span_tags = soup.find_all('span', class_='commtext c00')

    extracted_text = []
    for tag in span_tags:
        extracted_text.append( tag.text.strip())

    with open(output_file, 'w', encoding='utf-8') as f:
        for i in extracted_text: 
            f.write(i)
            f.write("\n------------------------\n")

if __name__ == "__main__":
    # Regular expression pattern to match filenames like "itemX.html"
    filename_pattern = re.compile(r'item\?id=(\d+)')

    for filename in os.listdir('.'):
        match = filename_pattern.match(filename)
        if match:
            item_number = int(match.group(1))
            input_file = filename
            output_file = f"output_item_{item_number}.txt"
            parse_html_file(input_file, output_file)

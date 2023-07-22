from collections import OrderedDict

def remove_duplicate_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Use an OrderedDict to store unique lines in the order of appearance
    unique_lines = OrderedDict()

    # Remove duplicate lines while preserving order
    for line in lines:
        line = line.strip()
        if line not in unique_lines:
            unique_lines[line] = None

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(unique_lines.keys()))

if __name__ == "__main__":
    input_file_path = "new_p_titles.txt"   # Replace with the path to your input file
    output_file_path = "pure_titles.txt" # Replace with the path for the output file

    remove_duplicate_lines(input_file_path, output_file_path)

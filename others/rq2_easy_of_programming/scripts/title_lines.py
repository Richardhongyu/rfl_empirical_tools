def remove_empty_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

if __name__ == "__main__":
    input_file_path = "p_titles.txt"   # Replace with the path to your input file
    output_file_path = "new_p_titles.txt" # Replace with the path for the output file

    remove_empty_lines(input_file_path, output_file_path)

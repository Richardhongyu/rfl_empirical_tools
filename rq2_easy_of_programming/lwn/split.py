import sys

# Function to redirect print output to a file
def redirect_print_to_file(file_path):
    original_stdout = sys.stdout  # Save a reference to the original stdout stream
    with open(file_path, 'w', encoding='utf-8') as f:
        sys.stdout = f
        # Now all print statements will be written to the file
        try:
            # Your original Python script code here
            file_name = "right_blockquote_blocks.txt"  # Replace this with the actual file path
            text_blocks_list = read_file_and_split(file_name)
            for i, block in enumerate(text_blocks_list, start=1):
                print(f"Text {i}:")
                print(block)
                print("-------------------------------")
        finally:
            sys.stdout = original_stdout  # Restore the original stdout stream

def read_file_and_split(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        text_blocks = text.split("------------------------\n")
        # Remove any leading/trailing whitespaces from each text block
        text_blocks = [block.strip() for block in text_blocks if block.strip()]
    return text_blocks

if __name__ == "__main__":
    output_file = "output.txt"  # Replace with your desired output file path
    redirect_print_to_file(output_file)



# if __name__ == "__main__":
#     output_file = "output.txt"  # Replace with your desired output file path
#     redirect_print_to_file(output_file)
#     print("This is a sample print statement.")
#     print("You can redirect this output to a file.")
#     # file_name = "right_blockquote_blocks.txt"  # Replace this with the actual file path
#     # text_blocks_list = read_file_and_split(file_name)
#     # for i, block in enumerate(text_blocks_list, start=1):
#     #     print("Text {i}:")
#     #     print(block)
#     #     print("-------------------------------")
#     restore_print()

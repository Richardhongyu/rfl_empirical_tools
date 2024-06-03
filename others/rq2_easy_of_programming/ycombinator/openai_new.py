import openai
import sys
import re
import os

# openai.api_base = 'https://api.closeai-asia.com/v1'
# openai.api_key = 'sk-3jRQB664OYefMLU64RpBbq6QckeIitL7UQQTZdYiSkK48zOA'

def read_file_and_split(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        text_blocks = text.split("------------------------\n")
        # Remove any leading/trailing whitespaces from each text block
        text_blocks = [block.strip() for block in text_blocks if block.strip() and "content" in block ]
    return text_blocks

# Function to redirect print output to a file
def redirect_print_to_file(file_path, file_name, end_name):
    original_stdout = sys.stdout  # Save a reference to the original stdout stream
    with open(file_path+file_name+end_name, 'w', encoding='utf-8') as f:
        sys.stdout = f
        # Now all print statements will be written to the file
        try:
            # Your original Python script code here
            # file_name = "output_item_31848499.txt"  # Replace this with the actual file path
            file_name = "ycombinator_comments_output_item_" + file_name + end_name
            # print(file_name)
            text_blocks_list = read_file_and_split(file_name)
            # print(text_blocks_list)
            for i, block in enumerate(text_blocks_list, start=1):
                print(f"Text {i}:")
                print(block)

                # response = openai.ChatCompletion.create(
                #   model="gpt-3.5-turbo",
                #   messages=[
                #     {"role": "system", "content": '''
                #       Summarize opinions in the following paragraph about rust. Just about rust, not anything else. The defination of "opinions" is the how the writter feels about the Rust. 
                #       If there is no opinions about rust, just give the answer No. It's all the answer you need give me. Just a "No".
                #       If there is opinions about rust. Answer Yes. Then judge whether the opinion is positive, general, or negative. Meanwhile, summarize the opinions and reasons. 
                #       Don't explain the reason why you make the decision. The format is important. The output must be in the following format.
                #       Here are some examles answers.
                #       Example1: 
                #       "No".
                #       Example2: 
                #       "Yes 
                #       General
                #       opinions:
                #         positive:
                #           1. rust is safe.
                #           2. rust is efficient.
                #         negative:
                #           1. rust is hard to learn.
                #           2. rust can not eliminate all the memory errors.
                #       " .
                #       Example3: 
                #       "Yes
                #       Positive
                #       opinions:
                #         positive:
                #           1. rust is safe.
                #           2. rust is efficient.
                #       " .z
                #       Example4: 
                #       "Yes
                #       Negative
                #       opinions:
                #         negative:
                #           1. rust is hard to learn.
                #           2. rust can not eliminate all the memory errors.
                #       " .
                #       I will give you the information in the next paragraph.'''},
                #     {"role": "user", "content": "{}".format(block)},
                #   ]
                # )
                # # print("the output is {}".format(block))
                # print(response)
                print("-------------------------------")
        finally:
            sys.stdout = original_stdout  # Restore the original stdout stream
            
if __name__ == '__main__':
  # output_file = "ycombinator_comments_output_item_31848499.txt"  # Replace with your desired output file path
  # redirect_print_to_file(output_file)

      # Regular expression pattern to match filenames like "itemX.html"
  filename_pattern = re.compile(r'item\?id=(\d+)')

  for filename in os.listdir('.'):
      match = filename_pattern.match(filename)
      if match:
          item_number = int(match.group(1))
          # print("ycombinator_comments_output_item_"+str(item_number)+".txt")
          redirect_print_to_file("stat_ycombinator_comments_output_item_", str(item_number), ".txt")
          # input_file = filename
          # output_file = f"output_item_{item_number}.txt"
          # parse_html_file(input_file, output_file)




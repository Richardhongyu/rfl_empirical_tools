import openai
openai.api_base = 'https://api.closeai-asia.com/v1'
openai.api_key = 'sk-3jRQB664OYefMLU64RpBbq6QckeIitL7UQQTZdYiSkK48zOA'

if __name__ == '__main__':

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": '''
        Summarize opinions in the following paragraph about rust. Just about rust, not anything else. The defination of "opinions" is the how the writter feels about the Rust. 
        If there is no opinions about rust, just give the answer No. It's all the answer you need give me. Just a "No".
        If there is opinions about rust. Answer Yes. Then judge whether the opinion is positive, general, or negative. Meanwhile, summarize the opinions and reasons. 
        Don't explain the reason why you make the decision. The format is important. The output must be in the following format.
        Here are some examles answers.
        Example1: 
        "No".
        Example2: 
        "Yes 
        General
        opinions:
          positive:
            1. rust is safe.
            2. rust is efficient.
          negative:
            1. rust is hard to learn.
            2. rust can not eliminate all the memory errors.
        " .
        Example3: 
        "Yes
        Positive
        opinions:
          positive:
            1. rust is safe.
            2. rust is efficient.
        " .z
        Example4: 
        "Yes
        Negative
        opinions:
          negative:
            1. rust is hard to learn.
            2. rust can not eliminate all the memory errors.
        " .
        I will give you the information in the next paragraph.'''},
      {"role": "user", "content": "Instead, Bottomley suggested that, rather than bringing in Rust, it might be better to just move more Rust-like features into C. Ojeda said that he has actually been working with the C language committee to push for that to happen, but any such change will take a long time if it happens at all. Christoph Hellwig said that this sort of change will have to happen anyway unless the plan is to rewrite the whole kernel in Rust; he was not pleased at the idea of rewriting working code in a new language. Perhaps the sparse static analyzer could be enhanced to do more Rust-like checking, he said. Ojeda answered that the result of such efforts would be like having Rust — but much later."},
    ]
  )

  print(response)
import openai
openai.api_base = 'https://api.closeai-asia.com/v1'
openai.api_key = 'sk-3jRQB664OYefMLU64RpBbq6QckeIitL7UQQTZdYiSkK48zOA'

if __name__ == '__main__':

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": '''You are a Linux expert.'''},
      {"role": "user", "content": "write me a python script to count the memory related bugs, like use-after-free, double free, from the git log in the different Linux drivers. Use git blame."},
    ]
  )

  print(response)
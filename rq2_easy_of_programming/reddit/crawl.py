import praw
from requests import Session

# Replace these with your credentials
CLIENT_ID = 'Richard_1999_lhy'
CLIENT_SECRET = '!@ChVFMj3rVGgJJ'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'  # Provide a descriptive user agent

def crawl_reddit_comments(subreddit_name, submission_id):
    s = Session()
    proxies =  { 'https': 'http://127.0.0.1:10809'}
    s.proxies.update(proxies)
    # praw.ini holds praw_bot_name oauth details
    # bot = praw.Reddit(praw_bot_name, requestor_kwargs={'session': s})
        
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT, requestor_kwargs={'session': s})
    print(reddit.auth.url(scopes=["identity"], state="...", duration="permanent"))
    print("test")

    try:
        subreddit = reddit.subreddit(subreddit_name)
        submission = reddit.submission(id=submission_id)
        
        submission.comments.replace_more(limit=None)  # Retrieve all comments
        for comment in submission.comments.list():
            print(f"Author: {comment.author}, Comment: {comment.body}")
    except praw.exceptions.PRAWException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    subreddit_name = 'rust'  # Replace with the subreddit name you want to crawl
    submission_id = 'xvorsd'  # Replace with the submission ID you want to crawl
    crawl_reddit_comments(subreddit_name, submission_id)

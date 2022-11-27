import praw
import time

reddit = praw.Reddit('bot', user_agent='cs40')

subreddit = reddit.subreddit("politics").top(limit=210)
count = 0
for submission in subreddit:
    count += 1
    print("title=", submission.title, count)
    reddit.subreddit("cs40_2022fall").submit(title=submission.title, url=submission.url)
    time.sleep(10)
import praw
from textblob import TextBlob

reddit = praw.Reddit('bot', user_agent='cs40')

subreddit = reddit.subreddit("cs40_2022fall").top(limit=None)

downvote_candidate = "trump"
comments_downvoted = 0
submissions_downvoted = 0
comments_upvoted = 0
submissions_upvoted = 0

for submission in subreddit:
    if downvote_candidate in submission.title.lower():
        content=TextBlob(str(submission.title))
        if content.sentiment.polarity>=0.5:
            submission.downvote()
            submissions_downvoted += 1
            print('downvotedsubmission:', submission.title, submissions_downvoted)
        else:
            if content.sentiment.polarity<0.5:
                submission.upvote()
                submissions_upvoted += 1
                print('upvotedsubmission:', submission.title, submissions_upvoted)
    submission.comments.replace_more(limit=None)

'''
    for comment in submission.comments.list():
        text = TextBlob(str(comment.body))
        if downvote_candidate in comment.body.lower() and text.sentiment.polarity>=0.5:
            comment.downvote()
            comments_downvoted += 1
            print('downvotedcomment:', comment.body, comments_downvoted)
        else:
            if downvote_candidate in comment.body.lower() and text.sentiment.polarity<0.5:
                comment.upvote()
                comments_upvoted += 1
                print('upvotedcomment:', comment.body, comments_upvoted)
    print('totalvotes=', submissions_downvoted + submissions_upvoted + comments_upvoted + comments_downvoted)
'''
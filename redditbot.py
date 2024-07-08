import praw

username = 'Your username here'
password = 'Your password here'
client_id = 'Your client id here'
secret = 'Your secret key here'

reddit_instance = praw.Reddit(
    client_id=client_id,
    client_secret=secret,
    username=username,
    password=password,
    user_agent="test_bot"
)

subreddit = reddit_instance.subreddit("showerthoughts")
top_25_submissions = subreddit.hot(limit=25)
for submission in top_25_submissions:
    print(submission.title, "\n")

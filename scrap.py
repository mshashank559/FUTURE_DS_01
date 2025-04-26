import praw
import pandas as pd

# Reddit API credentials
reddit = praw.Reddit(
    client_id="IU4Lty7NeCfwQNcY5NVwig",
    client_secret="xoTZjb0vNTUUJ6rVpH_fRzayxmTBbA",
    user_agent="trend_analysis"
)

# List of trending-related subreddits
subreddits = ["popular", "trendingsubreddits", "fitness", "news", "health", "technology"]

posts = []

for sub in subreddits:
    for post in reddit.subreddit(sub).hot(limit=100):
        posts.append([
            sub,
            post.title,
            post.selftext,
            post.score,
            post.num_comments
        ])

# Save to CSV
df = pd.DataFrame(posts, columns=["Subreddit", "Title", "Text", "Upvotes", "Comments"])
df.to_csv("Data/reddit_trending_posts.csv", index=False)

print("✅ Reddit scraping complete. File saved at: Data/reddit_trending_posts.csv")

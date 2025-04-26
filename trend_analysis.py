# social_fitness_trend_analysis.py

import praw
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from textblob import TextBlob
from datetime import datetime, timedelta
import random

# Create data folder if not exists
os.makedirs("Data", exist_ok=True)

#########################################
# 1. Scrape Reddit using PRAW
#########################################
print("🔄 Scraping Reddit...")

reddit = praw.Reddit(
    client_id="IU4Lty7NeCfwQNcY5NVwig",
    client_secret="xoTZjb0vNTUUJ6rVpH_fRzayxmTBbA",
    user_agent="my fitness scraper"
)

reddit_posts = []
for post in reddit.subreddit("fitness").hot(limit=300):
    reddit_posts.append([post.created_utc, post.title + " " + post.selftext, post.author.name, "Reddit"])

df_reddit = pd.DataFrame(reddit_posts, columns=["Date", "Text", "Username", "source"])
df_reddit["Date"] = pd.to_datetime(df_reddit["Date"], unit="s")

print(f"✅ Reddit: {len(df_reddit)} posts scraped.")

#########################################
# 2. Simulate Instagram & Facebook
#########################################

print("📸 Simulating Instagram & Facebook...")

messages = [
    "Just completed a killer leg workout! #fitnessgoals",
    "Healthy body, healthy mind. #wellness",
    "Morning yoga is my daily therapy 🧘‍♀️",
    "Hit a new PR today! Feeling strong 💪",
    "Protein shake + cardio = 🔥 #grindmode",
    "My gym routine is finally paying off 😤",
    "Trying out a vegan meal plan 🍃",
    "Track your progress. Stay motivated!",
    "Rest days are important too 😴",
    "Workout done. Time for gains!"
]

def simulate_social_data(platform, n):
    data = []
    for _ in range(n):
        date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 364))
        text = random.choice(messages)
        username = f"{platform.lower()}_user_{random.randint(1000, 9999)}"
        data.append([date, text, username, platform])
    return pd.DataFrame(data, columns=["Date", "Text", "Username", "source"])

df_insta = simulate_social_data("Instagram", 150)
df_fb = simulate_social_data("Facebook", 150)

print("✅ Simulation complete.")

#########################################
# 3. Combine & Clean
#########################################

print("📊 Combining all platforms...")

df_all = pd.concat([df_reddit, df_insta, df_fb], ignore_index=True)
df_all["cleaned_text"] = df_all["Text"].apply(lambda x: str(x).lower())

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    return 'Neutral'

df_all["Sentiment"] = df_all["cleaned_text"].apply(get_sentiment)

# Save intermediate dataset
df_all.to_csv("Data/processed_social_media.csv", index=False)

#########################################
# 4. Plot Sentiment & Word Cloud
#########################################

platforms = df_all["source"].unique()
print("📈 Generating plots and word clouds...")

for platform in platforms:
    subset = df_all[df_all["source"] == platform]

    # Sentiment Distribution Plot
    plt.figure(figsize=(6, 4))
    sns.countplot(data=subset, x="Sentiment", palette="pastel")
    plt.title(f"Sentiment Distribution - {platform}")
    plt.xlabel("Sentiment")
    plt.ylabel("Posts")
    plt.tight_layout()
    plt.savefig(f"Data/sentiment_{platform}.png")
    plt.show()

    # Word Cloud
    text = " ".join(subset["cleaned_text"])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"Word Cloud - {platform}")
    plt.savefig(f"Data/wordcloud_{platform}.png")
    plt.show()

#########################################
# 5. Save Final Dataset
#########################################
df_all.to_csv("Data/processed_social_media_final.csv", index=False)
print("✅ All done! Final file: Data/processed_social_media_final.csv")
reddit_df = pd.read_csv("Data/reddit_trending_posts.csv")
insta_df = pd.read_csv("Data/processed_social_media.csv")  # Assuming this includes Insta/Facebook
sentiment_df = pd.read_csv("Data/sentimentdataset.csv")

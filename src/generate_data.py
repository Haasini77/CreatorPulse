import pandas as pd
import random
from datetime import datetime, timedelta

platforms = ["Instagram", "YouTube", "LinkedIn"]
content_types = ["Reel", "Image", "Carousel", "Short"]
topics = ["AI", "Coding", "Education", "Technology", "Career", "Fitness"]

data = []

start_date = datetime(2026, 1, 1)

for i in range(1, 1001):

    platform = random.choice(platforms)
    content_type = random.choice(content_types)
    topic = random.choice(topics)

    post_date = start_date + timedelta(days=random.randint(0, 270))
    post_hour = random.randint(6, 23)

    followers = random.randint(1000, 100000)

    views = int(followers * random.uniform(0.3, 3.0))

    likes = int(views * random.uniform(0.02, 0.12))
    comments = int(likes * random.uniform(0.02, 0.15))
    shares = int(likes * random.uniform(0.01, 0.10))
    saves = int(likes * random.uniform(0.01, 0.08))

    hashtag_count = random.randint(1, 15)

    data.append([
        i,
        platform,
        content_type,
        topic,
        post_date.strftime("%Y-%m-%d"),
        post_hour,
        followers,
        views,
        likes,
        comments,
        shares,
        saves,
        hashtag_count
    ])

columns = [
    "post_id",
    "platform",
    "content_type",
    "topic",
    "post_date",
    "post_hour",
    "followers",
    "views",
    "likes",
    "comments",
    "shares",
    "saves",
    "hashtag_count"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("data/social_media_data.csv", index=False)

print("Dataset created successfully!")
print("Total posts:", len(df))
print(df.head())
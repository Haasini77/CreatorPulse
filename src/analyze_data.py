import pandas as pd

# Load dataset
df = pd.read_csv("data/social_media_data.csv")

# Basic information
print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())
# Calculate Engagement Rate
df["engagement_rate"] = (
    (df["likes"] + df["comments"] + df["shares"] + df["saves"])
    / df["views"]
) * 100

print("\nEngagement Rate:")
print(df["engagement_rate"].head())

print("\nAverage Engagement Rate:")
print(df["engagement_rate"].mean())
# Platform-wise average engagement
platform_analysis = df.groupby("platform")["engagement_rate"].mean()

print("\nPlatform-wise Engagement Rate:")
print(platform_analysis)
# Content type-wise average engagement
content_analysis = df.groupby("content_type")["engagement_rate"].mean()

print("\nContent Type-wise Engagement Rate:")
print(content_analysis)
# Topic-wise average engagement
topic_analysis = df.groupby("topic")["engagement_rate"].mean()

print("\nTopic-wise Engagement Rate:")
print(topic_analysis)
# Hour-wise average engagement
hour_analysis = df.groupby("post_hour")["engagement_rate"].mean()

print("\nHour-wise Engagement Rate:")
print(hour_analysis)
# Top 5 posting hours
top_hours = hour_analysis.sort_values(ascending=False).head(5)

print("\nTop 5 Best Posting Hours:")
print(top_hours)
# Hashtag count-wise average engagement
hashtag_analysis = df.groupby("hashtag_count")["engagement_rate"].mean()

print("\nHashtag Count-wise Engagement Rate:")
print(hashtag_analysis)
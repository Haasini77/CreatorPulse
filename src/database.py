import sqlite3
import pandas as pd

df = pd.read_csv("data/social_media_data.csv")

df["engagement_rate"] = (
    (df["likes"] + df["comments"] + df["shares"] + df["saves"])
    / df["views"]
) * 100

connection = sqlite3.connect("data/creatorpulse.db")

df.to_sql(
    "social_media_posts",
    connection,
    if_exists="replace",
    index=False
)

print("Database created successfully!")

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM social_media_posts")

count = cursor.fetchone()[0]

print("Total records in database:", count)
# SQL query: average engagement by platform
query = """
SELECT platform, AVG(engagement_rate) AS average_engagement
FROM social_media_posts
GROUP BY platform
ORDER BY average_engagement DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nSQL Platform Analysis:")
print(result)
# SQL query: average engagement by content type
query = """
SELECT content_type, AVG(engagement_rate) AS average_engagement
FROM social_media_posts
GROUP BY content_type
ORDER BY average_engagement DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nSQL Content Type Analysis:")
print(result)
# SQL query: average engagement by topic
query = """
SELECT topic, AVG(engagement_rate) AS average_engagement
FROM social_media_posts
GROUP BY topic
ORDER BY average_engagement DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nSQL Topic Analysis:")
print(result)
connection.close()
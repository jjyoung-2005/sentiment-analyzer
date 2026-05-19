import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sqlite3

conn = sqlite3.connect('emotions.db')
df = pd.read_sql("SELECT * FROM posts", conn)
analyzer = SentimentIntensityAnalyzer()

df['compound'] = df['text'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

def get_sentiment_score(compound):
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return  "Negative"
    else:
        return  "Neutral"

df['sentiment'] = df['compound'].apply(get_sentiment_score)

df.to_sql("scored_posts", conn, if_exists="replace", index=False)
conn.close()

print("Count:", df['sentiment'].value_counts())
print("Average Compound Score:", df.groupby('emotion')['compound'].mean())

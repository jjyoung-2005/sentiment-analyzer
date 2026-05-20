import pandas as pd
import json
import sqlite3



conn = sqlite3.connect('emotions.db')
df = pd.read_sql("SELECT * FROM scored_posts", conn)

emotion_dict = {}

avg_by_emotion = df.groupby('emotion')['compound'].mean().to_dict()

count_for_sentiment = df['sentiment'].value_counts().to_dict()

with open('summary.json', 'w') as f:
    json.dump(emotion_dict, f)

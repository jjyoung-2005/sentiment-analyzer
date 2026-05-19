from collections import Counter
import pandas as pd
import sqlite3
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import re

conn = sqlite3.connect('emotions.db')
df = pd.read_sql("SELECT * FROM scored_posts", conn)

for emotion in df['emotion'].unique():
    emo_filter = df[df['emotion'] == emotion]

emote_str = emo_filter['text'].str.cat(sep=' ')
emote_str = re.sub(r'[^a-zA-Z\s]', '', emote_str).lower()
custom_stops = {"feel", "feeling", "like", "im", "really", "get", "know", "make", "would", "time"}

stop_words = set(stopwords.words('english')).union(custom_stops)

words = [w for w in emote_str.split() if w.lower() not in stop_words]

count = Counter(words)
count.most_common(10)

print(emotion, count.most_common(10))

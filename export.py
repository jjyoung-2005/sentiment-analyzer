import pandas as pd
import sqlite3

conn = sqlite3.connect('emotions.db')
df = pd.read_sql("SELECT * FROM scored_posts", conn)
df.to_csv('sentiment_data.csv', index=False)
conn.close()
print("Exported")

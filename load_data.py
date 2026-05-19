from datasets import load_dataset
import pandas as pd
import sqlite3

ds = load_dataset("dair-ai/emotion")
df = ds["train"].to_pandas()

labels = {0: "sadness", 1: "joy", 2: "love", 3: "anger", 4: "fear", 5: "surprise"}
df["emotion"] = df["label"].map(labels)

print(df.head(10))

conn = sqlite3.connect("emotions.db")
df.to_sql("posts", conn, if_exists="replace", index=False)
conn.close()

print("\nSaved to emotions.db")

import sqlite3
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt


conn = sqlite3.connect('emotions.db')
df = pd.read_sql("SELECT * FROM scored_posts", conn)

emotion_map = {
    'joy' : "positive",
    'sadness' : 'negative',
    'anger' : 'negative',
    'fear' : 'negative',
    'disgust' : 'negative',
    'surprise':'neutral',
    'love':'positive',
    'excitement' : 'positive',
    'neutral' : 'neutral',
    'happiness' : 'positive',
    'boredom' : 'neutral',
    'frustration' : 'negative',
    'anxiety' : 'negative',
    'contentment' : 'positive',
    'guilt' : 'negative',
    'shame' : 'negative',
    'pride' : 'positive',
    'envy' : 'negative',
}
labels = ["positive", "negative", "neutral"]

df['true_sentiment'] = df['emotion'].map(emotion_map)

conf_matrix = confusion_matrix(df['true_sentiment'], df['sentiment'], labels = labels)
display = ConfusionMatrixDisplay(conf_matrix)
display.plot()
plt.savefig('confusion_matrix.png')
plt.show()
print(df['true_sentiment'].value_counts())
print(df['sentiment'].value_counts())

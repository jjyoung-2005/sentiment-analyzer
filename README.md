# Emotion Classification and Sentiment Analyzer
#### An end-to-end analysis of sentiment across six human-labeled emotion categories using VADER, Python,, SQLite, and Tableau.

## Overview

   For this personal project, I used the "dair-ai" dataset from Hugging Face, which classifies Twitter/X posts into six emotional categories:

- sadness
- anger
- love
- surprise
- fear
- joy

Using VADER (Valence Aware Dictionary and sEntiment Reasoner) - a lexicon used for informal social media posts - I decided to evaluate its accuracy by comparing it with human classification scores. With this information, we can decide whether rule-based sentiment tools like VADER are reliable enough for real-world mental health and social media analysis.

My goal with this project is to explore how sentiment varies across emotion categories to see where VADER struggles to most and visualize findings through an interactive Tableau dashboard.

## Tools Used

- Python
- pandas
- VADER
- scikit-learn
- SQLite
- Tableau Public

## Key Findings
- VADER achieved 75% accuracy against human emotion labels, performing well on clearly positive and negative categories but struggling with nuanced emotions like fear and surprise.
- Joy and Love scored the highest VADER sentiment scores, with 0.51 and 0.46 respectively. This suggests VADER is most reliable when classifying clearly positive language.
- Fear and surprise produced average compound scores of -0.15 and 0.24 respectively, placing them near neutral. Notably, both showed the widest score distribution in the box plot, suggesting VADER is least consistent when classifying ambiguous emotions.
- Even within positively labeled emotions like joy and love, VADER produced compound scores as low as -0.98, highlighting its limitations with sarcasm, irony, and context-dependent language.


## Project Structure

`load_data.py` : Loads the dair-ai emotion dataset and stores it in SQLite.

`word_freq.py` : Calculates most frequent words per emotion category.

`vader.py` : Runs VADER sentiment analysis on each post and saves scores.

`confusion_matrix.py` : Compares VADER labels against human labels and plots results

`export.py`: Exports scored data to CSV for Tableau

`export_json.py` : Exports summary statistics to JSON.

## How to Run

- Run `pip install -r requirements.txt`, then run each `.py` file in order, as follows:

 1. `load_data.py`
 2. `vader.py`
 3. `word_freq.py`
 4. `confusion_matrix.py`
 5. `export.py`
 6. `export_json.py`

## Tableau Public Visualizations Dashboard

https://public.tableau.com/app/profile/josh.young8779/viz/EmotionSentimentAnalysis/Dashboard1?publish=yes

# Emotion Classification and Sentiment Analyzer

## Overview

For this personal project, I used the `dair-ai` dataset from Hugging Face, which classifies Twitter/X posts into six emotional categories:

- sadness
- anger
- love
- surprise
- fear
- joy

Using VADER (Valence Aware Dictionary and sEntiment Reasoner) - a lexicon used for informal social media posts - I decided to evaluate its accuracy by comparing it with human classification scores. With this imformation, we can decide whether rule-based sentiment tools like VADER are reliable enough for real-world mental health and social media analysis.

My goal with this project is to explore how sentiment varies across emotion categories to see where BADER struggles to most and visualize findings through an interactive Tableau dashboard.

## Tools Used

- Python
- pandas
- VADER
- scikit-learn
- SQLite
- Tableau Public

## Key Findings

## Project Structure

## How to Run

- Run `pip install -r requirements.txt`, then run each `.py` file in order, as follows:

 1. `load_data.py`
 2. `word_freq.py`
 3. `vader.py`
 4. `confusion_matrix.py`









https://public.tableau.com/app/profile/josh.young8779/viz/EmotionSentimentAnalysis/Dashboard1?publish=yes
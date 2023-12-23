# Cryptocurrency Sentiment Analysis

This Python script, `sentiment_analysis.py`, analyzes the sentiment of tweets about a specific cryptocurrency and correlates it with the price of the cryptocurrency. It uses the Natural Language Toolkit (NLTK) for sentiment analysis, the yfinance library to fetch cryptocurrency prices, and pandas for data manipulation. The results are displayed on a web page using Streamlit.

## Requirements

This script requires the following Python libraries:

- pandas
- nltk
- yfinance
- streamlit

You can install these libraries using pip:

```bash
pip install -r requirements.txt
```
### Usage

To run the script, use the following command:
```bash
streamlit run sentiment_analysis.py
```
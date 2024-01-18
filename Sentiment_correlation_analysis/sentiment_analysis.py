import pandas as pd
import nltk
import streamlit as st
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import logging
import os
def analize(sentence):
    result = SentimentIntensityAnalyzer().polarity_scores(sentence)
    return result['compound'], result['neg'], result['neu'], result['pos']

def process_csv_tweets(crypto):
    df = pd.read_csv('files/' + crypto + '_tweets.csv')
    df = df[pd.to_datetime(df['Date'], errors='coerce').notna()]
    sentences = df['Text'].astype(str)
    likes = df['Likes']
    retweets = df['Retweets']
    results = [analize(sentence) for sentence in sentences]
    results_df = pd.DataFrame(results, columns=['compound', 'negative', 'neutral', 'positive'])
    results_df['Date'] = pd.to_datetime(df['Date']).dt.date
    results_df['likes'] = likes
    results_df['retweets'] = retweets
    results_df = results_df.groupby('Date').mean().reset_index()
    results_df['compound'] = results_df['compound']
    results_df.to_csv('files/' + crypto + '_sentiment.csv')
    avg_compound = results_df['compound'].mean()
    if avg_compound > 0.05:
        logging.info("The overall sentiment of the tweets is positive. {0}".format(avg_compound))
    elif avg_compound < -0.05:
        logging.info("The overall sentiment of the tweets is negative. {0}".format(avg_compound))
    else:
        logging.info("The overall sentiment of the tweets is neutral. {0}".format(avg_compound))

def analyze_relation(crypto):
    sentiment_data = pd.read_csv('files/' + crypto + '_sentiment.csv', index_col='Date', parse_dates=True).map(lambda x: 1 if x > 0.25 else (-1 if x < -0.1 else 0))
    price_data = pd.read_csv('files/' + crypto + '_data.csv', index_col='Date', parse_dates=True)
    merged_data = pd.merge(sentiment_data, price_data, on='Date')
    merged_data.to_csv('files/' + crypto + '_merged.csv')
    if merged_data['compound'].std() != 0 and merged_data['Close'].std() != 0:
        correlation = merged_data['compound'].corr(merged_data['Close'])
        logging.info("The correlation between the sentiment scores and the prices is {0}".format(correlation))
        if(correlation > 0.5):
            logging.info("The correlation is strong.")
        elif(correlation > 0.3):
            logging.info("The correlation is moderate.")
        elif(correlation > 0.1):
            logging.info("The correlation is weak.")
        elif(correlation > -0.1):
            logging.info("The correlation is very weak.")
        elif(correlation > -0.3):
            logging.info("The correlation is weak.")
        elif(correlation > -0.5):
            logging.info("The correlation is moderate.")
    else:
        logging.info("The correlation is not defined.")

def show_on_webpage(crypto):
    data = pd.read_csv('files/' + crypto + '_data.csv', index_col='Date', parse_dates=True)
    min_date = data.index.min().date()
    max_date = data.index.max().date()
    start_date = datetime.strptime(str(st.sidebar.date_input('Start date', min_date, key=crypto+'start_date')), "%Y-%m-%d").date()
    end_date = datetime.strptime(str(st.sidebar.date_input('End date', max_date, key=crypto+'end_date')), "%Y-%m-%d").date()
    st.title("Cryptocurrency sentiment analysis")
    st.markdown("### " + crypto)
    st.markdown("#### Dates")
    st.markdown("Start date: " + str(start_date))
    st.markdown("End date: " + str(end_date))
    st.markdown("#### Sentiment")
    st.line_chart(pd.read_csv('files/' + crypto + '_sentiment.csv', index_col='Date', parse_dates=True)['compound'])
    st.markdown("#### Prices")
    st.line_chart(pd.read_csv('files/' + crypto + '_data.csv', index_col='Date', parse_dates=True)['Close'])
    st.markdown("#### Correlation")
    st.markdown("The correlation between the sentiment scores and the prices is " + "{:.3f}".format(pd.read_csv('files/' + crypto + '_merged.csv')['compound'].corr(pd.read_csv('files/' + crypto + '_merged.csv')['Close'])))

def execute(crypto):

    sentiment_file = 'files/' + crypto + '_sentiment.csv'
    merged_file = 'files/' + crypto + '_merged.csv'
    if not os.path.exists(sentiment_file):
        logging.info("Processing sentiment of " + crypto + "...")
        process_csv_tweets(crypto)
    if not os.path.exists(merged_file):
        logging.info("Processing correlation of " + crypto + "...")
        analyze_relation(crypto)
    show_on_webpage(crypto)

def main():
    logging.basicConfig(level=logging.INFO)
    nltk.download('vader_lexicon')
    execute("one")
    execute("xrp")

if __name__ == '__main__':
    main()
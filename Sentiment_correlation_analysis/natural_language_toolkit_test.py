import pandas as pd
import nltk
import yfinance as yf
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer

start_date = ""
end_date = ""
average_compound = 0.0

def analize(sentence):
    result = SentimentIntensityAnalyzer().polarity_scores(sentence)
    return result['compound'], result['neg'], result['neu'], result['pos']

def process_csv_tweets(crypto):
    df = pd.read_csv('in/' + crypto + '_tweets.csv')

    # Extract the first and last date and remove the time
    first_date = datetime.strptime(df['Date'].iloc[0], "%Y-%m-%d %H:%M:%S%z").date()
    last_date = datetime.strptime(df['Date'].iloc[-1], "%Y-%m-%d %H:%M:%S%z").date()
    print("First date: ", first_date)
    print("Last date: ", last_date)

    sentences = df['Text']
    likes = df['Likes']
    retweets = df['Retweets']

    results = [analize(sentence) for sentence in sentences]

    results_df = pd.DataFrame(results, columns=['compound', 'negative', 'neutral', 'positive'])
    results_df['Date'] = pd.to_datetime(df['Date']).dt.date
    results_df['likes'] = likes
    results_df['retweets'] = retweets
    results_df.to_csv('out/' + crypto + '_sentiment.csv')

    avg_compound = results_df['compound'].mean()

    if avg_compound > 0.05:
        print("The overall sentiment of the tweets is positive. {0}".format(avg_compound))
    elif avg_compound < -0.05:
        print("The overall sentiment of the tweets is negative. {0}".format(avg_compound))
    else:
        print("The overall sentiment of the tweets is neutral. {0}".format(avg_compound))

    return first_date, last_date, avg_compound

def process_csv_prices(crypto, start_date, end_date):
    start_datetime = datetime.combine(start_date, datetime.min.time())
    end_datetime = datetime.combine(end_date, datetime.min.time()) + pd.Timedelta(days=1)

    crypto_data = yf.download(crypto + "-USD", start=start_datetime, end=end_datetime)

    if not crypto_data.empty:
        data = crypto_data["Close"].dropna()
        data.to_csv("out/" + crypto + "_data.csv")
    else:
        print("No data available for {0} on {1}".format(crypto, start_date))

def analyze_relation(crypto):
    sentiment_data = pd.read_csv('out/' + crypto + '_sentiment.csv', index_col='Date', parse_dates=True)
    price_data = pd.read_csv('out/' + crypto + '_data.csv', index_col='Date', parse_dates=True)

    merged_data = pd.merge(sentiment_data, price_data, on='Date')
    merged_data.to_csv('out/' + crypto + '_merged.csv')

    if merged_data['compound'].std() != 0 and merged_data['Close'].std() != 0:
        correlation = merged_data['compound'].corr(merged_data['Close'])
        print("The correlation between the sentiment scores and the prices is {0}".format(correlation))
        if(correlation > 0.5):
            print("The correlation is strong.")
        elif(correlation > 0.3):
            print("The correlation is moderate.")
        elif(correlation > 0.1):
            print("The correlation is weak.")
        elif(correlation > -0.1):
            print("The correlation is very weak.")
        elif(correlation > -0.3):
            print("The correlation is weak.")
        elif(correlation > -0.5):
            print("The correlation is moderate.")
    else:
        print("The standard deviation of the sentiment scores or the prices is zero. The correlation is undefined.")



if __name__ == '__main__':
    nltk.download('vader_lexicon')
    #start_date, end_date, average_compound = process_csv_tweets("BTC")
    start_date = datetime.strptime("2017-07-13", "%Y-%m-%d").date()
    end_date = datetime.strptime("2017-07-31", "%Y-%m-%d").date()
    process_csv_prices("BTC", start_date, end_date)
    analyze_relation("BTC")
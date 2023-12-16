import datetime as date
from tweety import Twitter
import pandas as pd
import sqlite3
from constants.names import TWEETS_CSV_NAME, DATABASE_PATH, DATABASE_TABLE_NAME
from exceptions.database_exceptions import DatabaseConnectionError


class TweeterScraper:
    def __init__(self):
        try:
            self.connection = sqlite3.connect(DATABASE_PATH)
        except sqlite3.Error as e:
            raise DatabaseConnectionError(f"Error connecting to the database: {e}")

    async def save_tweets_to_database(self, tweets_to_save):
        tweets_to_save.to_sql(DATABASE_TABLE_NAME, self.connection, if_exists='replace', index=False)

    async def fetch_tweets_and_save_to_csv(self, keyword, until=None, since=None):
        app = Twitter("session")
        app.start()
        query = keyword
        if until:
            query += f" until:{until}"
        if since:
            query += f" since:{since}"
        all_tweets = app.search(query, pages=1, wait_time=2)
        tweets_to_add = []
        for tweet in all_tweets:
            tweet_data = {
                "Date": tweet.date,
                "Text": tweet.text,
                "Likes": tweet.likes,
                "Retweets": tweet.retweet_counts
            }
            tweets_to_add.append(tweet_data)
        tweets_to_save = pd.DataFrame(tweets_to_add)
        timestamp = date.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"csvs/{TWEETS_CSV_NAME}{keyword}_{timestamp}.csv"
        tweets_to_save.to_csv(filename, index=False)
        await self.save_tweets_to_database(tweets_to_save)

    async def get_data_from_database_and_convert_to_csv(self):
        query = f"SELECT * FROM {DATABASE_TABLE_NAME}"
        df = pd.read_sql_query(query, self.connection)
        if not df.empty:
            timestamp = date.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"csvs/{TWEETS_CSV_NAME}from_db_{timestamp}.csv"
            df.to_csv(filename, index=False)

    def close_connection(self):
        self.connection.close()
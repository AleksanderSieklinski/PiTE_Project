import datetime as date
import threading
import os
from tweety import Twitter
import pandas as pd
import sqlite3
import logging
from PiTE_Project.constants.names import TWEETS_CSV_NAME, DATABASE_PATH, DATABASE_TABLE_NAME, TWEETS_SEARCH_PAGES, \
    TWEETS_SEARCH_WAIT_TIME, TWITTER_SESSION, LOGGING_LEVEL
from PiTE_Project.exceptions.database_exceptions import DatabaseConnectionError


class TweeterScraper:
    def __init__(self):
        self.setup_logging()
        self.lock = threading.Lock()
        if not os.path.exists("databases"):
            os.makedirs("databases")
        try:
            self.connection = sqlite3.connect(DATABASE_PATH)
            self.logger.info(f"Connected to database")
        except sqlite3.Error as e:
            error_message = f"Error connectiong to database {type(e).__name__} - {str(e)}"
            self.logger.error(error_message)
            raise DatabaseConnectionError(error_message)

    def setup_logging(self):
        if not os.path.exists("logs"):
            os.makedirs("logs")
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(LOGGING_LEVEL)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        timestamp = date.date.today().strftime("%Y-%m-%d")
        file_handler = logging.FileHandler(f"logs/twitter_service_{timestamp}.log")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    async def save_tweets_to_database(self, tweets_to_save):
        self.logger.info(f"Saving data to database")
        with self.lock:
            tweets_to_save.to_sql(DATABASE_TABLE_NAME, self.connection, if_exists='append', index=False)

    async def save_tweets_to_csv_and_database(self, all_tweets, keyword):
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
        with self.lock:
            self.logger.info(f"Saving data to {filename} file")
            tweets_to_save.to_csv(filename, index=False)
        await self.save_tweets_to_database(tweets_to_save)

    async def search_user_tweets_and_save_to_csv(self, twitter_account):
        app = Twitter(TWITTER_SESSION)
        self.logger.info(f"Start searching for {twitter_account}")
        all_tweets = app.get_tweets(twitter_account, pages=TWEETS_SEARCH_PAGES, wait_time=TWEETS_SEARCH_WAIT_TIME)
        await self.save_tweets_to_csv_and_database(all_tweets, twitter_account)
        self.logger.info(f"Finished searching for {twitter_account}")

    async def search_keyword_tweets_and_save_to_csv(self, keyword, until=None, since=None):
        app = Twitter(TWITTER_SESSION)
        self.logger.info(f"Start searching for {keyword}")
        app.start()
        query = keyword
        if until:
            query += f" until:{until}"
        if since:
            query += f" since:{since}"
        all_tweets = app.search(query, pages=TWEETS_SEARCH_PAGES, wait_time=TWEETS_SEARCH_WAIT_TIME)
        await self.save_tweets_to_csv_and_database(all_tweets, keyword)
        self.logger.info(f"Finished searching for {keyword}")

    async def get_data_from_database_and_convert_to_csv(self):
        self.logger.info(f"Start get all data from database")
        query = f"SELECT * FROM {DATABASE_TABLE_NAME}"
        df = pd.read_sql_query(query, self.connection)
        if not df.empty:
            timestamp = date.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"csvs/{TWEETS_CSV_NAME}from_db_{timestamp}.csv"
            df.to_csv(filename, index=False)
        self.logger.info(f"Finished getting all data from database")

    def close_connection(self):
        self.logger.info(f"Database connection closed")
        self.connection.close()

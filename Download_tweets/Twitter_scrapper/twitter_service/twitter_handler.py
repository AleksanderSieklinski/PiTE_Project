import datetime as date
import threading
import time
import os
from tweety import Twitter
import pandas as pd
import sqlite3
import logging
from Download_tweets.Twitter_scrapper.constants.names import TWEETS_CSV_NAME, DATABASE_PATH, DATABASE_TABLE_NAME, TWEETS_SEARCH_PAGES, \
    TWEETS_SEARCH_WAIT_TIME, TWITTER_SESSION, LOGGING_LEVEL, DATE_CHUNK_DAYS
from Download_tweets.Twitter_scrapper.exceptions.database_exceptions import DatabaseConnectionError


class TweeterScraper:
    def __init__(self):
        self.cancel_search = False
        self.setup_logging()
        self.lock = threading.Lock()

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

    async def save_tweets_to_csv(self, all_tweets, keyword):
        if not os.path.exists("csvs"):
            os.makedirs("csvs")
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

    async def search_user_tweets_and_save_to_csv(self, twitter_account):
        app = Twitter(TWITTER_SESSION)
        self.logger.info(f"Start searching for {twitter_account}")
        all_tweets = app.get_tweets(twitter_account, pages=TWEETS_SEARCH_PAGES, wait_time=TWEETS_SEARCH_WAIT_TIME)
        await self.save_tweets_to_csv(all_tweets, twitter_account)
        self.logger.info(f"Finished searching for {twitter_account}")

    async def search_keyword_tweets_and_save_to_csv(self, keyword, until=None, since=None):
        app = Twitter(TWITTER_SESSION)
        self.logger.info(f"Start searching for {keyword}")
        app.start()
        query = keyword

        if until and since:
            until_date = date.datetime.strptime(until, '%Y-%m-%d')
            since_date = date.datetime.strptime(since, '%Y-%m-%d')
            delta = until_date - since_date

            if delta.days > DATE_CHUNK_DAYS:
                await self.search_tweets_in_chunks(app, query, since_date, until_date, keyword)
            else:
                await self.search_tweets(app, query, since, until, keyword)
        else:
            await self.search_tweets(app, query, since, until, keyword)

    async def search_tweets_in_chunks(self, app, query, since_date, until_date, keyword):
        chunk_size = date.timedelta(days=DATE_CHUNK_DAYS)
        num_chunks = (until_date - since_date).days // DATE_CHUNK_DAYS + 1
        self.logger.info(f"Date exceeded DATE_CHUNK_DAYS, divided into: {num_chunks} chunks")
        all_tweets = []

        for i in range(num_chunks):
            try:
                if self.cancel_search:
                    self.logger.info("Search canceled.")
                    break
                time.sleep(30)
                chunk_since = since_date + i * chunk_size
                chunk_until = min(since_date + (i + 1) * chunk_size, until_date)

                try:
                    chunk_query = f"{query} since:{chunk_since.strftime('%Y-%m-%d')} until:{chunk_until.strftime('%Y-%m-%d')}"
                    self.logger.info(f"Handling chunk: {i + 1}/{num_chunks}. Query: {chunk_query}")
                    chunk_tweets = app.search(chunk_query, pages=TWEETS_SEARCH_PAGES, wait_time=TWEETS_SEARCH_WAIT_TIME)
                    all_tweets.extend(chunk_tweets)
                    self.logger.info(f"Found {len(chunk_tweets.results)} tweets")
                except Exception as e:
                    error_message = f"Error while searching for tweets ({i + 1}/{num_chunks}): {type(e).__name__} - {str(e)}"
                    self.logger.error(error_message)
                self.logger.info(f"Finished handling chunk: {i + 1}/{num_chunks}")
            except KeyboardInterrupt:
                self.logger.error("Received KeyboardInterrupt. Cancelling the search.")
                self.cancel_search = True

        await self.save_tweets_to_csv(all_tweets, keyword)
        self.logger.info(f"Finished searching for {keyword} in {num_chunks} chunks")

    async def search_tweets(self, app, query, since, until, keyword):
        if until:
            query += f" until:{until}"
        if since:
            query += f" since:{since}"

        all_tweets = []
        try:
            all_tweets = app.search(query, pages=TWEETS_SEARCH_PAGES, wait_time=TWEETS_SEARCH_WAIT_TIME)
        except Exception as e:
            error_message = f"Error while searching for tweets: {type(e).__name__} - {str(e)}"
            self.logger.error(error_message)

        await self.save_tweets_to_csv(all_tweets, keyword)
        self.logger.info(f"Finished searching for {keyword}")

import asyncio

from twitter_service.twitter_handler import TweeterScraper


async def main():
    tweeter_scraper = TweeterScraper()
    await tweeter_scraper.fetch_tweets_and_save_to_csv("ChainCoin", "2017-07-14", "2017-07-12")
    await tweeter_scraper.get_data_from_database_and_convert_to_csv()
    tweeter_scraper.close_connection()


if __name__ == "__main__":
    asyncio.run(main())

if __name__ == "__main__":
    import logging
    import sys
    import os
    import asyncio
    sys.path.insert(0, os.getcwd())
    import Sentiment_correlation_analysis.sentiment_analysis as sentiment_analysis
    import Download_and_show_data.main as download_data
    import Download_tweets.Twitter_scrapper.twitter_service.twitter_handler as twitter_handler

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Starting twitter handler")
    Scrapper = twitter_handler.TweeterScraper()
    if not os.path.exists("csvs/onecoin_tweets.csv"):
        Scrapper.search_keyword_tweets_and_save_to_csv("onecoin")
    if not os.path.exists("csvs/xrp_tweets.csv"):
        Scrapper.search_keyword_tweets_and_save_to_csv("xrp")
    logger.info("Twitter handler done")
    logger.info("Starting download data")
    if not os.path.exists("csvs/one_data.csv") or not os.path.exists("csvs/xrp_data.csv"):
        download_data.main()
    logger.info("Download data done")
    logger.info("Starting sentiment analysis")
    sentiment_analysis.execute("one")
    sentiment_analysis.execute("xrp")
    logger.info("Sentiment analysis done")
    logger.info("Starting web page")
    sentiment_analysis.show_on_webpage("one")
    sentiment_analysis.show_on_webpage("xrp")
    logger.info("Web page done")
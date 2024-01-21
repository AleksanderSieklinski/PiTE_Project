def load_crypto(crypto):
    logger.info("Starting twitter handler")
    Scrapper = twitter_handler.TweeterScraper()
    if not os.path.exists("csvs/{0}_tweets.csv".format(crypto)):
        asyncio.run(Scrapper.search_keyword_tweets_and_save_to_csv(crypto))
    logger.info("Twitter handler done")
    logger.info("Starting download data")
    if not os.path.exists("csvs/{0}_data.csv".format(crypto)):
        download_data.main()
    logger.info("Download data done")
    logger.info("Starting sentiment analysis")
    sentiment_analysis.execute(crypto)
    logger.info("Sentiment analysis done")
    logger.info("Starting web page")
    sentiment_analysis.show_on_webpage(crypto)
    logger.info("Web page done")
    
    # logger.info("Predicting risk of pump&dump")
    # use_model_day.predict_if_PumpDump('csvs/{0}_merged.csv'.format(crypto))
    # logger.info("Prediction done")
    
if __name__ == "__main__":
    import logging
    import os
    import asyncio
    import Sentiment_correlation_analysis.sentiment_analysis as sentiment_analysis
    import Download_and_show_data.main as download_data
    import Download_tweets.Twitter_scrapper.twitter_service.twitter_handler as twitter_handler
    import Machine_learning.ML_model_and_data.use_model_day as use_model_day

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    load_crypto("one")
    load_crypto("bitconnect")
    load_crypto("bnb")
    load_crypto("chaincoin")
    load_crypto("magi")
    load_crypto("trx")
    load_crypto("vet")
    load_crypto("xrp")
    load_crypto("xvg")

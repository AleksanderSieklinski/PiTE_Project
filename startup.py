if __name__ == "__main__":
    import logging
    import os
    import Sentiment_correlation_analysis.sentiment_analysis as sentiment_analysis
    import Download_and_show_data.main as download_data

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Starting download data")
    download_data.main()
    logger.info("Download data done")
    logger.info("Starting sentiment analysis")
    sentiment_analysis.main()
    logger.info("Sentiment analysis done")
    logger.info("Starting web page")
    sentiment_analysis.show_on_webpage("one")
    sentiment_analysis.show_on_webpage("xrp")
    logger.info("Web page done")
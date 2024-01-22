

## twitter_scraper
### Installation

Install necessary packages using:
```bash
pip install -r requirements.txt
```
For better performance update base.py of `tweety` library, so it will stop scraping tweets if there is no more pages.

### Initialization

Create an instance of TweeterScraper.
It sets up logging and you can log into your Twitter account to enable searching by hashtag.
```
tweeter_scraper = TweeterScraper()
```

### Methods

Search for tweets from a specific Twitter account and save them.
```
search_user_tweets_and_save_to_csv(twitter_account):
```
Search for tweets related to a keyword and save them.
```
search_keyword_tweets_and_save_to_csv(keyword, until=None, since=None):
```


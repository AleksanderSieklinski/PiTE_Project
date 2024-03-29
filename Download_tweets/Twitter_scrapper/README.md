## twitter_scraper
### Installation

In order to run properly install necessary packages using:
```bash
pip install -r requirements.txt
```
For safety run with using terminal, so you will be able to stop scraping by pressing `ctrl+c` and all data will be saved.
Additionally, it's better to update base.py of `tweety` library, so it will stop scraping tweets if there is no more pages.

### Initialization

Create an instance of TweeterScraper.
It sets up logging and establishes a connection to a SQLite database. Additionally, u can log in into your Twitter account to enable searching by hashtag.
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
Retrieve all data from the connected database and save it to a CSV file.
```
get_data_from_database_and_convert_to_csv():
```


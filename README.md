In order to run properly install necessary packages using:

pip install -r requirements.txt

Usage Guide:
Initialization:

Create an instance of TweeterScraper.
It sets up logging and establishes a connection to a SQLite database.
Methods:

search_user_tweets_and_save_to_csv(twitter_account):
Searches for tweets from a specific Twitter account and saves them.

search_keyword_tweets_and_save_to_csv(keyword, until=None, since=None):
Searches for tweets related to a keyword and saves them.

get_data_from_database_and_convert_to_csv():
Retrieves all data from the connected database and saves it to a CSV file.

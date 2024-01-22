# PITE_PROJECT - PumpGuard
### Installation

Install necessary packages using:
```bash
pip install -r requirements.txt
```
For better performance update base.py of `tweety` library, so it will stop scraping tweets if there is no more pages.

## ML
Do uruchomienia modelu predykcyjnego potrzebujemy:
1) zainstalowanych bibliotek z requirements.txt
2) use_model.ipynb, model_epoch_307.hdf5, oraz naszej csv z przynajmniej 20 wierszami danych (oraz odpowiednimi kolumnami)
3) Dodajemy nazwe csv w use_model.ipynb i uruchamiamy: output to 0/1/2 (nie ma zagrożenia Pump&Dump, potencjalne zagrożenie, wysokie zagrożenie)
   Warto jednak zwrócić uwagę, że model zwraca często błędne dane

Model wczytuje 20 ostatnich lini, które MUSZĄ zawierać kolumny: 'Close', 'compound', 'likes', 'retweets' oddzielone przecinkiem.




## twitter_handler

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

## tweets_analyzer

### Initialization
Create an instance of TweetsAnalyzer and reads specified CSV file.
```
tweets_analyzer = TweetsAnalyzer(csv_file)
```

### Methods
Generates Number of Tweets about a Specific Cryptocurrency per Day
```
tweets_per_day_plot()
```
Generates User Engagement from Day to Day
```
engagement_per_day_plot()
```
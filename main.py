from tweety import Twitter
import pandas as pd

app = Twitter("session")
app.start()

all_tweets = app.search("ChainCoin until:2017-07-14 since:2017-07-12", pages=10,
                        wait_time=2)

df_tweets = pd.DataFrame(columns=["Date", "Text", "Likes", "Retweets"])

for tweet in all_tweets:
    new_row = pd.DataFrame({
        "Date": [tweet.date],
        "Text": [tweet.text],
        "Likes": [tweet.likes],
        "Retweets": [tweet.retweet_counts]
    })
    df_tweets = pd.concat([df_tweets, new_row], ignore_index=True)
    df_tweets.to_csv('csvs/tweets.csv', index=False)

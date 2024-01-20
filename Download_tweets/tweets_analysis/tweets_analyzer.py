import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

class TweetsAnalyzer:
    def __init__(self, csv_file):
        self.csv_name = os.path.basename(csv_file)
        self.df = pd.read_csv(csv_file)
        self.df['Date'] = pd.to_datetime(self.df['Date'])

    def tweets_per_day_plot(self):
        tweets_per_day = self.df.groupby(self.df['Date'].dt.date).size()
        st.bar_chart(tweets_per_day)
        st.title('Number of Tweets about a Specific Cryptocurrency per Day')

    def engagement_per_day_plot(self):
        engagement_per_day = self.df.groupby(self.df['Date'].dt.date)[['Likes', 'Retweets']].sum()
        st.line_chart(engagement_per_day, color=['#0000FF', '#00FF00'])
        st.title('User Engagement from Day to Day')

if __name__ == "__main__":
    tweets_analyzer = TweetsAnalyzer('../csvsGOOD/tweets_ChainCoin_2023-12-28_22-03-13.csv')
    plot_option = st.sidebar.radio('Select Plot:', ('Tweets per Day', 'Engagement per Day'))
    if plot_option == 'Tweets per Day':
        tweets_analyzer.tweets_per_day_plot()
    elif plot_option == 'Engagement per Day':
        tweets_analyzer.engagement_per_day_plot()

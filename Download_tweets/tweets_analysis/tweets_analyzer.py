import streamlit as st
import pandas as pd
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

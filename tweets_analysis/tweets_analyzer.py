# import pandas as pd
# import matplotlib.pyplot as plt
# import os
#
# class TweetsAnalyzer:
#     def __init__(self, csv_file):
#         self.csv_name = os.path.basename(csv_file)
#         self.df = pd.read_csv(csv_file)
#         self.df['Date'] = pd.to_datetime(self.df['Date'])
#
#     def create_plots_folder(self):
#         if not os.path.exists('plots'):
#             os.makedirs('plots')
#
#     def tweets_per_day_plot(self):
#         tweets_per_day = self.df.groupby(self.df['Date'].dt.date).size()
#         plt.figure(figsize=(10, 6))
#         tweets_per_day.plot(kind='bar', color='skyblue')
#         plt.title('Ilość tweetów o danej kryptowalucie na dzień')
#         plt.xlabel('Data')
#         plt.ylabel('Ilość tweetów')
#         plt.xticks(rotation=45)
#         plt.gca().set_xticks(
#             range(0, len(tweets_per_day), max(len(tweets_per_day) // 10, 1)))
#         plt.tight_layout()
#         plt.savefig(f'plots/tweets_per_day_{self.csv_name}.png')
#         plt.close()
#
#     def engagement_per_day_plot(self):
#         engagement_per_day = self.df.groupby(self.df['Date'].dt.date)[['Likes', 'Retweets']].sum()
#         plt.figure(figsize=(10, 6))
#         engagement_per_day.plot(kind='line')
#         plt.title('Zaangażowanie użytkowników z dnia na dzień')
#         plt.xlabel('Data')
#         plt.ylabel('Suma polubień i retweetów')
#         plt.legend(['Polubienia', 'Retweety'])
#         plt.xticks(rotation=45)
#         plt.tight_layout()
#         plt.savefig(f'plots/engagement_per_day_{self.csv_name}.png')
#         plt.close()
#
#
# if __name__ == "__main__":
#     tweets_analyzer = TweetsAnalyzer('tweets.csv')
#     tweets_analyzer.create_plots_folder()
#     tweets_analyzer.tweets_per_day_plot()
#     tweets_analyzer.engagement_per_day_plot()


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

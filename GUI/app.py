import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Machine_learning.ML_model_and_data.use_model_day as use_model_day


st.set_page_config(page_title="PiTE_Project", page_icon="💹", layout="wide")

st.title("PiTE_Project")

dict_crypto = {"Ripple": "XRP", "OneCoin": "ONE", "Bitconnect": "Bitconnect", "Binance Coin": "BNB", "ChainCoin": "ChainCoin", "Magi": "Magi", 
               "TRON": "TRX", "VeChain": "VET", "Verge": "XVG"}

selected_crypto = st.sidebar.selectbox("Select crypto", list(dict_crypto.keys()))


def get_crypto_data(crypto_name):
    crypto_iso = dict_crypto[crypto_name]
    # crypto_data = pd.read_csv("../csvs/" + crypto_iso.lower() + "_merged.csv", parse_dates=['Date'])
    # crypto_sentiment = pd.read_csv("../csvs/" + crypto_iso.lower() + "_sentiment.csv", parse_dates=['Date']) # version for local testing
    crypto_data = pd.read_csv("csvs/" + crypto_iso.lower() + "_merged.csv", parse_dates=['Date'])
    crypto_sentiment = pd.read_csv("csvs/" + crypto_iso.lower() + "_sentiment.csv", parse_dates=['Date']) # version for startup.py
    return crypto_iso, crypto_data, crypto_sentiment
    
crypto_iso = get_crypto_data(selected_crypto)[0]
crypto_data = get_crypto_data(selected_crypto)[1]
crypto_sentiment = get_crypto_data(selected_crypto)[2]

# limit data to range in crypto_data
min_date_data = crypto_data['Date'].min()
min_date_sentiment = crypto_sentiment['Date'].min()
min_date = max(min_date_data, min_date_sentiment)
max_date_data = crypto_data['Date'].max()
max_date_sentiment = crypto_sentiment['Date'].max()
max_date = min(max_date_data, max_date_sentiment)
choose_date = max_date

# date input
col1, col2, col3, col4, col5 = st.columns([1,1,6,1,1])
start_date = pd.to_datetime(col1.date_input('Start date', min_date, min_value=min_date, max_value=max_date))
end_date = pd.to_datetime(col2.date_input('End date', max_date, min_value=min_date, max_value=max_date))
choose_date = pd.to_datetime(col4.date_input('Choose date', choose_date, min_value=min_date, max_value=max_date))

if start_date > end_date:
    st.error('Error: End date must fall after start date.')

# filter data by date
crypto_data = crypto_data[(crypto_data['Date'] >= start_date) & (crypto_data['Date'] <= end_date)]
crypto_sentiment = crypto_sentiment[(crypto_sentiment['Date'] >= start_date) & (crypto_sentiment['Date'] <= end_date)]

# button for p&d prediction
if col5.button('Predict pump&dump'):
    # danger = use_model_day.predict_if_PumpDump('../csvs/' + crypto_iso.lower() + '_merged.csv', choose_date) # version for local testing
    danger = use_model_day.predict_if_PumpDump('csvs/' + crypto_iso.lower() + '_merged.csv', choose_date) # version for startup.py
    if danger == 0:
        st.markdown("<h2 style='text-align: center; color: green;'>No danger</h2>", unsafe_allow_html=True)
    elif danger == 1:
        st.markdown("<h2 style='text-align: center; color: orange;'>Potential danger</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='text-align: center; color: red;'>High danger</h2>", unsafe_allow_html=True)

# create two columns to display plots next to each other
col1, col2 = st.columns(2)

# price plot
price_fig = go.Figure()
price_fig.add_trace(go.Scatter(x=crypto_data['Date'], y=crypto_data['Close'], mode='lines'))

# update axes names
price_fig.update_xaxes(title_text='Date')
price_fig.update_yaxes(title_text='Price [$]', range=[0, 1.3 * crypto_data['Close'].max()])
price_fig.update_layout(title_text= dict_crypto[selected_crypto] + ' price over time')

# isplay price plot
col1.plotly_chart(price_fig)

# volume plot
volume_fig = go.Figure()
volume_fig.add_trace(go.Scatter(x=crypto_data['Date'], y=crypto_data['Volume'], mode='lines'))

volume_fig.update_xaxes(title_text='Date')
volume_fig.update_yaxes(title_text='Volume [$]', range=[0, 1.3 * crypto_data['Volume'].max()])
volume_fig.update_layout(title_text= dict_crypto[selected_crypto] + ' volume over time')

# display volume plot
col2.plotly_chart(volume_fig)


# sentiment plot
sentiment_fig = go.Figure()
sentiment_fig.add_trace(go.Scatter(x=crypto_sentiment['Date'], y=crypto_sentiment['compound'], mode='lines'))

sentiment_fig.update_xaxes(title_text='Date')
sentiment_fig.update_yaxes(title_text='Sentiment', range=[crypto_sentiment['compound'].min() - 0.1, crypto_sentiment['compound'].max() + 0.1])
sentiment_fig.update_layout(title_text= dict_crypto[selected_crypto] + ' opinion on Twitter')

col1.plotly_chart(sentiment_fig)




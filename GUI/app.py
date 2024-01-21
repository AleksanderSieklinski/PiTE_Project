import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="PiTE_Project", page_icon="💹", layout="wide")

st.title("PiTE_Project")

dict_crypto = {"Ripple": "XRP", "OneCoin": "ONE"} # !!!update with all cryptos afterwards!!!

selected_crypto = st.sidebar.selectbox("Select crypto", list(dict_crypto.keys()))


def get_crypto_data(crypto_name):
    crypto_iso = dict_crypto[crypto_name]
    crypto_data = pd.read_csv("../csvs/" + crypto_iso.lower() + "_merged.csv", parse_dates=['Date'])
    return crypto_iso, crypto_data
    
crypto_iso = get_crypto_data(selected_crypto)[0]
crypto_data = get_crypto_data(selected_crypto)[1]

# limit data to range in crypto_data
min_date = crypto_data['Date'].min()
max_date = crypto_data['Date'].max()

# date input
col1, col2, col3, col4 = st.columns([1,1,3,3])
start_date = pd.to_datetime(col1.date_input('Start date', min_date, min_value=min_date, max_value=max_date))
end_date = pd.to_datetime(col2.date_input('End date', max_date, min_value=min_date, max_value=max_date))

if start_date > end_date:
    st.error('Error: End date must fall after start date.')

# filter data by date
crypto_data = crypto_data[(crypto_data['Date'] >= np.datetime64(start_date)) & (crypto_data['Date'] <= np.datetime64(end_date))]

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
sentiment_fig.add_trace(go.Scatter(x=crypto_data['Date'], y=crypto_data['compound'], mode='lines'))

sentiment_fig.update_xaxes(title_text='Date')
sentiment_fig.update_yaxes(title_text='Sentiment', range=[-1,1])
sentiment_fig.update_layout(title_text= dict_crypto[selected_crypto] + ' opinion on Twitter')

col1.plotly_chart(sentiment_fig)




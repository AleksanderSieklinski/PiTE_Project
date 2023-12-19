import yfinance as yf
import pandas as pd
import streamlit as st
from datetime import datetime



# Change cryptocurrencies and start date to your preference
start_date = "2020-01-01"
end_date = datetime.today().strftime('%Y-%m-%d')
crypto_data = yf.download("BTC-USD DOGE-USD ETH-USD", start=start_date, end=end_date)

btc_data = crypto_data["Close"]["BTC-USD"].dropna()
doge_data = crypto_data["Close"]["DOGE-USD"].dropna()
eth_data = crypto_data["Close"]["ETH-USD"].dropna()

btc_data.to_csv("btc_data.csv")
doge_data.to_csv("doge_data.csv")
eth_data.to_csv("eth_data.csv")

st.markdown("# Crypto Price Analysis")
st.markdown("## Bitcoin Price")
st.line_chart(btc_data)

st.markdown("## Dogecoin Price")
st.line_chart(doge_data)

st.markdown("## Ethereum Price")
st.line_chart(eth_data)
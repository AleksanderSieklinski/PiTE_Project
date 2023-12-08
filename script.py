import yfinance as yf
import pandas as pd
import streamlit as st

crypto_data = yf.download("BTC-USD DOGE-USD ETH-USD", period="max")

btc_data = crypto_data["Close"]["BTC-USD"].dropna()
doge_data = crypto_data["Close"]["DOGE-USD"].dropna()
eth_data = crypto_data["Close"]["ETH-USD"].dropna()

st.markdown("# Crypto Price Analysis")
st.markdown("## Bitcoin Price")
st.line_chart(btc_data)

st.markdown("## Dogecoin Price")
st.line_chart(doge_data)

st.markdown("## Ethereum Price")
st.line_chart(eth_data)
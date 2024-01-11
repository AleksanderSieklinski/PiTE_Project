import streamlit as st
import pandas as pd
from datetime import datetime
from cryptocmd import CmcScraper

# Verge
xvg_scraper = CmcScraper("XVG", "02-04-2017", "13-10-2018")
xvg_data = xvg_scraper.get_dataframe()
xvg_data.set_index('Date', inplace=True)
xvg_data.to_csv("xvg_data.csv")

# TRON
trx_scraper = CmcScraper("TRX", "01-11-2017", "01-12-2018")
trx_data = trx_scraper.get_dataframe()
trx_data.set_index('Date', inplace=True)
trx_data.to_csv("trx_data.csv")

# Binance Coin
bnb_scraper = CmcScraper("BNB", "01-12-2020", "21-07-2021")
bnb_data = bnb_scraper.get_dataframe()
bnb_data.set_index('Date', inplace=True)
bnb_data.to_csv("bnb_data.csv")

# Vechain
vet_scraper = CmcScraper("VET", "01-12-2020", "21-07-2021")
vet_data = vet_scraper.get_dataframe()
vet_data.set_index('Date', inplace=True)
vet_data.to_csv("vet_data.csv")

# 1Coin
one_scraper = CmcScraper("1COIN")
one_data = one_scraper.get_dataframe()
one_data.set_index('Date', inplace=True)
one_data.to_csv("one_data.csv")

# XRP
xrp_scraper = CmcScraper("XRP")
xrp_data = xrp_scraper.get_dataframe()
xrp_data.set_index('Date', inplace=True)
xrp_data.to_csv("xrp_data.csv")

# ChainCoin
chaincoin_data = pd.read_csv("chaincoin_data.csv", parse_dates=['Start']) 
chaincoin_data = chaincoin_data.rename(columns={'Start': 'Date'})
chaincoin_data.set_index('Date', inplace=True)
chaincoin_start_date = datetime.strptime("2017-01-02", "%Y-%m-%d")
chaincoin_end_date = datetime.strptime("2017-11-06", "%Y-%m-%d")
chaincoin_data = chaincoin_data[(chaincoin_data.index >= chaincoin_start_date) & (chaincoin_data.index <= chaincoin_end_date)]
chaincoin_data.to_csv("chaincoin_data_final.csv", index=False)

# Magi
magi_data = pd.read_csv("magi_data.csv", index_col=0, parse_dates=True)
magi_data = magi_data.rename(columns={'Start': 'Date'})
magi_start_date = datetime.strptime("2016-10-01", "%Y-%m-%d")
magi_end_date = datetime.strptime("2018-07-30", "%Y-%m-%d")
magi_data = magi_data[(magi_data.index >= magi_start_date) & (magi_data.index <= magi_end_date)]
magi_data.to_csv("magi_data_final.csv", index=False)

# BitConnect
bitconnect_data = pd.read_csv("bitconnect_data.csv", index_col=0, parse_dates=True)
bitconnect_data = bitconnect_data.rename(columns={'Start': 'Date'})
bitconnect_start_date = datetime.strptime("2017-01-12", "%Y-%m-%d")
bitconnect_end_date = datetime.strptime("2020-01-16", "%Y-%m-%d")
bitconnect_data = bitconnect_data[(bitconnect_data.index >= bitconnect_start_date) & (bitconnect_data.index <= bitconnect_end_date)]
bitconnect_data.to_csv("bitconnect_data_final.csv", index=False)



st.markdown("# Crypto Price Analysis")
st.markdown("## Verge Price")
st.line_chart(xvg_data["Close"])
st.markdown("## TRON Price")
st.line_chart(trx_data["Close"])
st.markdown("## Binance Coin Price")
st.line_chart(bnb_data["Close"])
st.markdown("## Vechain Price")
st.line_chart(vet_data["Close"])
st.markdown("## 1Coin Price")
st.line_chart(one_data["Close"])
st.markdown("## XRP Price")
st.line_chart(xrp_data["Close"])
st.markdown("## ChainCoin Price")
st.line_chart(chaincoin_data["Close"])
st.markdown("## Magi Price")
st.line_chart(magi_data["Close"])
st.markdown("## BitConnect Price")
st.line_chart(bitconnect_data["Open"])



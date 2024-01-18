import pandas as pd
from datetime import datetime
from cryptocmd import CmcScraper

# Verge
xvg_scraper = CmcScraper("XVG", "02-04-2017", "13-10-2018")
xvg_data = xvg_scraper.get_dataframe()
xvg_data.set_index('Date', inplace=True)
xvg_data.to_csv("final_data/xvg_data_final.csv")

# TRON
trx_scraper = CmcScraper("TRX", "01-11-2017", "01-12-2018")
trx_data = trx_scraper.get_dataframe()
trx_data.set_index('Date', inplace=True)
trx_data.to_csv("final_data/trx_data_final.csv")

# Binance Coin
bnb_scraper = CmcScraper("BNB", "01-12-2020", "21-07-2021")
bnb_data = bnb_scraper.get_dataframe()
bnb_data.set_index('Date', inplace=True)
bnb_data.to_csv("final_data/bnb_data_final.csv")

# Vechain
vet_scraper = CmcScraper("VET", "01-12-2020", "21-07-2021")
vet_data = vet_scraper.get_dataframe()
vet_data.set_index('Date', inplace=True)
vet_data.to_csv("final_data/vet_data_final.csv")

# 1Coin
onecoin_data = pd.read_csv("onecoin_data.csv", parse_dates=['Date'])
onecoin_data.set_index('Date', inplace=True)
onecoin_start_date = datetime.strptime("2021-01-01", "%Y-%m-%d")
onecoin_end_date = datetime.strptime("2022-01-01", "%Y-%m-%d")
onecoin_data = onecoin_data[(onecoin_data.index >= onecoin_start_date) & (onecoin_data.index <= onecoin_end_date)]
onecoin_data.to_csv("final_data/onecoin_data_final.csv")

# XRP
xrp_scraper = CmcScraper("XRP")
xrp_data = xrp_scraper.get_dataframe()
xrp_data.set_index('Date', inplace=True)
xrp_data.to_csv("final_data/xrp_data_final.csv")

# ChainCoin
chaincoin_data = pd.read_csv("chaincoin_data.csv", parse_dates=['Start']) 
chaincoin_data = chaincoin_data.rename(columns={'Start': 'Date'})
chaincoin_data.set_index('Date', inplace=True)
chaincoin_start_date = datetime.strptime("2017-01-02", "%Y-%m-%d")
chaincoin_end_date = datetime.strptime("2017-11-06", "%Y-%m-%d")
chaincoin_data = chaincoin_data[(chaincoin_data.index >= chaincoin_start_date) & (chaincoin_data.index <= chaincoin_end_date)]
chaincoin_data.to_csv("final_data/chaincoin_data_final.csv", index=False)

# Magi
magi_data = pd.read_csv("magi_data.csv", index_col=0, parse_dates=True)
magi_data = magi_data.rename(columns={'Start': 'Date'})
magi_start_date = datetime.strptime("2016-10-01", "%Y-%m-%d")
magi_end_date = datetime.strptime("2018-07-30", "%Y-%m-%d")
magi_data = magi_data[(magi_data.index >= magi_start_date) & (magi_data.index <= magi_end_date)]
magi_data.to_csv("final_data/magi_data_final.csv", index=False)

# BitConnect
bitconnect_data = pd.read_csv("bitconnect_data.csv", index_col=0, parse_dates=True)
bitconnect_data = bitconnect_data.rename(columns={'Start': 'Date'})
bitconnect_start_date = datetime.strptime("2017-01-12", "%Y-%m-%d")
bitconnect_end_date = datetime.strptime("2020-01-16", "%Y-%m-%d")
bitconnect_data = bitconnect_data[(bitconnect_data.index >= bitconnect_start_date) & (bitconnect_data.index <= bitconnect_end_date)]
bitconnect_data.to_csv("final_data/bitconnect_data_final.csv", index=False)

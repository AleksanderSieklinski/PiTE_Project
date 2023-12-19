import yfinance as yf

btc_ticker = yf.Ticker("BTC-USD")
btc_data = btc_ticker.history(period="1y")
btc_data.to_csv("btc.csv")

doge_ticker = yf.Ticker("DOGE-USD")
doge_data = doge_ticker.history(period="1y")
doge_data.to_csv("doge.csv")

eth_ticker = yf.Ticker("ETH-USD")
eth_data = eth_ticker.history(period="1y")
eth_data.to_csv("eth.csv")
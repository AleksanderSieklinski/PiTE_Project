import streamlit as st
import pandas as pd

st.title("Crypto Price (one year)")

dogef = pd.read_csv("doge.csv")
bitf = pd.read_csv("btc.csv")
ethf = pd.read_csv("eth.csv")

dogef = dogef.set_index("Date")
bitf = bitf.set_index("Date")
ethf = ethf.set_index("Date")

st.write("Dogecoin")
st.line_chart(dogef["Close"])
st.write("Bitcoin")
st.line_chart(bitf["Close"])
st.write("Ethereum")
st.line_chart(ethf["Close"])





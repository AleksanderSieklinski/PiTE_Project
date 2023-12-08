import streamlit as st
import pandas as pd
import altair as alt

dogef = pd.read_csv("dogecoin.csv")
bitf = pd.read_csv("bitcoin.csv")
ethf = pd.read_csv("ethereum.csv")

dogef['date'] = pd.to_datetime(dogef['date']).dt.date
bitf['date'] = pd.to_datetime(bitf['date']).dt.date
ethf['date'] = pd.to_datetime(ethf['date']).dt.date

st.title("Cryptocurrency prices charts")
st.markdown("### Dogecoin")
st.line_chart(dogef.set_index('date')['price'])

st.markdown("### Bitcoin")
st.line_chart(bitf.set_index('date')['price'])

st.markdown("### Ethereum")
st.line_chart(ethf.set_index('date')['price'])



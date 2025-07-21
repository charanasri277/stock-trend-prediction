import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st

# Title
st.title('📈 Stock Trend Prediction')

# 🟢 Correct variable name used consistently
stock_ticker_input = st.text_input('Enter the stock ticker', 'AAPL')

if stock_ticker_input:
    df = yf.download(stock_ticker_input, start='2010-01-01', end='2022-12-21')

    if not df.empty:
        plt.figure(figsize=(12,6))
        plt.plot(df.index, df['Close'])
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.title(f'{stock_ticker_input} Closing Price')
        st.pyplot(plt)
    else:
        st.error("No data found.")



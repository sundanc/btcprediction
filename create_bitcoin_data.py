import yfinance as yf
import pandas as pd


ticker_symbol = 'BTC-USD'

btc_data = yf.download(ticker_symbol, start='2016-01-01', end='2024-11-28')


btc_data.to_csv('bitcoin_data.csv')

print("Bitcoin data has been saved to 'bitcoin_data.csv'")

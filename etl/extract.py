import yfinance as yf
import pandas as pd

#need to get name, symbol, ohlc, volume to fill the db name
def fetch_data(ticker: str, start: str, end: str): 
    symbol = yf.Ticker(ticker)
    name = symbol.get_info()
    ohlcv_df = yf.download([symbol], start = start, end = end)
    return symbol, name, ohlcv_df
    



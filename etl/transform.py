import pandas as pd
import yfinance as yf

#need to get name, symbol, ohlc, volume to fill the db name
ohlcv_df = yf.download("MSFT", start = "2025-10-11", end = "2025-10-16")
def clean_data(name: str, symbol: str, dataframe:pd.DataFrame):
    dataframe = dataframe.droplevel('Ticker', axis=1)
    dataframe = dataframe.reset_index()
    dataframe = dataframe.rename(columns={'Open':'open', 
                                          'Close':'close', 
                                          'High': 'high',
                                          'Low':'low',
                                          'Volume':'volume',
                                          'Date':'date'
                                          })
    dataframe['ticker'] = symbol
    return dataframe
clean_data('Microsoft', "MSFT", ohlcv_df)


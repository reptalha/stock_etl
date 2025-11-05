import pandas as pd
import yfinance as yf

#need to get name, symbol, ohlc, volume to fill the db name
ohlcv_df = yf.download("MSFT", start = "2025-10-11", end = "2025-10-16")
def clean_data(name: str, symbol: str, dataframe:pd.DataFrame):
    dataframe.columns = [col[0] for col in dataframe.columns] 
    dataframe = dataframe.reset_index()
    dataframe = dataframe.rename(columns={
        "Open":"open", 
        "High":"high", 
        "Low":"low", 
        "Close":"close", 
        "Volume":"volume", 
        "Date":"date"})
    dataframe['ticker'] = symbol
    dataframe = dataframe.dropna()
    print(dataframe.head())
    
    
clean_data('Microsoft', "MSFT", ohlcv_df)
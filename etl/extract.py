import yfinance as yf
import pandas as pd

def fetch_data(ticker: str, start: str, end: str): 
    df = yf.download([ticker], start = start, end = end)
    return df




from sqlalchemy import create_engine
import pandas as pd
import yfinance as yf
import os
from dotenv import load_dotenv
from etl.extract import fetch_data
from etl.transform import clean_data

raw = fetch_data("MSFT", "2025-10-11", "2025-10-16")
clean = clean_data("Microsoft", "MSFT", raw)
load_dotenv("config/db_config.env")
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL)

def load_to_db(dataframe:pd.DataFrame):
    dataframe.to_sql(
    name="daily_stock_data",
    con=engine,
    if_exists="append",
    index=False
)




load_to_db(clean)
    
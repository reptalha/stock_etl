CREATE TABLE tickers(symbol VARCHAR(10) PRIMARY KEY, name TEXT);

CREATE TABLE daily_stock_data (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) REFERENCES tickers(symbol),
    date DATE NOT NULL,
    open NUMERIC,
    high NUMERIC,
    low NUMERIC,
    close NUMERIC,
    volume BIGINT,
    UNIQUE (ticker, date)
);
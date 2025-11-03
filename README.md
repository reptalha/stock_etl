# Financial Market ETL Pipeline (Python + PostgreSQL)

A Python-based ETL pipeline for collecting, transforming, and storing stock market data in PostgreSQL.

## Features
- Extracts daily OHLCV data via Yahoo Finance API
- Cleans, validates, and computes daily returns
- Loads data into normalized PostgreSQL tables
- Designed for scalability and automation (cron jobs)

## Tech Stack
**Python:** pandas, SQLAlchemy, yfinance  
**Database:** PostgreSQL  
**Automation:** cron (for daily scheduling)

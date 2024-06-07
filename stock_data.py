import yfinance as yf

def get_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    return df

def save_stock_data_to_csv(stock_df, filename):
    stock_df.to_csv(filename, index=True)
    print(f'Stock data saved to {filename}')

import pandas as pd
import matplotlib.pyplot as plt

def merge_news_stock_data(news_filename, stock_df):
    df_news = pd.read_csv(news_filename)
    df_news['publishedAt'] = pd.to_datetime(df_news['publishedAt'])
    stock_df.index = pd.to_datetime(stock_df.index)
    merged_df = pd.merge(df_news, stock_df, left_on='publishedAt', right_index=True, how='inner')
    merged_filename = news_filename.replace('.csv', '_stock.csv')
    merged_df.to_csv(merged_filename, index=False)
    print(f'Merged data saved to {merged_filename}')
    return merged_filename

def visualize_data(merged_filename):
    df = pd.read_csv(merged_filename)
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['publishedAt'], df['compound'], label='Sentiment')
    plt.plot(df['publishedAt'], df['Close'], label='Stock Price')
    plt.legend()
    plt.title('Sentiment vs. Stock Price')
    plt.show()

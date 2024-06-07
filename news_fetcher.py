import requests
import pandas as pd

# Your NewsAPI key
api_key = 'f5732e4ba98641e590632055326f6b6b'

def get_news(query, from_date, to_date, api_key):
    url = f'https://newsapi.org/v2/everything?q={query}&from={from_date}&to={to_date}&sortBy=publishedAt&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    print("API response:", data)

    if 'articles' in data:
        return data['articles']
    else:
        print("Error fetching news:", data)
        return []

def save_news_to_csv(articles, filename):
    df = pd.DataFrame(articles)
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    df.to_csv(filename, index=False)
    print(f'News data saved to {filename}')

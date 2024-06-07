import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(text)
    return sentiment

def add_sentiment_to_news(filename):
    df = pd.read_csv(filename)
    sentiments = df['description'].apply(lambda x: analyze_sentiment(str(x)))
    sentiment_df = pd.DataFrame(sentiments.tolist())
    df = pd.concat([df, sentiment_df], axis=1)
    sentiment_filename = filename.replace('.csv', '_sentiment.csv')
    df.to_csv(sentiment_filename, index=False)
    print(f'Sentiment analysis saved to {sentiment_filename}')
    return sentiment_filename

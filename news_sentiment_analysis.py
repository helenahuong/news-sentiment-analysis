from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import os

# Ensure NLTK_DATA environment variable is set correctly
nltk_data_path = os.environ.get('NLTK_DATA')
if nltk_data_path:
    print(f"Using NLTK_DATA path: {nltk_data_path}")
else:
    raise EnvironmentError("NLTK_DATA environment variable not set")

# Check if the vader_lexicon.txt file exists in the specified path
lexicon_file_path = os.path.join(nltk_data_path, 'sentiment/vader_lexicon/vader_lexicon.txt')
if os.path.exists(lexicon_file_path):
    print(f"vader_lexicon.txt found at {lexicon_file_path}")
else:
    raise FileNotFoundError(f"vader_lexicon.txt not found at {lexicon_file_path}")

# Define the function to analyze sentiment using the specified lexicon file
def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer(lexicon_file=lexicon_file_path)
    sentiment = sid.polarity_scores(text)
    return sentiment

# Define the function to add sentiment to news
def add_sentiment_to_news(filename):
    df = pd.read_csv(filename)
    sentiments = df['description'].apply(lambda x: analyze_sentiment(str(x)))
    sentiment_df = pd.json_normalize(sentiments)
    result_df = pd.concat([df, sentiment_df], axis=1)
    
    # Classify sentiment based on compound score
    result_df['sentiment_label'] = result_df['compound'].apply(lambda x: 'positive' if x > 0.05 else ('negative' if x < -0.05 else 'neutral'))
    
    # Rearrange columns for better readability
    columns_order = ['source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content', 'neg', 'neu', 'pos', 'compound', 'sentiment_label']
    result_df = result_df[columns_order]
    
    output_filename = 'sentiment_' + filename
    result_df.to_csv(output_filename, index=False)
    return output_filename

# Main function
if __name__ == "__main__":
    news_filename = 'nvidia_news_may_2024.csv'  # Hardcoded filename
    sentiment_filename = add_sentiment_to_news(news_filename)
    print(f"Sentiment analysis completed. Results saved to {sentiment_filename}")

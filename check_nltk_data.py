import os

nltk_data_path = os.getenv('NLTK_DATA')
print(f"NLTK_DATA is set to: {nltk_data_path}")

vader_lexicon_path = os.path.join(nltk_data_path, 'sentiment', 'vader_lexicon', 'vader_lexicon.txt')
if os.path.isfile(vader_lexicon_path):
    print(f"vader_lexicon.txt found at: {vader_lexicon_path}")
else:
    print(f"vader_lexicon.txt NOT found at: {vader_lexicon_path}")

import sys
import os

print("Current working directory:", os.getcwd())
print("Current file:", __file__)

# Ensure the current directory is in the module search path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
print("Updated sys.path:", sys.path)

print("Attempting to import from news_fetcher")

try:
    from news_fetcher import get_news, save_news_to_csv
    print("Successfully imported from news_fetcher")
except ImportError as e:
    print(f"Failed to import from news_fetcher: {e}")

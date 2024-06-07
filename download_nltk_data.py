import nltk
import ssl
import certifi

# Use certifi's CA bundle
ssl._create_default_https_context = ssl.create_default_context
ssl._create_default_https_context().load_verify_locations(certifi.where())

# Download the vader_lexicon
nltk.download('vader_lexicon')

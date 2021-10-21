# Console program that show random quotes from movies and shows

# Librarys needed
import requests
from googletrans import Translator

# API
url = "https://movie-quote-api.herokuapp.com/v1/quote/"

# Getting data
response = requests.get(url)
data = response.json()

# Google translator object
translator = Translator()

# Random quote and show
quote = data['quote']
show = data['show']

print("Quote:", quote)
print("Show:", show)
import json
import os

SECRET_KEY = os.getenv("SECRET_KEY")

MAPS_API_KEY = os.getenv("API_PASSWORD")

with open("stop_words.json") as json_stop_words:
    STOP_WORDS = json.load(json_stop_words)

WORDS_TO_REMOVE = [
    "bonjour",
    "bonsoir",
    "salut",
    "hello",
    "adresse",
    "situé",
    "situe",
    "trouve"
]

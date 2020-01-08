import json
import secret
import os

SECRET_KEY = secret.SECRET_KEY
MAPS_API_KEY = os.environ['API_PASSWORD']


print(MAPS_API_KEY)
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

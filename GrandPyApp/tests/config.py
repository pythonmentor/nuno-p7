import json

SECRET_KEY ="#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

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


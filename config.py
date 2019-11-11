import json

SECRET_KEY ="#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

with open("stop_words.json") as json_stop_words:
    stop_words = json.load(json_stop_words)

STOP_WORDS = stop_words

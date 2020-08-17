import json
import os

MAPS_API_KEY = os.environ['API_PASSWORD']
API_PASS_FRONT = os.environ['API_PASS_FRONT']


with open("stop_words.json") as json_stop_words:
    STOP_WORDS = json.load(json_stop_words)

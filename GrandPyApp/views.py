from flask import Flask
from .first_input_parser import (
    parse_user_input,
    important_words
)

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']
g_maps_key = app.config["MAPS_API_KEY"]
stop_words_custom = app.config['STOP_WORDS']
words_to_remove = app.config['WORDS_TO_REMOVE']


@app.route('/')
def index():
    return "Hello world !"


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from .first_input_parser import (
    parse_user_input,
    important_words
)
from .interface_requests import (
    call_google_maps_positionnement,
    call_google_maps_details,
    call_wiki_main_page,
    call_wiki_found_page
)

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']
g_maps_key = app.config["MAPS_API_KEY"]
stop_words_custom = app.config['STOP_WORDS']
words_to_remove = app.config['WORDS_TO_REMOVE']


@app.route('/')
def home():
    return render_template("index.html")


"""@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        message = request.form['message-input']
        parced_msg = parse_user_input(message, stop_words_custom)
        msg_to_api_requests = important_words(parced_msg, important_words)
        msg_gmaps = call_google_maps_positionnement(
            g_maps_key,
            msg_to_api_requests
            )
        wiki_title = call_wiki_main_page(parced_msg)

        if msg_gmaps[2] == IndexError or wiki_title[1] == IndexError:
            return jsonify(msg_gmaps)
        else:
            msg_gmaps_url = call_google_maps_details(g_maps_key, msg_gmaps[0])
            wiki_title = call_wiki_main_page(parced_msg)
            history = call_wiki_found_page(wiki_title[1])

            return jsonify(
                title=wiki_title[0],
                history=history,
                location=msg_gmaps[1],
                adress=msg_gmaps[2],
                url=msg_gmaps_url
                )"""


if __name__ == "__main__":
    app.run(debug=True)

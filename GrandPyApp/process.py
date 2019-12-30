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


def grandPyWork(message, app):
    # Config options
    app.config.from_object('config')
    # To get one variable, tape app.config['MY_VARIABLE']
    g_maps_key = app.config["MAPS_API_KEY"]
    stop_words_custom = app.config['STOP_WORDS']
    words_to_remove = app.config['WORDS_TO_REMOVE']
    print(message)
    parced_msg = parse_user_input(message, stop_words_custom)
    msg_to_api_requests = important_words(parced_msg, words_to_remove)
    msg_gmaps = call_google_maps_positionnement(
        g_maps_key,
        msg_to_api_requests
        )
    wiki_title = call_wiki_main_page(parced_msg)

    if msg_gmaps[2] == IndexError or wiki_title[1] == IndexError:
        return msg_gmaps
    else:
        msg_gmaps_url = call_google_maps_details(g_maps_key, msg_gmaps[0])
        wiki_title = call_wiki_main_page(parced_msg)
        history = call_wiki_found_page(wiki_title[1])

        message = [
            "Et donc tu veux savoir " + wiki_title[0]+ "Coquinou, quand même!",
            "Et bein oui c'est au " + msg_gmaps[2] + "pas bête la bête!",
            "En plus ce-ci est cadeau, gratos, rien que pour toi " + history,
            " je te montre?, un dessin ? " + msg_gmaps_url
        ]
        return message


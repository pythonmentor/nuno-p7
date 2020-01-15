from .first_input_parser import parse_user_input, important_words
from .interface_requests import (
    call_google_maps_positionnement,
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
    parced_msg = parse_user_input(message, stop_words_custom)
    msg_to_api_requests = important_words(parced_msg, words_to_remove)

    msg_gmaps = call_google_maps_positionnement(
        g_maps_key,
        msg_to_api_requests
        )
    wiki_title = call_wiki_main_page(msg_to_api_requests)
    history = call_wiki_found_page(wiki_title[1]
    if msg_gmaps[2] == IndexError:
        return {"messages": msg_gmaps}
    if wiki_title[1] == IndexError:
        return {"messages": wiki_title}
    if msg_gmaps[2] == KeyError:
        return {"messages": [
            "Ups je n'ai pas trouvé ce que tu me demandes,",
            "On vas devoir changer de conversation, tu veux?",
            "j'en connais un rayon, mais ça???",
            "Alors qu'est-ce que tu veux savoir, petit filou?"
        ]}
    else:
        try:
            message = {
                "messages": [
                            "Et donc tu veux savoir tout sur " +
                            wiki_title[0],
                            "Coquinou, quand même!" +
                            "Et bein oui c'est a : " + msg_gmaps[2],
                            "Pas bête la bête!" +
                            " Allez autre chose... Je te montre," +
                            " une image vaux mieux que 1000 mots!!!",
                            "Et a propos de ta demande et pour la petitte" +
                            " histoire :" + history
                            ],
                "position": msg_gmaps[1],
                "tag": wiki_title[0]
                }
            return message
        except TypeError:
            return {"messages": [
                "T'as pas hont de faire une blague a PAPY?",
                "A ton age!!",
                "Ups je n'ai pas trouvé ce que tu me demandes,",
                "On vas devoir changer de conversation, " +
                ".... Ha ces jeaunneaux...!!!"
            ]}

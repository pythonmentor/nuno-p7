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
    try:
        location = msg_gmaps["results"][0]["geometry"]["location"]
    except IndexError or KeyError:
        ups = {"messages": [
            "Desolé je n'ai pas pu t'aider mon petit...",
            "Ecris mieux tête de linotte!",
            " et tu sais? A mon age, on n'as pas toutte sa tête!",
            "Et redemandemoi-ce que tu veux, mais tu t'appliques ok?"
        ], "tag": "ups"
        }
        return ups
    else:
        adress = msg_gmaps["results"][0]["formatted_address"]

    wiki_title = call_wiki_main_page(msg_to_api_requests)
    try:
        processed_title = wiki_title["query"]["search"][0]["title"]
    except IndexError or KeyError:
        return {"messages ": [
            "Ups je n'ai pas trouvé ce que tu me demandes,",
            "On vas devoir changer de conversation, tu veux?",
            "J'ai bien cherché dans ma tête, mais rien!!",
            "je ne vopis pas de quoi tu veux parler.."
        ]}
    else:
        pageid = processed_title["query"]["search"][0]["pageid"]
        history = call_wiki_found_page(pageid)
        try:
            message = {
                "messages": [
                            "Et donc tu veux savoir tout sur " +
                            processed_title,
                            "Coquinou, quand même!" +
                            "Et bein oui c'est a : " + adress,
                            "Pas bête la bête!" +
                            " Allez autre chose... Je te montre," +
                            " une image vaux mieux que 1000 mots!!!",
                            "Et a propos de ta demande et pour la petitte" +
                            " histoire :" + history
                            ],
                "position": location,
                "tag": processed_title
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

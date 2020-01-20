from .first_input_parser import parse_user_input, important_words
from .interface_requests import (
    call_google_maps_positionnement,
    call_wiki_main_page,
    call_wiki_found_page
)


def grandPyWork(message, app):
    """
    Function, to prepare the answers and instace all API's once.
    """
    # Config options
    app.config.from_object('config')
    # To get one variable, tape app.config['MY_VARIABLE']
    g_maps_key = app.config["MAPS_API_KEY"]
    stop_words_custom = app.config['STOP_WORDS']
    words_to_remove = app.config['WORDS_TO_REMOVE']
    # Parse the input sentence
    parsed_msg = parse_user_input(message, stop_words_custom)
    msg_to_api_requests = important_words(parsed_msg, words_to_remove)
    # Request and test the Google Maps call
    msg_gmaps = call_google_maps_positionnement(
        g_maps_key,
        msg_to_api_requests
        )
    try:
        address = msg_gmaps["results"][0]["formatted_address"]
    except IndexError or KeyError:
        ups = {"messages": [
            "Desolé je n'ai pas pu t'aider mon petit...",
            "Écris mieux tête de linotte!",
            "Et tu sait? A mon age, on n'as pas toute sa tête!",
            "Et redemande moi-ce que tu veut, mais tu t'appliques ok?"
        ], "tag": "ups"
        }
        return ups
    else:
        location = msg_gmaps["results"][0]["geometry"]["location"]
    # call Wikipedia for a tittle and test il the parsed input is Ok
    wiki_title = call_wiki_main_page(msg_to_api_requests)
    try:
        processed_title = wiki_title["query"]["search"][0]["title"]
    except IndexError or KeyError:
        return {"messages ": [
            "Ups je n'ai pas trouvé ce que tu me demandes,",
            "On vas devoir changer de conversation, tu veux?",
            "J'ai bien cherché dans ma tête, mais rien!!",
            "je ne vois pas de quoi tu veux parler.."
        ]}
    else:
        pageid = wiki_title["query"]["search"][0]["pageid"]
        history = call_wiki_found_page(pageid)
        try:
            # Construction of the bot responses
            message = {
                "messages": [
                            "Et donc tu veux savoir tout sur " +
                            processed_title,
                            "Coquinou, quand même!" +
                            "Et bein oui c'est a : " + address,
                            "Pas bête la bête!" +
                            " Allez autre chose... Je te montre," +
                            " une image vaux mieux que 1000 mots!!!",
                            "Et a propos de ta demande et pour la petite" +
                            " histoire :" + history
                            ],
                "position": location,
                "tag": processed_title
                }
            return message
        except TypeError:
            return {"messages": [
                "T'as pas honte de faire une blague a PAPPY?",
                "A ton age!!",
                "Ups je n'ai pas trouvé ce que tu me demandes,",
                "On vas devoir changer de conversation, " +
                ".... Ha ces jetits jeunes...!!!"
            ]}

import requests

# Api Gmaps


def call_google_maps_positionnement(key, tittle):
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_payload = {"key": key, "query": tittle}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()

    try:
        place_id = search_json["results"][0]["place_id"]
        location = search_json["results"][0]["geometry"]["location"]
        adress = search_json["results"][0]["formatted_address"]

        return place_id, location, adress

    except IndexError:
        search_json = "Desolé je n'ai pas pu t'aider mon petit, peut-tu " + \
            "refaire ta demande autrement stp? Tu sais avec mon age..."
        return search_json

# Api Wikipedia


def call_wiki_main_page(title):
    """Call Api Wikipedia"""
    s = requests.Session()
    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": "{}".format(title)
        }
    r = s.get(url=url, params=params)
    data = r.json()

    try:
        processed_title = data["query"]["search"][0]["title"]
        pageid = data["query"]["search"][0]["pageid"]
        return processed_title, pageid

    except KeyError:
        return [
            "Ups je n'ai pas trouvé ce que tu me demandes,",
            "On vas devoir changer de conversation, tu veux?"
        ]
    except IndexError:
        return [
            "Ups je n'ai pas trouvé ce que tu me demandes,",
            "On vas devoir changer de conversation, tu veux?"
        ]


def call_wiki_found_page(pageid):
    s = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        'action': "query",
        'pageids': pageid,
        'format': "json",
        'prop': 'extracts',
        'explaintext': 1,
        'exsentences': 6,
    }
    r = s.get(url=url, params=params)
    data = r.json()

    text = data['query']['pages'][str(pageid)]['extract']
    return text

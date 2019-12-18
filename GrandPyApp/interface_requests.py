import requests

# Api Gmaps


def call_google_maps_positionnement(key, tittle):
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_payload = {"key": key, "query": tittle}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()

    place_id = search_json["results"][0]["place_id"]
    location = search_json["results"][0]["geometry"]["location"]
    adress = search_json["results"][0]["formatted_address"]

    return place_id, location, adress


def call_google_maps_details(key, place_id):
    details_url = "https://maps.googleapis.com/maps/api/place/details/json"
    details_payload = {"key": key, "placeid": place_id}
    details_resp = requests.get(details_url, params=details_payload)
    details_json = details_resp.json()

    url = details_json["result"]["url"]

    return url

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
    # incorporer if etc.. por repeter la requete en cas d'error
    processed_title = data["query"]["search"][0]["title"]
    pageid = data["query"]["search"][0]["pageid"]
    return processed_title, pageid


def call_wiki_found_page(pageid):
    s = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        'action': "query",
        'pageids': pageid,
        'format': "json",
        'prop': 'extracts',
        'explaintext': 1,
        'exsentences': 2,
    }
    r = s.get(url=url, params=params)
    data = r.json()

    text = data['query']['pages'][str(pageid)]['extract']
    return text

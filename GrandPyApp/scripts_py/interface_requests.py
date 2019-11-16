import sys
sys.path.append(".")
import requests
from GrandPyApp.views import app
import json
from pprint import pprint

app.config.from_object('config')
key = app.config["MAPS_API_KEY"]


def call_google_maps_positionnement(tittle):
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_payload = {"key": key, "query": tittle}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()

    with open('current_data.json', 'w') as fp:
        json.dump(search_json, fp)

    place_id = search_json["results"][0]["place_id"]
    location = search_json["results"][0]["geometry"]["location"]
    adress = search_json["results"][0]["formatted_address"]

    return place_id, location, adress


def call_google_maps_details(place_id):
    details_url = "https://maps.googleapis.com/maps/api/place/details/json"
    details_payload = {"key": key, "placeid": place_id}
    details_resp = requests.get(details_url, params=details_payload)
    details_json = details_resp.json()

    with open('current_page_data.json', 'w') as fp:
        json.dump(details_json, fp)

    url = details_json["result"]["url"]

    return url

# Api Wikipedia


def call_wiki_by_geocoordinates(coordinates):

    """
    Obtain wiki pages nearby coordinates

    """
    lat = coordinates['lat']
    lng = coordinates['lng']

    s = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "generator": "geosearch",
        "titles": "Wikimedia Foundation",
        "prop": "coordinates|pageimages",
        "ggscoord": "{}|{}". format(lat, lng)
        }

    r = s.get(url=url, params=params)
    data = r.json()
    with open('wiki_data.json', 'w') as fp:
        json.dump(data, fp)
    pages = data['query']['pages']

    return pages


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
    pprint(data)
    processed_title = data["query"]["search"][0]["title"]
    print(processed_title)
    return processed_title


def call_wiki_found_page(title):
    s = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        "titles": "{}".format(title),
        "action": "query",
        "prop": "extracts",
        "exsentences": "3",
        "format": "json",
        "explaintext": "explaintext",
        "exlimit": "max",
        "exintro": "exintro"
    }
    r = s.get(url=url, params=params)
    data = r.json()

    pprint(data)
    return data


if __name__ == "__main__":
    """call_google_maps_positionnement("openclassrooms")
    place_id = "ChIJIZX8lhRu5kcRGwYk8Ce3Vc8"
    call_google_maps_details(place_id)"""
    coordinates = {'lat': 48.8748465, 'lng': 2.3504873}
    call_wiki_by_geocoordinates(coordinates)
    call_wiki_main_page("openclassrooms")
    call_wiki_found_page("openclassrooms")

import requests
from ..views import app

key = app.config.from_object('MAPS_API_KEY')


def call_google_maps_positionnement(tittle):
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    search_payload = {"key": key, "query": tittle}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()

    place_id = search_json["results"][0]["place_id"]
    location = search_json["results"][0]["location"]
    adress = search_json["results"][0]["formatted_address"]

    print(location)
    print(adress)
    return place_id, location, adress


def call_google_maps_details(place_id):
    details_url = "https://maps.googleapis.com/maps/api/place/details/json"
    details_payload = {"key": key, "placeid": place_id}
    details_resp = requests.get(details_url, params=details_payload)
    details_json = details_resp.json()

    url = details_json["result"]["url"]

    return url


def call_wiki_by_geocoordinates(coordinates):

    """
    Obtain wiki pages nearby coordinates

    """

    s = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "generator": "geosearch",
        "titles": "Wikimedia Foundation",
        "prop": "coordinates|pageimages",
        "ggscoord": """coordinates[0] | coordinates[1]"""}

    r = s.get(url=url, params=params)
    data = r.json()
    pages = data['query']['pages']


if __name__ == "__main__":
    call_google_maps_positionnement("openclassrooms")

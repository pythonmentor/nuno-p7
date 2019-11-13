import requests


def call_wiki_by_geocoordinates(coordinates):

    """
    Obtain coordinates for wiki pages nearby

    """

    s = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "generator": "geosearch",
        "titles": "Wikimedia Foundation",
        "prop": "coordinates|pageimages",
        "ggscoord": # coordinates[0] | coordinates[1]
    }
    r = s.get(url=url, params=params)
    data = r.json()
    pages = data['query']['pages']

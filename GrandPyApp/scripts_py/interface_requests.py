import requests
import json
from pprint import pprint


def call_wiki_title(parsed_user_title):
    """Call Api Wikipedia"""
    # first call all main page
    url_begin = "https://fr.wikipedia.org/w/api.php?action=query&format=json&list=search&srwhat=text&srsearch="
    url_title = parsed_user_title
    url = "{}{}".format(url_begin, url_title)
    # and we took the first occurrence
    r = requests.get(url)
    print(r.content)
    result_wiki_title = json.loads(r.content)
    pprint(result_wiki_title)
    try:
        title = result_wiki_title["query"]["search"][0]["title"]
    except IndexError:
        title = "Openclassrooms"  # in case of invalid user input
    return title


def call_wiki_page(title):
    # format url
    url_begin = "https://fr.wikipedia.org/w/api.php?action=query&titles="
    url_title = title
    url_end = "&prop=extracts&exsentences=3&format=json&explaintext&exlimit=max&exintro"
    url = "{}{}{}".format(url_begin, url_title, url_end)

    # call api
    r = requests.get(url)
    result_wiki_text = json.loads(r.content)
    return result_wiki_text


def get_from_google_maps():
    pass

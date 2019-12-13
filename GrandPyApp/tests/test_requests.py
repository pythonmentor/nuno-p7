from ..interface_requests import (
  call_google_maps_details,
  call_google_maps_positionnement,
  call_wiki_found_page, call_wiki_main_page
  )
from ..views import app
import urllib.request
from io import BytesIO
import json

key = app.config["MAPS_API_KEY"]


def test_call_google_maps(monkeypatch):
    with open("GrandPyApp/tests/gmaps_data.json") as g_maps_data:
      results_test = json.load(g_maps_data)

    def mockreturn(request):
        return BytesIO(json.dumps(results_test).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    place_id_test = results_test["results"][0]["place_id"]
    location_test = results_test["results"][0]["geometry"]["location"]
    adress_test = results_test["results"][0]["formatted_address"]

    assert call_google_maps_positionnement(
      key,
      "openclassrooms")[0] == place_id_test
    assert call_google_maps_positionnement(
      key,
      "openclassrooms")[1] == location_test
    assert call_google_maps_positionnement(
      key,
      "openclassrooms")[2] == adress_test


def test_call_google_maps_details(monkeypatch):
    with open("GrandPyApp/tests/current_gmaps_page_data_for_url.json") as g_maps_url_data:
      results_test = json.load(g_maps_url_data)

    def mockreturn(request):
        return BytesIO(json.dumps(results_test).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    url = results_test["result"]["url"]
    place_id = call_google_maps_positionnement(
      key,
      "openclassrooms")[0]

    assert call_google_maps_details(key, place_id) == url


def test_call_wiki_main_page(monkeypatch):
    with open("GrandPyApp/tests/wiki_tittle_main_page.json") as wiki_tittle_data:
      results_test = json.load(wiki_tittle_data)

    def mockreturn(request):
        return BytesIO(json.dumps(results_test).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    processed_title = results_test["query"]["search"][0]["title"]
    pageid = results_test["query"]["search"][0]["pageid"]

    assert call_wiki_main_page(
      "openclassrooms")[0] == processed_title
    assert call_wiki_main_page(
      "openclassrooms")[1] == pageid


def test_call_wiki_found_page(monkeypatch):
    with open("GrandPyApp/tests/wiki_found_page.json") as wiki_found_data:
      results_test = json.load(wiki_found_data)

    def mockreturn(request):
        return BytesIO(json.dumps(results_test).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    pageid = call_wiki_main_page(
      "openclassrooms")[1]
    text = results_test['query']['pages'][str(pageid)]['extract']

    assert call_wiki_found_page(pageid) == text

import os
from GrandPyApp import interface_requests as ir
import json

"""
For test all API's you need a Google DEV Key,
For security reasons i have hide in a Py secret file.
Here you must put Yours DEV Google key
"""

key = os.environ["API_PASSWORD"]


def test_call_google_maps(monkeypatch):
    with open("tests/gmaps_data.json") as g_maps_data:
        results_test = json.load(g_maps_data)

    class MockResponse:
        def read(self):
            result_strings = json.dumps(results_test)
            result_bytes = result_strings.encode()
            return result_bytes

    def mock_g_maps(url):
        return MockResponse()

    monkeypatch.setattr(
      "GrandPyApp.interface_requests.call_google_maps_positionnement",
      mock_g_maps
      )

    place_id_test = results_test["results"][0]["place_id"]
    location_test = results_test["results"][0]["geometry"]["location"]
    adress_test = results_test["results"][0]["formatted_address"]

    assert ir.call_google_maps_positionnement(
      key,
      "openclassrooms")[0] == place_id_test
    assert ir.call_google_maps_positionnement(
      key,
      "openclassrooms")[1] == location_test
    assert ir.call_google_maps_positionnement(
      key,
      "openclassrooms")[2] == adress_test
    assert ir.call_google_maps_positionnement(
      key,
      "") == "Desolé je n'ai pas pu t'aider mon petit, peut-tu " + \
        "refaire ta demande autrement stp? Tu sais avec mon age..."


def test_call_wiki_main_page(monkeypatch):
    with open("tests/wiki_tittle_main_page.json") as wiki_tittle_data:
        results_test = json.load(wiki_tittle_data)

    class MockResponse:
        def read(self):
            result_strings = json.dumps(results_test)
            result_bytes = result_strings.encode()
            return result_bytes

    def mock_call_wiki_main_page(url):
        return MockResponse()

    monkeypatch.setattr(
      "GrandPyApp.interface_requests.call_wiki_main_page",
      mock_call_wiki_main_page
      )

    processed_title = results_test["query"]["search"][0]["title"]
    pageid = results_test["query"]["search"][0]["pageid"]

    assert ir.call_wiki_main_page(
      "openclassrooms")[0] == processed_title
    assert ir.call_wiki_main_page(
      "openclassrooms")[1] == pageid


def test_call_wiki_found_page(monkeypatch):
    with open("tests/wiki_found_page.json") as wiki_found_data:
        results_test = json.load(wiki_found_data)

    class MockResponse:
        def read(self):
            result_strings = json.dumps(results_test)
            result_bytes = result_strings.encode()
            return result_bytes

    def mock_call_wiki_found_page(url):
        return MockResponse()

    monkeypatch.setattr(
      "GrandPyApp.interface_requests.call_wiki_found_page",
      mock_call_wiki_found_page
      )

    pageid = ir.call_wiki_main_page(
      "openclassrooms")[1]
    text = results_test['query']['pages'][str(pageid)]['extract']

    assert ir.call_wiki_found_page(pageid) == text

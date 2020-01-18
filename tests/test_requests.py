from GrandPyApp.interface_requests import (
  call_google_maps_positionnement,
  call_wiki_main_page,
  call_wiki_found_page
)
from .config import API_PASSWORD
import json

"""
For test all API's you need a Google DEV Key,
For security reasons i have hide in a Py secret file.
Here you must put Yours DEV Google key
"""

key = API_PASSWORD


def test_call_google_maps(monkeypatch):
    with open("gmaps_data.json") as g_maps_data:
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
    assert call_google_maps_positionnement(
      key, "openclassrooms") == results_test


results_call_wiki_main_page = call_wiki_main_page(
      "openclassrooms")
with open("wiki_tittle_main_page.json", "w") as f_write:
    json.dump(results_call_wiki_main_page, f_write)


def test_call_wiki_main_page(monkeypatch):
    with open("wiki_tittle_main_page.json") as wiki_tittle_data:
        results_call_wiki_main_page = json.load(wiki_tittle_data)

    class MockResponse:
        def read(self):
            result_strings = json.dumps(results_call_wiki_main_page)
            result_bytes = result_strings.encode()
            return result_bytes

    def mock_call_wiki_main_page(url):
        return MockResponse()

    monkeypatch.setattr(
      "GrandPyApp.interface_requests.call_wiki_main_page",
      mock_call_wiki_main_page
      )

    assert call_wiki_main_page("openclassrooms") == results_call_wiki_main_page


def test_call_wiki_found_page(monkeypatch):
    with open("wiki_found_page.json") as wiki_found_data:
        results_call_wiki_found_page = json.load(wiki_found_data)

    class MockResponse:
        def read(self):
            result_strings = json.dumps(results_call_wiki_found_page)
            result_bytes = result_strings.encode()
            return result_bytes

    def mock_call_wiki_found_page(url):
        return MockResponse()

    monkeypatch.setattr(
      "GrandPyApp.interface_requests.call_wiki_found_page",
      mock_call_wiki_found_page
      )

    data = call_wiki_main_page("openclassrooms")
    pageid = data["query"]["search"][0]["pageid"]

    assert call_wiki_found_page(pageid) == results_call_wiki_found_page

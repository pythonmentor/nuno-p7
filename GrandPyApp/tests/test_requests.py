from ..interface_requests import (
  call_google_maps_details,
  call_google_maps_positionnement,
  call_wiki_by_geocoordinates,
  call_wiki_found_page, call_wiki_main_page
  )
import urllib.request
from io import BytesIO
import json


def test_call_google_maps(monkeypatch):
    results_test = {
      'html_attributions': [],
      'results': [
        {
          'formatted_address': '7 Cité Paradis, 75010 Paris, France',
          'geometry': {
            'location': {'lat': 48.8748465, 'lng': 2.3504873},
            'viewport': {'northeast': {
              'lat': 48.87622362989272,
              'lng': 2.351843679892722},
                          'southwest': {
                            'lat': 48.87352397010727,
                            'lng': 2.349144020107278}}},
          'icon': 'https://maps.gstatic.com/mapfiles/place_api/\
            icons/generic_business-71.png',
          'id': 'dd80dc7de1802674cba35cce4e303e6862a4f3ed',
          'name': 'Openclassrooms',
          'opening_hours': {'open_now': False},
          'photos': [{'height': 385,
                          'html_attributions': ['<a '
                                                'href="https://maps.google.com/maps/contrib/110718279865691618892/\
                                                  photos">Openclassrooms</a>'],
                          'photo_reference': 'CmRaAAAA6W3YUxObWTJeoPpFWPqSLV5rmctanDg8pM6NZZiIVwvz5Pvk3xCMvXuA0HLMtCpH7YQo\
                            mRPpzh8iVkONgPps9tIi9kXm88oKLs2hlN7DzmBchLwm6EMgxtmHZH7QHrjZEhC5J1SEKFvmEtTKUtyVrXyZG\
                              hS6nFgV7g4ddr6uTLZYJqJRdktE4g',
                          'width': 385}],
          'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8',
          'plus_code': {'compound_code': 'V9F2+W5 Paris',
                        'global_code': '8FW4V9F2+W5'},
          'rating': 3.3,
          'reference': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8',
          'types': ['point_of_interest', 'establishment'],
          'user_ratings_total': 25}],
      'status': 'OK'}

    def mockreturn(request):
        return BytesIO(json.dumps(results_test).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    place_id_test = results_test["results"][0]["place_id"]
    location_test = results_test["results"][0]["geometry"]["location"]
    adress_test = results_test["results"][0]["formatted_address"]

    assert call_google_maps_positionnement(
      "openclassrooms")[0] == place_id_test
    assert call_google_maps_positionnement(
      "openclassrooms")[1] == location_test
    assert call_google_maps_positionnement(
      "openclassrooms")[2] == adress_test


def test_call_google_maps_details():
  pass


def test_call_wiki_by_gecoodinates():
  pass


def test_call_wiki_main_page():
  pass


def test_call_wiki_found_page():
  pass

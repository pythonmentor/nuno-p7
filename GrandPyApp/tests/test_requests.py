from ..scripts_py import interface_requests as req
import urllib.request
from io import BytesIO
import json


def test_call_google_maps(monkeypatch):
    results = [{
            "age": 84,
            "agreeableness": 0.74
          }
        ]
    
    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    assert 

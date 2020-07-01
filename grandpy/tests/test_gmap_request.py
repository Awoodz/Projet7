import requests
import requests_mock

from grandpy.api.gmap_request import Gmap

class MockResponse():

    @staticmethod
    def json():
        return {"mock": "fake"}


def test_does_gmap_class_makes_requests(monkeypatch):

    def mock_request(mock):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_request)

    mock_result = Gmap.google_map_request("mock1", "mock2")
    print(mock_result)
    assert mock_result["mock"] == "fake"

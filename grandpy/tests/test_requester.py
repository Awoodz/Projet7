from grandpy.api.gmap_request import Gmap
from grandpy.api.requester import Requester
from grandpy.api.wiki_request import Wiki


def test_does_words_removal_remove_first_words_of_string():
    test_text = "one two"
    test_response = Requester.words_removal(test_text)
    assert test_response == "two "


def mock_invalid_google_request(text, mock):
    return {"test_status": "INVALID_REQUEST"}


def mock_wiki_request(mock1, mock2):
    return "story"


def test_request_return_response_if_google_status_is_invalid(monkeypatch):
    monkeypatch.setattr(
        Gmap,
        "google_map_request",
        mock_invalid_google_request
    )

    monkeypatch.setattr("grandpy.utilities.data.API_MAP_STATUS", "test_status")
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_CND",
        "test_candidates"
    )
    assert Requester.request_engine("self", "fake_txt") == {
        "test_candidates": 0
    }


def mock_valid_google_request(text, mock):
    return {"test_status": "OK", "test_state": "yay!"}


def test_request_return_response_if_google_status_is_valid(monkeypatch):
    monkeypatch.setattr(Gmap, "google_map_request", mock_valid_google_request)
    monkeypatch.setattr(Wiki, "wiki_request", mock_wiki_request)
    monkeypatch.setattr("grandpy.utilities.data.API_MAP_STATUS", "test_status")
    assert Requester.request_engine("self", "fake_txt") == {
        "gmap": {"test_status": "OK", "test_state": "yay!"},
        "wiki": "story",
    }

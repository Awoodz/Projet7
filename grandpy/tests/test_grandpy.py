from grandpy.api.place import Place
from grandpy.api.requester import Requester
from grandpy.utilities import helpers
from grandpy.utilities.grandpy import Grandpy
from grandpy.utilities.parser import Parser


class Mock_place:
    def __init__(self, mock1, mock2):
        pass

    @property
    def name(self):
        return "fake_name"

    @property
    def adress(self):
        return "fake_adress"

    @property
    def lat(self):
        return "fake_lat"

    @property
    def lng(self):
        return "fake_lng"

    @property
    def story(self):
        return "this is a fake story"


class Mock_parser:
    def __init__(self, form_input):
        self.request = "request"


class Mock_requester:
    def __init__(self, parsed_txt):
        self.placedata = {"gmap": "gmapdata", "wiki": "wikidata"}


def mock_randomisator(mock1):
    return "!"


def test_does_grandpy_get_every_datas(monkeypatch):
    monkeypatch.setattr(Parser, "__init__", Mock_parser.__init__)
    monkeypatch.setattr(Requester, "__init__", Mock_requester.__init__)
    monkeypatch.setattr(Place, "__init__", Mock_place.__init__)
    monkeypatch.setattr(Place, "name", Mock_place.name)
    monkeypatch.setattr(Place, "adress", Mock_place.adress)
    monkeypatch.setattr(Place, "lat", Mock_place.lat)
    monkeypatch.setattr(Place, "lng", Mock_place.lng)
    monkeypatch.setattr(Place, "story", Mock_place.story)
    monkeypatch.setattr(helpers, "randomisator", mock_randomisator)

    usertest = Grandpy("mock1")

    assert usertest.name == "fake_name"
    assert usertest.adress == "!fake_adress"
    assert usertest.lat == "fake_lat"
    assert usertest.lng == "fake_lng"
    assert usertest.story == "!this is a fake story"

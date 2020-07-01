from grandpy.utilities.grandpy import Grandpy
from grandpy.utilities.parser import Parser
from grandpy.api.requester import Requester
from grandpy.api.place import Place
from grandpy.api.story import Story
from grandpy.utilities import helpers


class Mock_place():

    def __init__(self, gmap_json):
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


class Mock_story():

    def __init__(self, gmap_json):
        self.story = "this is a fake story"

    @property
    def story(self):
        return "this is a fake story"


class Mock_parser():

    def __init__(self, form_input):
        self.request = "request"

    def request(self):
        return "request"


class Mock_requester():

    def __init__(self, parsed_txt):
        self.placedata = "placedata"

    @property
    def placedata(self):
        return "placedata"


def mock_randomisator(mock1):
    return "!"


def test_does_grandpy_get_every_datas(monkeypatch):
    monkeypatch.setattr(Parser, "__init__", Mock_parser.__init__)
    monkeypatch.setattr(Parser, "parse", Mock_parser.request)
    monkeypatch.setattr(Requester, "__init__", Mock_requester.__init__)
    monkeypatch.setattr(Requester, "request_engine", Mock_requester.placedata)
    monkeypatch.setattr(Place, "__init__", Mock_place.__init__)
    monkeypatch.setattr(Place, "name", Mock_place.name)
    monkeypatch.setattr(Place, "adress", Mock_place.adress)
    monkeypatch.setattr(Place, "lat", Mock_place.lat)
    monkeypatch.setattr(Place, "lng", Mock_place.lng)
    monkeypatch.setattr(Story, "__init__", Mock_story.__init__)
    monkeypatch.setattr(Story, "wiki_request", Mock_story.story)
    monkeypatch.setattr(helpers, "randomisator", mock_randomisator)

    usertest = Grandpy("mock1")

    assert usertest.name == "fake_name"
    assert usertest.adress == "!fake_adress"
    assert usertest.lat == "fake_lat"
    assert usertest.lng == "fake_lng"
    assert usertest.story == "!this is a fake story"

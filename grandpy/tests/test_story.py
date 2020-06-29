from grandpy.api.story import Story
from grandpy.api.place import Place


def mock_wiki(self, name, language):
    return "this is a story"


class Mock_place():

    def __init__(self, gmap_json):
        pass

    @property
    def name(self):
        return "test"


def test_does_story_class_get_name_from_place_class(monkeypatch):
    monkeypatch.setattr(Place, "__init__", Mock_place.__init__)
    monkeypatch.setattr(Place, "name", Mock_place.name)
    monkeypatch.setattr(Story, "wiki_request", mock_wiki)
    usertest = Story("mock1", "mock2")
    assert usertest.place == "test"


def test_does_story_class_get_story_from_wikipedia(monkeypatch):
    monkeypatch.setattr(Place, "__init__", Mock_place.__init__)
    monkeypatch.setattr(Place, "name", Mock_place.name)
    monkeypatch.setattr(Story, "wiki_request", mock_wiki)
    usertest = Story("mock1", "mock2")
    assert usertest.story == "this is a story"

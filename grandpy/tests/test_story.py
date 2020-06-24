from grandpy.class_file.story import Story
from grandpy.class_file.place import Place




def mock_wiki(self, name, language):
    pass


def test_name(monkeypatch):
    
    class Mock_place():

        def __init__(self, gmap_json):
            pass

        def get_place_data(self):
            pass

        @property
        def name(self):
            return "test"

    monkeypatch.setattr(Place, "__init__", Mock_place.__init__)
    monkeypatch.setattr(Place, "get_place_data", Mock_place.get_place_data)
    monkeypatch.setattr(Place, "name", Mock_place.name)
    monkeypatch.setattr(Story, "wiki_request", mock_wiki)
    usertest = Story("mock1", "mock2")
    assert usertest.place == "test"

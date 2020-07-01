from grandpy.api.wiki_request import Wiki


def mock_wiki(self, name):
    return "this is a story"


def test_does_wiki_class_get_story_from_wikipedia(monkeypatch):
    monkeypatch.setattr(Wiki, "wiki_request", mock_wiki)
    usertest = Wiki("mock1")
    assert usertest.story == "this is a story"

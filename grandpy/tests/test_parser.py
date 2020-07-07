from grandpy.utilities.parser import Parser
from grandpy.utilities import helpers


def mock_stop_words(mock1, mock2):
    return ["sure", "to", "be", "the"]


def mock_punctuation(mock1):
    return ["!"]


def test_does_parser_remove_stop_words(monkeypatch):
    monkeypatch.setattr(helpers, "stop_words", mock_stop_words)
    monkeypatch.setattr(helpers, "punctuation", mock_punctuation)
    text_to_parse = "I am sure to be the number one !"
    parser_test = Parser(text_to_parse)
    assert parser_test.request == ("i am number one")

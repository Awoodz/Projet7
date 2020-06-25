from grandpy.utilities.parser import Parser


def mock_stopwords():
    return ["hello", "sure", "to", "be"]


def mock_punctuation():
    return [",", "!"]


def test_does_parser_remove_stop_words():
    text_to_parse = (
        "Hello, I am sure to be number one !"
    )
    parser_test = Parser(text_to_parse, mock_stopwords(), mock_punctuation())
    assert parser_test.request == (
        "i am number one"
    )

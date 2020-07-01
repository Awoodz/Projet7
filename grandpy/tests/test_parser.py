from grandpy.utilities.parser import Parser


def test_does_parser_remove_stop_words():
    text_to_parse = "Salut grandpy ! Est-ce que tu connais l'adresse ?"
    parser_test = Parser(text_to_parse)
    assert parser_test.request == ("salut connais adresse")

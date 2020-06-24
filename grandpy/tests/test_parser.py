from stop_words import get_stop_words
import string

import grandpy.data as dt
import grandpy.helpers as hp
from grandpy.class_file.parser import Parser


def test_does_parser_remove_stop_words():
    text_to_parse = (
        "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    )
    stopwords = hp.stop_words(
        get_stop_words(dt.BOT_LANGUAGE),
        dt.SPECIAL_STOP_WORDS
    )
    punctuation = hp.punctuation(string.punctuation)
    parser_test = Parser(text_to_parse, stopwords, punctuation)
    assert parser_test.request == (
        "salut connais adresse openclassrooms"
    )

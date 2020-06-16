from stop_words import get_stop_words
import string

import grandpy.class_file.human as hu
import grandpy.class_file.bot as bt
import grandpy.data as dt
import grandpy.helpers as hp
import grandpy.app as app

# Class Human
# Send a request


def test_send_request():
    form_input = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    user = hu.Human(form_input)
    assert user.request == "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"

# Parse a request


def test_parse_request():
    form_input = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    stopwords = hp.stop_words(
        get_stop_words(dt.BOT_LANGUAGE),
        dt.SPECIAL_STOP_WORDS
    )
    punctuation = hp.punctuation(string.punctuation)
    user = hu.Human(form_input)
    assert user.parse(stopwords, punctuation) == "salut connais adresse openclassrooms"


# Give an answer for request


def test_give_answer():
    grandpy = bt.Bot("answer", "story")
    assert grandpy.answer == "answer"


# Tell a story


def test_tell_story():
    grandpy = bt.Bot("anwser", "story")
    assert grandpy.tell_story == "story"


def test_google_map_request(monkeypatch):
    response = {
        'name': 'OpenClassrooms',
        'adress': '7 Cité Paradis, 75010 Paris, France',
        'lat': 48.8748465,
        'lng': 2.3504873,
        'story': 'bonjour'
    }

    def mockreturn(request):
        return response

    assert app.get_request("Openclassrooms") == response

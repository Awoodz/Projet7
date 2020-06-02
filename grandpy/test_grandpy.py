from stop_words import get_stop_words
import string

import grandpy.class_grandpy as cg
import grandpy.data as dt
import grandpy.helpers as hp

# Class Human
# Send a request
def test_send_request():
    form_input = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    user = cg.Human(form_input)
    assert user.request == "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
# Parse a request
def test_parse_request():
    form_input = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    stopwords = hp.stop_words(
        get_stop_words(dt.BOT_LANGUAGE),
        dt.SPECIAL_STOP_WORDS
    )
    punctuation = hp.punctuation(string.punctuation)
    user = cg.Human(form_input)
    assert user.parse(stopwords, punctuation) == "adresse openclassrooms"

# Class Place
# Get latitude
def test_get_latitude():
    site = cg.Place("name", "adress", 50, 100, "story")
    assert site.latitude == 100

# Get longitude
def test_get_longitude():
    site = cg.Place("name", "adress", 50, 100, "story")
    assert site.longitude == 50
# Get adress
def test_get_adress():
    site = cg.Place("name", "adress", 50, 100, "story")
    assert site.adress == "adress"
# Get name
def test_get_name():
    site = cg.Place("name", "adress", 50, 100, "story")
    assert site.name == "name"
# Get informations about a place
def test_get_story():
    site = cg.Place("name", "adress", 50, 100, "story")
    assert site.story == "story"

# Bot
# Give an answer for request
def test_give_answer():
    grandpy = cg.Bot("answer", "story")
    assert grandpy.answer == "answer"
# Tell a story
def test_tell_story():
    grandpy = cg.Bot("anwser", "story")
    assert grandpy.tell_story == "story"

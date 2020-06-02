import grandpy.class_grandpy as cg

# Class Human
# Send a request
def test_send_request():
    form_input = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    user = cg.Human(form_input)
    assert user.request == "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
# Parse a request
def test_parse_request():
    form_input = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    user = cg.Human(form_input)
    assert user.parse() == "adresse Openclassrooms"

# Class Place
# Get latitude
def test_get_latitude():
    site = cg.Place("name", "adress", 100, 50, "story")
    assert site.latitude == 100

# Get longitude
def test_get_longitude():
    site = cg.Place("name", "adress", 100, 50, "story")
    assert site.latitude == 50
# Get adress
def test_get_adress():
    site = cg.Place("name", "adress", 100, 50, "story")
    assert site.adress == "adress"
# Get name
def test_get_name():
    site = cg.Place("name", "adress", 100, 50, "story")
    assert site.adress == "name"
# Get informations about a place
def test_get_story():
    site = cg.Place("name", "adress", 100, 50, "story")
    assert site.adress == "story"

# Bot
# Give an answer for request
def test_give_answer():
    grandpy = cg.Bot("anwser", "story")
    assert grandpy.answer == "answer"
# Tell a story
def test_tell_story():
    grandpy = cg.Bot("anwser", "story")
    assert grandpy.tell_story == "story"

import grandpy.class_grandpy as cg

# Class Human
# Send a request
def test_send_request():
    form_input = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    user = cg.Human(form_input)
    assert user.request == "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
# Parse a request
def test_parse_request():
    user.request = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    assert user.parse == "adresse Openclassrooms"

# Class Place
# Get latitude
def test_get_latitude():
    site = Place()
# Get longitude
# Get adress
# Get name
# Get informations about a place

# Bot
# Give an answer for request
# Tell a story

class Bot():
    """Docstrings"""

    def __init__(self, answer, tell_story):
        self.answer = answer
        self.tell_story = tell_story


class Place():
    """Docstrings"""

    def __init__(self, name, adress, longitude, latitude, story):
        self.name = name
        self.adress = adress
        self.longitude = longitude
        self.latitude = latitude
        self.story = story


class Human():
    """Docstrings"""

    def __init__(self, form_input):
        self.request = form_input
    
    # def parse():

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
    
    def parse(self, stop_words, punctuation):

        request = self.request.lower()
        
        for elem in punctuation:
            request = request.replace(elem, " ")

        parsed_request = request.split()

        for words in stop_words:
            for elem in parsed_request:
                if elem == words:
                    parsed_request.remove(elem)
        return (" ".join(parsed_request))

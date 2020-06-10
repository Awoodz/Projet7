import grandpy.data as dt


class Bot():
    """Docstrings"""

    def __init__(self, answer, tell_story):
        self.answer = answer
        self.tell_story = tell_story


class Place():
    """Docstrings"""

    def __init__(self, gmap_json, story):
        self.name = gmap_json[dt.API_MAP_NAME]
        self.adress = gmap_json[dt.API_MAP_ADRESS]
        self.longitude = gmap_json[dt.API_MAP_GEO][dt.API_MAP_LOC][dt.API_MAP_LNG]
        self.latitude = gmap_json[dt.API_MAP_GEO][dt.API_MAP_LOC][dt.API_MAP_LAT]
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

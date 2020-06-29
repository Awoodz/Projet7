import wikipedia

from grandpy.api.place import Place
import grandpy.utilities.data as dt


class Story():
    """Gather story data"""

    def __init__(self, gmap_json):
        self.place = Place(gmap_json).name
        self.story = self.wiki_request(self.place)

    def wiki_request(self, name):
        """Get a short story using wikipedia module"""
        # Set wikipedia language
        wikipedia.set_lang(dt.WIKI_LANGUAGE)
        # Request first sentence of wikipedia summary
        story = wikipedia.summary(name, sentences=dt.SENT_NB)
        # Return that sentence
        return story

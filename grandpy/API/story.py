import wikipedia

from grandpy.api.place import Place
import grandpy.utilities.data as dt


class Story():
    """Gather story data"""

    def __init__(self, gmap_json, language):
        self.place = Place(gmap_json).name
        self.story = self.wiki_request(self.place, language)

    def wiki_request(self, name, language):
        """Get a short story using wikipedia module"""
        # Set wikipedia language
        wikipedia.set_lang(language)
        # Request first sentence of wikipedia summary
        story = wikipedia.summary(name, sentences=dt.SENT_NB)
        # Return that sentence
        return story

import wikipedia
import grandpy.class_file.place as pl
import grandpy.data as dt


class Story():
    """Gather story data"""

    def __init__(self, gmap_json, language):
        self.place = pl.Place(gmap_json)
        name = self.place.name
        self.story = self._wiki_request(name, language)

    def _wiki_request(self, name, language):
        """Get a short story using wikipedia module"""
        # Set wikipedia language
        wikipedia.set_lang(language)
        # Request first sentence of wikipedia summary
        story = wikipedia.summary(name, sentences=dt.SENT_NB)
        # Return that sentence
        return story

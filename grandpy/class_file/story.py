import wikipedia
import grandpy.class_file.place as pl


class Story():
    """Docstrings"""

    def __init__(self, gmap_json, language):
        self.place = pl.Place(gmap_json)
        name = self.place.name
        self.story = self.wiki_request(name, language)

    def wiki_request(self, name, language):
        """Docstrings"""
        wikipedia.set_lang(language)
        story = wikipedia.summary(name, sentences=1)
        return story

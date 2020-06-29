import wikipedia

import grandpy.utilities.data as dt


class Wiki():
    """Docstrings"""

    def wiki_request(name):
        """Get a short story using wikipedia module"""
        # Set wikipedia language
        wikipedia.set_lang(dt.WIKI_LANGUAGE)
        # Request first sentence of wikipedia summary
        story = wikipedia.summary(name, sentences=dt.SENT_NB)
        # Return that sentence
        return story

import wikipedia

import grandpy.utilities.data as dt


class Wiki:
    """Contains all that concerns Wikipedia request"""

    def __init__(self, name):
        self.story = self.wiki_request(name)

    def wiki_request(self, name):
        """Get a short story using wikipedia module"""
        try:
            # Set wikipedia language
            wikipedia.set_lang(dt.WIKI_LANGUAGE)
            # Request first sentence of wikipedia summary
            story = wikipedia.summary(name, sentences=dt.SENT_NB)
            # Return that sentence
            return story

        except (
            wikipedia.exceptions.PageError,
            wikipedia.exceptions.WikipediaException
        ) as error:
            print(error)
            return "fail"

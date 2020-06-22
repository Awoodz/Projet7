from stop_words import get_stop_words
import string

import grandpy.class_file.grandpy as gp
import grandpy.data as dt
import grandpy.helpers as hp
import config as cg


def get_request(user_input):
    """Treats user's request"""

    # Set the main stop words list
    stopwords = hp.stop_words(
        get_stop_words(dt.BOT_LANGUAGE),
        dt.SPECIAL_STOP_WORDS
    )
    # Set the punctuation list
    punctuation = hp.punctuation(string.punctuation)

    try:
        # Initialize Grandpy class
        grandpy = gp.Grandpy(
            dt.WIKI_LANGUAGE,
            cg.GMAP_API_KEY,
            user_input,
            stopwords,
            punctuation
        )

        # If successul, return gathered data as json
        return {
            "name": grandpy.name,
            "adress":
                hp.randomisator(dt.GRANDPY_PLACE) +
                grandpy.adress,
            "lat": grandpy.lat,
            "lng": grandpy.lng,
            "story":
                hp.randomisator(dt.GRANDPY_STORY) +
                grandpy.story
        }

    except (IndexError, TypeError) as error:
        print(error)
        # If failed, return lame excuses as json !
        return {
            "adress": hp.randomisator(dt.GRANDPY_PLACE_ERROR),
            "story": hp.randomisator(dt.GRANDPY_STORY_ERROR)
        }

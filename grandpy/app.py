<<<<<<< HEAD
from stop_words import get_stop_words
import string

import grandpy.class_file.grandpy as gp
import grandpy.data as dt
import grandpy.helpers as hp
import config as cg
=======
import grandpy.utilities.data as dt
import grandpy.utilities.helpers as hp
from grandpy.utilities.grandpy import Grandpy
>>>>>>> 588d1c918ba9417293e25c572ab5bf7530edf0fd


def get_request(user_input):
    """Treats user's request"""

    try:
        # Initialize Grandpy class
        grandpy = Grandpy(user_input)

        # If successul, return gathered data as json
        return {
            "name": grandpy.name,
            "adress": grandpy.adress,
            "lat": grandpy.lat,
            "lng": grandpy.lng,
            "story": grandpy.story,
        }

    except (IndexError, TypeError) as error:
        print(error)
        # If failed, return lame excuses as json !
        return {
            "adress": hp.randomisator(dt.GRANDPY_PLACE_ERROR),
            "story": hp.randomisator(dt.GRANDPY_STORY_ERROR),
        }

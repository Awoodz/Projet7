import grandpy.utilities.data as dt
import grandpy.utilities.helpers as hp
from grandpy.utilities.grandpy import Grandpy


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

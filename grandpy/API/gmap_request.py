import requests

import grandpy.utilities.data as dt
from config import GMAP_API_KEY


class Gmap():
    """Docstrings"""

    def google_map_request(request_txt):
        """Makes requests to Google Map API"""
        # Creates variables to create an url string in request
        input_key = (dt.INPUT_KEY + request_txt)
        inputtype = (dt.INPUT_TYPE)
        api_key = (dt.INPUT_API_KEY + GMAP_API_KEY)

        # Makes the request
        gmap_req = requests.get(
            dt.REQUEST_GMAP_URL +
            input_key +
            inputtype +
            api_key
        )
        return gmap_req.json()

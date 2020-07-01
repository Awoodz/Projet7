import requests

import grandpy.utilities.data as dt
from config import GMAP_API_KEY


class Gmap:
    """Docstrings"""

    def __init__(self, request_txt):
        self.req_result = self.google_map_request(request_txt)

    def google_map_request(self, request_txt):
        """Makes requests to Google Map API"""
        # Creates variables to create an url string in request
        url = [
            dt.REQUEST_GMAP_URL,
            dt.INPUT_KEY + request_txt,
            dt.INPUT_TYPE,
            dt.INPUT_API_KEY + GMAP_API_KEY,
        ]

        request_url = "".join(url)

        print(request_url)

        # Makes the request
        gmap_req = requests.get(request_url)

        return gmap_req.json()

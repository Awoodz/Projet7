import requests

import grandpy.data as dt


class Requester():
    """Docstrings"""

    def __init__(self, parsed_txt, gmap_api_key):
        self.placedata = self.gmap_request(parsed_txt, gmap_api_key)

    def gmap_request(self, parsed_txt, gmap_api_key):
        """Docstrings"""
        input_key = (dt.INPUT_KEY + parsed_txt)
        inputtype = (dt.INPUT_TYPE)
        api_key = (dt.INPUT_API_KEY + gmap_api_key)
        gmap_req = requests.get(
            dt.REQUEST_GMAP_URL +
            input_key +
            inputtype +
            api_key)
        return gmap_req.json()

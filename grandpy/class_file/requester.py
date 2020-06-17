import requests

import grandpy.data as dt


class Requester():
    """Docstrings"""

    def __init__(self, parsed_txt, gmap_api_key):
        self.placedata = self.gmap_request(parsed_txt, gmap_api_key)

    def gmap_request(self, parsed_txt, gmap_api_key):
        """Docstrings"""
        checker = False
        request_txt = parsed_txt
        while not checker:
            input_key = (dt.INPUT_KEY + request_txt)
            inputtype = (dt.INPUT_TYPE)
            api_key = (dt.INPUT_API_KEY + gmap_api_key)
            gmap_req = requests.get(
                dt.REQUEST_GMAP_URL +
                input_key +
                inputtype +
                api_key)

            if gmap_req.json()[dt.API_MAP_STATUS] == "INVALID_REQUEST":
                checker = True
                return {dt.API_MAP_CANDIDATES: 0}

            elif gmap_req.json()[dt.API_MAP_STATUS] != "OK":
                words_list = request_txt.split(" ")
                words_list.remove(words_list[0])
                request_txt = ""
                index_nb = 0

                for elt in words_list:
                    request_txt = request_txt + words_list[index_nb] + " "
                    index_nb += 1

            else:
                checker = True
                return gmap_req.json()

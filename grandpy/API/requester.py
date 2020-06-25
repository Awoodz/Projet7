import requests

import grandpy.utilities.data as dt


class Requester():
    """Makes requests to Google Map API"""

    def __init__(self, parsed_txt, gmap_api_key):
        self.placedata = self.request_engine(parsed_txt, gmap_api_key)

    def google_map_request(request_txt, gmap_api_key):
        """Makes requests to Google Map API"""
        # Creates variables to create an url string in request
        input_key = (dt.INPUT_KEY + request_txt)
        inputtype = (dt.INPUT_TYPE)
        api_key = (dt.INPUT_API_KEY + gmap_api_key)

        # Makes the request
        gmap_req = requests.get(
            dt.REQUEST_GMAP_URL +
            input_key +
            inputtype +
            api_key
        )
        return gmap_req.json()

    def words_removal(request_txt):
        """Removes words from a string"""
        # Split request text to a list
        words_list = []
        words_list = request_txt.split(" ")
        # Removes the first index of the list
        # The important words should be at the end
        # of the sentence
        words_list.remove(words_list[0])
        # reset request_txt
        request_txt = ""
        # reset index number
        index_nb = 0
        # recreates a sentence in request_txt
        for elt in words_list:
            request_txt = request_txt + words_list[index_nb] + " "
            index_nb += 1
        return request_txt

    def request_engine(self, parsed_txt, gmap_api_key):
        """Makes requests to Google Map API and modify"""
        """the request if there is no result"""
        # Setting a variable for loop
        checker = False

        request_txt = parsed_txt

        # As long as checker is not True
        while not checker:

            req_response = Requester.google_map_request(
                request_txt,
                gmap_api_key
            )

            # If the request status is invalid
            if req_response[dt.API_MAP_STATUS] == "INVALID_REQUEST":
                # stop the loop
                checker = True
                # return an empty google map json
                # return "candidates" tag avoid crash in Place class
                return {dt.API_MAP_CANDIDATES: 0}

            # And if request status is not OK
            elif req_response[dt.API_MAP_STATUS] != "OK":
                request_txt = Requester.words_removal(request_txt)

            # Else, if everything is ok
            else:
                # stop the loop
                checker = True
                # return the result as a json
                return req_response

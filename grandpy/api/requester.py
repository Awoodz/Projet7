import grandpy.utilities.data as dt
from grandpy.api.gmap_request import Gmap
from grandpy.api.wiki_request import Wiki


class Requester:
    """Makes requests to Google Map API and Wiki API"""

    def __init__(self, parsed_txt):
        self.placedata = self.request_engine(parsed_txt)

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

    def request_engine(self, parsed_txt):
        """Makes requests to Google Map API and wikipedia."""
        """Modify the request if there is no result"""
        # Setting a variable for loop
        checker = False

        request_txt = parsed_txt

        # As long as checker is not True
        while not checker:

            gmap_response = Gmap(request_txt).req_result

            # If the request status is invalid
            if gmap_response[dt.API_MAP_STATUS] == "INVALID_REQUEST":
                # stop the loop
                checker = True
                # return an empty google map json
                # return "candidates" tag avoid crash in Place class
                return {dt.API_MAP_CND: 0}

            # And if request status is not OK
            elif gmap_response[dt.API_MAP_STATUS] != "OK":
                request_txt = Requester.words_removal(request_txt)

            # Else, if everything is ok
            else:
                # stop the loop
                checker = True
                # return the result as a json
                wiki_response = Wiki(request_txt).story
                return {"gmap": gmap_response, "wiki": wiki_response}

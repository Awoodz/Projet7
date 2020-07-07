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
        return {
            "gmap": Requester.make_gmap_request(parsed_txt),
            "wiki": Requester.make_wiki_request(parsed_txt)
        }

    def make_gmap_request(parsed_txt):
        """Makes requests to Google Map API."""
        """Modify the request if there is no result"""
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
                # stop the first loop
                checker = True
                return gmap_response

    def make_wiki_request(parsed_txt):
        """Makes requests to wikipedia."""
        """Modify the request if there is no result"""
        # Setting a variable for loop

        request_txt = parsed_txt

        checker = False
        # As long as checker2 is not true
        while not checker:

            wiki_response = Wiki(request_txt).story

            # If wikipedia request as no result :
            if wiki_response == "fail":
                # remove one word from the request
                request_txt = Requester.words_removal(request_txt)
                print(request_txt)
                # If there is no word left in request
                if request_txt == "":
                    # End the loop
                    checker = True
                    # Return answer
                    return dt.GRANDPY_FORGET
            # If a there is a result
            else:
                # End the loop
                checker = True
                # return the result as a json
                return wiki_response

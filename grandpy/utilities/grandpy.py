from grandpy.utilities.parser import Parser
from grandpy.api.requester import Requester
from grandpy.api.place import Place
from grandpy.api.story import Story


class Grandpy():
    """Gather all datas that will be returned to frontpage"""

    def __init__(
        self,
        language,
        gmap_api_key,
        form_input,
        stop_words,
        punctuation
    ):
        self.parsed_request = Parser(
            form_input,
            stop_words,
            punctuation
        ).request

        self.apigmap = Requester(
            self.parsed_request,
            gmap_api_key
        ).placedata
        
        self.place_data = Place(self.apigmap)
        self.story_data = Story(self.apigmap, language)

    @property
    def name(self):
        return self.place_data.name

    @property
    def adress(self):
        return self.place_data.adress

    @property
    def lng(self):
        return self.place_data.lng

    @property
    def lat(self):
        return self.place_data.lat

    @property
    def story(self):
        return self.story_data.story

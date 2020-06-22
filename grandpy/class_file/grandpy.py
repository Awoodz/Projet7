from grandpy.class_file.parser import Parser
from grandpy.class_file.requester import Requester
from grandpy.class_file.place import Place
from grandpy.class_file.story import Story


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
        self.parsed_request = Parser(form_input, stop_words, punctuation)
        parsed_txt = self.parsed_request.request
        self.apigmap = Requester(parsed_txt, gmap_api_key)
        gmap_json = self.apigmap.placedata
        self.place_data = Place(gmap_json)
        self.story_data = Story(gmap_json, language)

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

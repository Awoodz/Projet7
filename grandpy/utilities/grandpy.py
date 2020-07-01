from grandpy.utilities.parser import Parser
from grandpy.api.requester import Requester
from grandpy.api.place import Place
import grandpy.utilities.data as dt
import grandpy.utilities.helpers as hp


class Grandpy():
    """Gather all datas that will be returned to frontpage"""

    def __init__(self, form_input):
        self.parsed_request = Parser(form_input).request
        self.apigmap = Requester(self.parsed_request).placedata
        self.place_data = Place(self.apigmap["gmap"], self.apigmap["wiki"])

    @property
    def name(self):
        return self.place_data.name

    @property
    def adress(self):
        return hp.randomisator(dt.GRANDPY_PLACE) + self.place_data.adress

    @property
    def lng(self):
        return self.place_data.lng

    @property
    def lat(self):
        return self.place_data.lat

    @property
    def story(self):
        return hp.randomisator(dt.GRANDPY_STORY) + self.place_data.story

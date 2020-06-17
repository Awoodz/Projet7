import grandpy.class_file.parser as prs
import grandpy.class_file.requester as rq
import grandpy.class_file.place as pl
import grandpy.class_file.story as st


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
        self.parsed_request = prs.Parser(form_input, stop_words, punctuation)
        parsed_txt = self.parsed_request.request
        self.apigmap = rq.Requester(parsed_txt, gmap_api_key)
        gmap_json = self.apigmap.placedata
        self.place_data = pl.Place(gmap_json)
        self.story_data = st.Story(gmap_json, language)

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

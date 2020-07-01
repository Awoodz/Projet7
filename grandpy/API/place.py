import grandpy.utilities.data as dt


class Place():
    """Gather all place datas"""

    def __init__(self, gmap_json, wiki_response):
        self.place_data = gmap_json
        self.story_data = wiki_response

    @property
    def name(self):
        return self.place_data[dt.API_MAP_CND][0][dt.API_MAP_NAME]

    @property
    def adress(self):
        return self.place_data[dt.API_MAP_CND][0][dt.API_MAP_ADRESS]

    @property
    def lng(self):
        return self.place_data[dt.API_MAP_CND][0][dt.API_MAP_GEO][dt.API_MAP_LOC][dt.API_MAP_LNG]

    @property
    def lat(self):
        return self.place_data[dt.API_MAP_CND][0][dt.API_MAP_GEO][dt.API_MAP_LOC][dt.API_MAP_LAT]

    @property
    def story(self):
        return self.story_data
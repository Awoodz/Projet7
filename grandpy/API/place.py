import grandpy.utilities.data as dt


class Place():
    """Gather all place datas"""

    def __init__(self, gmap_json):
        self.data = gmap_json

    @property
    def name(self):
        return self.data[dt.API_MAP_CND][0][dt.API_MAP_NAME]

    @property
    def adress(self):
        return self.data[dt.API_MAP_CND][0][dt.API_MAP_ADRESS]

    @property
    def lng(self):
        return self.data[dt.API_MAP_CND][0][dt.API_MAP_GEO][dt.API_MAP_LOC][dt.API_MAP_LNG]

    @property
    def lat(self):
        return self.data[dt.API_MAP_CND][0][dt.API_MAP_GEO][dt.API_MAP_LOC][dt.API_MAP_LAT]

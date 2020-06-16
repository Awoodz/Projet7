import grandpy.data as dt


class Place():
    """Docstrings"""

    def __init__(self, gmap_json, story):
        self.name = gmap_json[dt.API_MAP_NAME]
        self.adress = gmap_json[dt.API_MAP_ADRESS]
        self.longitude = gmap_json[dt.API_MAP_GEO][dt.API_MAP_LOC][dt.API_MAP_LNG]
        self.latitude = gmap_json[dt.API_MAP_GEO][dt.API_MAP_LOC][dt.API_MAP_LAT]
        self.story = story

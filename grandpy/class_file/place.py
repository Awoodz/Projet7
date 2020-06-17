import data as dt


class Place():
    """Docstrings"""

    def __init__(self, gmap_json):
        self.json = gmap_json
        self.data = self.get_place_data()

    def get_place_data(self):
        place_data = []
        for dictionary in self.json[dt.API_MAP_CANDIDATES]:
            place_data.append(dictionary)
        return place_data[0]

    @property
    def name(self):
        return self.data[dt.API_MAP_NAME]

    @property
    def adress(self):
        return self.data[dt.API_MAP_ADRESS]

    @property
    def lng(self):
        return self.data[dt.API_MAP_GEO][dt.API_MAP_LOC][dt.API_MAP_LNG]

    @property
    def lat(self):
        return self.data[dt.API_MAP_GEO][dt.API_MAP_LOC][dt.API_MAP_LAT]
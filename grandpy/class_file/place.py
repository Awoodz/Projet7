import grandpy.data as dt


class Place():
    """Gather all place datas"""

    def __init__(self, gmap_json):
        self.json = gmap_json
        self.data = self._get_place_data()

    def _get_place_data(self):
        """Get the datas out of "candidates" list of gmap json"""
        place_data = []
        # For each dictionnary in json
        for dictionary in self.json[dt.API_MAP_CANDIDATES]:
            # appends a list with every dictionnary
            place_data.append(dictionary)
        # Returns the first (and only) index of that list
        # so we can work with dictionnaries only
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

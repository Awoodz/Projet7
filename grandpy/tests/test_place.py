from grandpy.class_file.place import Place


def test_does_datas_get_out_from_json_list(monkeypatch):
    monkeypatch.setattr(
        "grandpy.data.API_MAP_CANDIDATES",
        "candidates_test"
    )
    fake_json = {
        "candidates_test": [
            {
                "name": "Test_town",
                "formatted_address": "0 grandpy/tests/test_place.py street",
                "geometry": {
                    "location": {
                        "lat": 0,
                        "lng": 100
                    }
                }
            }
        ]
    }
    fake_place = Place(fake_json)
    without_list_json = Place.get_place_data(fake_place)
    assert without_list_json == {
        "name": "Test_town",
        "formatted_address": "0 grandpy/tests/test_place.py street",
        "geometry": {
            "location": {
                "lat": 0,
                "lng": 100
            }
        }
    }


def mock_get_name(self):
    return {"name_test": "Test_town"}


def test_does_place_class_can_return_name(monkeypatch):
    monkeypatch.setattr(Place, "get_place_data", mock_get_name)
    monkeypatch.setattr(
        "grandpy.data.API_MAP_NAME",
        "name_test"
    )
    fake_json = {}
    fake_place = Place(fake_json)
    assert fake_place.name == "Test_town"


def mock_get_address(self):
    return {"test_address": "0 grandpy/tests/test_place.py street"}


def test_does_place_class_can_return_address(monkeypatch):
    monkeypatch.setattr(Place, "get_place_data", mock_get_address)
    monkeypatch.setattr(
        "grandpy.data.API_MAP_ADRESS",
        "test_address"
    )
    fake_json = {}
    fake_place = Place(fake_json)
    assert fake_place.adress == "0 grandpy/tests/test_place.py street"


def mock_get_lat(self):
    return {
        "test_geometry": {
            "test_location": {
                "test_lat": 0
            }
        }
    }


def test_does_place_class_can_return_latitude(monkeypatch):
    monkeypatch.setattr(Place, "get_place_data", mock_get_lat)
    monkeypatch.setattr(
        "grandpy.data.API_MAP_GEO",
        "test_geometry"
    )
    monkeypatch.setattr(
        "grandpy.data.API_MAP_LOC",
        "test_location"
    )
    monkeypatch.setattr(
        "grandpy.data.API_MAP_LAT",
        "test_lat"
    )
    fake_json = {}
    fake_place = Place(fake_json)
    assert fake_place.lat == 0


def mock_get_lng(self):
    return {
        "test_geometry": {
            "test_location": {
                "test_lng": 100
            }
        }
    }


def test_does_place_class_can_return_longitude(monkeypatch):
    monkeypatch.setattr(Place, "get_place_data", mock_get_lng)
    monkeypatch.setattr(
        "grandpy.data.API_MAP_GEO",
        "test_geometry"
    )
    monkeypatch.setattr(
        "grandpy.data.API_MAP_LOC",
        "test_location"
    )
    monkeypatch.setattr(
        "grandpy.data.API_MAP_LNG",
        "test_lng"
    )
    fake_json = {}
    fake_place = Place(fake_json)
    assert fake_place.lng == 100


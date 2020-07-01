from grandpy.api.place import Place


def test_does_place_class_can_return_name(monkeypatch):
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_CND",
        "candidates_test"
    )
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_NAME",
        "name_test"
    )
    fake_json = {
        "candidates_test": [
            {"name_test": "Test_town"}
        ]
    }
    fake_place = Place(fake_json, "mock_story")
    assert fake_place.name == "Test_town"


def test_does_place_class_can_return_address(monkeypatch):
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_CND",
        "candidates_test"
    )
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_ADRESS",
        "test_address"
    )
    fake_json = {
        "candidates_test": [
            {"test_address": "0 grandpy/tests/test_place.py street"}
        ]
    }
    fake_place = Place(fake_json, "mock_story")
    assert fake_place.adress == "0 grandpy/tests/test_place.py street"


def test_does_place_class_can_return_latitude(monkeypatch):
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_CND",
        "candidates_test"
    )
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_GEO",
        "test_geometry"
    )
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_LOC",
        "test_location"
    )
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_LAT",
        "test_lat"
    )
    fake_json = {
        "candidates_test": [
            {
                "test_geometry": {
                    "test_location": {
                        "test_lat": 0
                    }
                }
            }
        ]
    }
    fake_place = Place(fake_json, "mock_story")
    assert fake_place.lat == 0


def test_does_place_class_can_return_longitude(monkeypatch):
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_CND",
        "candidates_test"
    )
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_GEO",
        "test_geometry"
    )
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_LOC",
        "test_location"
    )
    monkeypatch.setattr(
        "grandpy.utilities.data.API_MAP_LNG",
        "test_lng"
    )
    fake_json = {
        "candidates_test": [
            {
                "test_geometry": {
                    "test_location": {
                        "test_lng": 100
                    }
                }
            }
        ]
    }
    fake_place = Place(fake_json, "mock_story")
    assert fake_place.lng == 100

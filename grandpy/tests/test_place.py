from grandpy.class_file.place import Place


def test_does_datas_get_out_from_json_list():
    fake_json = {
        "candidates": [
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


def test_does_place_class_can_return_name():
    fake_json = {
        "candidates": [
            {
                "name": "Test_town"
            }
        ]
    }
    fake_place = Place(fake_json)
    assert fake_place.name == "Test_town"


def test_does_place_class_can_return_adress():
    fake_json = {
        "candidates": [
            {
                "formatted_address": "0 grandpy/tests/test_place.py street"
            }
        ]
    }
    fake_place = Place(fake_json)
    assert fake_place.adress == "0 grandpy/tests/test_place.py street"


def test_does_place_class_can_return_latitude():
    fake_json = {
        "candidates": [
            {
                "geometry": {
                    "location": {
                        "lat": 0
                    }
                }
            }
        ]
    }
    fake_place = Place(fake_json)
    assert fake_place.lat == 0


def test_does_place_class_can_return_longitude():
    fake_json = {
        "candidates": [
            {
                "geometry": {
                    "location": {

                        "lng": 100
                    }
                }
            }
        ]
    }
    fake_place = Place(fake_json)
    assert fake_place.lng == 100

import grandpy.utilities.helpers as hp


def test_does_stop_words_unify_both_lists():
    mock_list_1 = ["1", "2"]
    mock_list_2 = ["3", "4"]
    mock_response = hp.stop_words(mock_list_1, mock_list_2)
    assert mock_response == ["1", "2", "3", "4"]


def test_does_punctuation_create_list_from_string():
    mock_string_1 = "azerty"
    mock_response = hp.punctuation(mock_string_1)
    assert mock_response == ["a", "z", "e", "r", "t", "y"]


def mock_random(mock1, mock2, mock3):
    return 0


def test_does_randomizator_get_string_out_of_list(monkeypatch):
    monkeypatch.setattr("random.randrange", mock_random)
    mock_list = ["yes", "no"]
    mock_response = hp.randomisator(mock_list)
    assert mock_response == "yes"

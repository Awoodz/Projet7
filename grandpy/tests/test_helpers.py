import grandpy.utilities.helpers as hp


def does_stop_words_unify_both_lists():
    mock_list_1 = ["1", "2"]
    mock_list_2 = ["3", "4"]
    mock_response = hp.stop_words(mock_list_1, mock_list_2)
    assert mock_response == ["1", "2", "3", "4"]


def does_punctuation_create_list_from_string():
    mock_string_1 = "azerty"
    mock_response = hp.punctuation(mock_string_1)
    assert mock_response == ["a", "z", "e", "r", "t", "y"]
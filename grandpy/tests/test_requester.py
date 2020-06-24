from grandpy.class_file.requester import Requester


def test_does_words_removal_remove_first_words_of_string():
    test_text = "one two"
    test_response = Requester.words_removal(test_text)
    assert test_response == "two "

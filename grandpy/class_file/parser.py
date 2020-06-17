class Parser():
    """Docstrings"""

    def __init__(self, form_input, stop_words, punctuation):
        self.request = self.parse(form_input, stop_words, punctuation)

    def parse(self, form_input, stop_words, punctuation):

        request = form_input.lower()

        for elem in punctuation:
            request = request.replace(elem, " ")

        parsed_request = request.split()

        for words in stop_words:
            for elem in parsed_request:
                if elem == words:
                    parsed_request.remove(elem)
        return (" ".join(parsed_request))

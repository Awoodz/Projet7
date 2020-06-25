class Parser():
    """Removes useless words and punctuation symbols"""
    """from a sentence"""

    def __init__(self, form_input, stop_words, punctuation):
        self.request = self.parse(form_input, stop_words, punctuation)

    def parse(self, form_input, stop_words, punctuation):
        """Removes useless words and punctuation symbols"""
        """from a sentence"""

        # Changes uppercases to lowercases in the sentence
        request = form_input.lower()

        # Removing punctuation symbols from the sentence
        for elem in punctuation:
            request = request.replace(elem, " ")

        # Creates a list with all the words
        parsed_request = request.split()

        # For each words in the stop words list
        for words in stop_words:
            # and each words form the list we created
            for elem in parsed_request:
                # if word is existing in both lists
                if elem == words:
                    # remove it !
                    parsed_request.remove(elem)
        # then return a new strings without stop words
        return (" ".join(parsed_request))

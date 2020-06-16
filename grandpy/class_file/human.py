class Human():
    """Docstrings"""

    def __init__(self, form_input):
        self.request = form_input
    
    def parse(self, stop_words, punctuation):

        request = self.request.lower()
        
        for elem in punctuation:
            request = request.replace(elem, " ")

        parsed_request = request.split()

        for words in stop_words:
            for elem in parsed_request:
                if elem == words:
                    parsed_request.remove(elem)
        return (" ".join(parsed_request))

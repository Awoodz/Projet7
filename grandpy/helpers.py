def stop_words(stopwords, extra_stopwords):
    """Docstrings"""
    for elem in extra_stopwords:
        stopwords.append(elem)
    return stopwords

def punctuation(punctuation_string):
    """Docstrings"""
    punctuation_list = []
    for char in punctuation_string:
        punctuation_list.append(char)
    return punctuation_list

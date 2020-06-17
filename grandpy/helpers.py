import random


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


def randomisator(list_name):
    """Docstrings"""
    index_nb = 0
    for elt in list_name:
        index_nb += 1
    rand = random.randrange(0, index_nb, 1)
    return list_name[rand]

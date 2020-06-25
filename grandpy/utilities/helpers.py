import random


def stop_words(stopwords, extra_stopwords):
    """Create a unique list of stopwords"""
    # for each elements in extra stopwords list :
    for elem in extra_stopwords:
        # add elements to the stopwords list
        stopwords.append(elem)
    # return new list
    return stopwords


def punctuation(punctuation_string):
    """Create a list of every punctuation"""
    # creating an empty list
    punctuation_list = []
    # for each punctuation symbols in the string
    for char in punctuation_string:
        # add punctunation symbols to a list
        punctuation_list.append(char)
    # return that list
    return punctuation_list


def randomisator(list_name):
    """Get a random elements of a list"""
    # setting index number to 0
    index_nb = 0
    # for each elements in the list
    for elt in list_name:
        # add 1 to index number
        index_nb += 1
    # rand a number between 0 and the index number
    rand = random.randrange(0, index_nb, 1)
    # return the randomized index
    return list_name[rand]

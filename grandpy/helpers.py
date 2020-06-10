import json
import requests
import grandpy.data as dt

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

def gmap_request(parsed_txt, gmap_api_key):
    """Docstrings"""
    input_key = ("input=" + parsed_txt)
    inputtype = ("&inputtype=textquery&fields=formatted_address,name,geometry")
    api_key = ("&key=" + gmap_api_key)
    gmap_req = requests.get(
        dt.REQUEST_GMAP_URL +
        input_key +
        inputtype +
        api_key)
    return gmap_req.json()

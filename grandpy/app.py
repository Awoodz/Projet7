from stop_words import get_stop_words
import string

import grandpy.class_file.grandpy as gp
import grandpy.data as dt
import grandpy.helpers as hp
import config as cg


def get_request(user_input):

    stopwords = hp.stop_words(
        get_stop_words(dt.BOT_LANGUAGE),
        dt.SPECIAL_STOP_WORDS
    )
    punctuation = hp.punctuation(string.punctuation)

    # try:

    #     grandpy = gp.Grandpy(
    #         dt.WIKI_LANGUAGE,
    #         cg.GMAP_API_KEY,
    #         user_input,
    #         stopwords,
    #         punctuation
    #     )

    #     return {
    #         "name": grandpy.name,
    #         "adress": grandpy.adress,
    #         "lat": grandpy.lat,
    #         "lng": grandpy.lng,
    #         "story": grandpy.story
    #     }
    # except:
    #     return {
    #         "adress": "Mais qu'est ce que tu raconte ?",
    #         "story": "Tu te drogues, petit ?"
    #     }

    grandpy = gp.Grandpy(
        dt.WIKI_LANGUAGE,
        cg.GMAP_API_KEY,
        user_input,
        stopwords,
        punctuation
    )

    return {
        "name": grandpy.name,
        "adress": grandpy.adress,
        "lat": grandpy.lat,
        "lng": grandpy.lng,
        "story": grandpy.story
    }
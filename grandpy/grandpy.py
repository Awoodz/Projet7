from stop_words import get_stop_words
import string

import grandpy.class_grandpy as cg
import grandpy.data as dt
import grandpy.helpers as hp


def get_request(user_input):

    place_data = []

    stopwords = hp.stop_words(
        get_stop_words(dt.BOT_LANGUAGE),
        dt.SPECIAL_STOP_WORDS
    )
    punctuation = hp.punctuation(string.punctuation)

    user = cg.Human(user_input)

    parser = user.parse(stopwords, punctuation)

    try:
        result_json = hp.gmap_request(parser, dt.GMAP_API_KEY)

        for dictionary in result_json["candidates"]:
            place_data.append(dictionary)

        place = cg.Place(place_data[0], "bonjour")

        return {
            "name": place.name,
            "adress": place.adress,
            "lat": place.latitude,
            "lng": place.longitude,
            "story": place.story
        }
    except:
        return {
            "adress" : "Mais qu'est ce que tu raconte ?",
            "story" : "Tu te drogues, petit ?"
        }


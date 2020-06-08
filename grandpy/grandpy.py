from stop_words import get_stop_words
import string

import grandpy.class_grandpy as cg
import grandpy.data as dt
import grandpy.helpers as hp

def traitement(user_input):

    stopwords = hp.stop_words(
        get_stop_words(dt.BOT_LANGUAGE),
        dt.SPECIAL_STOP_WORDS
    )
    punctuation = hp.punctuation(string.punctuation)
    user = cg.Human(user_input)
    parser = user.parse(stopwords, punctuation)
    return {"text_original": user_input, "text_parsed": parser}

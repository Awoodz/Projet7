# Determine language of stop words in stopwords module
BOT_LANGUAGE = "french"
# Determine language of wiki API
WIKI_LANGUAGE = "fr"
# Number of sentence requested to wiki API
SENT_NB = 1
# Special stop words that are not in stop words popular list
SPECIAL_STOP_WORDS = ["grandpy"]

# Candidates tag of google map json
API_MAP_CND = "candidates"
# Status tag of google map json
API_MAP_STATUS = "status"
# Name tag of google map json
API_MAP_NAME = "name"
# adress tag of google map json
API_MAP_ADRESS = "formatted_address"
# Geometry tag of google map json
API_MAP_GEO = "geometry"
# Location tag of google map json
API_MAP_LOC = "location"
# Latitude tag of google map json
API_MAP_LAT = "lat"
# Longitude tag of google map json
API_MAP_LNG = "lng"

# First part of google map request url
REQUEST_GMAP_URL = (
    "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
)

# Input part of google map request url
INPUT_KEY = "input="
# Inputtype part of google map request url
INPUT_TYPE = "&inputtype=textquery&fields=formatted_address,name,geometry"
# Api key part of google map request url
INPUT_API_KEY = "&key="

# List of sentences for place part if research fails
GRANDPY_PLACE_ERROR = [
    "Mais qu'est ce que c'est que ce charabia ?",
    "Quoi ? Qu'est ce que tu racontes ? je n'ai rien compris !",
]

# List of sentences for story part if research fails
GRANDPY_STORY_ERROR = [
    "...ou alors c'est mon créateur qui m'a mal programmé !",
    "...ou bien c'est mon euh... 'Parser' ! qui n'est pas au point..."
]

# List of sentences for place part
GRANDPY_PLACE = [
    "Mais bien sûr que je connais ! c'est au ",
    "Sans problème ! c'est à cette adresse : "
]

# List of sentences for story part
GRANDPY_STORY = [
    "D'ailleurs je peux même ajouter ceci : ",
    "Tu veux plus d'information ? Et bien sâches que "
]

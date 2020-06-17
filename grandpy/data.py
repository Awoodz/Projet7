BOT_LANGUAGE = "french"
WIKI_LANGUAGE = "fr"
SPECIAL_STOP_WORDS = ["grandpy"]

API_MAP_CANDIDATES = "candidates"
API_MAP_STATUS = "status"
API_MAP_NAME = "name"
API_MAP_ADRESS = "formatted_address"
API_MAP_GEO = "geometry"
API_MAP_LOC = "location"
API_MAP_LAT = "lat"
API_MAP_LNG = "lng"

REQUEST_GMAP_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"

INPUT_KEY = "input="
INPUT_TYPE = "&inputtype=textquery&fields=formatted_address,name,geometry"
INPUT_API_KEY = "&key="

GRANDPY_PLACE_ERROR = [
    "Mais qu'est ce que c'est que ce charabia ?",
    "Quoi ? Qu'est ce que tu racontes ? je n'ai rien compris !",
]

GRANDPY_STORY_ERROR = [
    "...ou alors c'est mon créateur qui m'a mal programmé !",
    "...ou bien c'est mon euh... 'Parser' ! qui n'est pas au point..."
]

GRANDPY_PLACE = [
    "Mais bien sûr que je connais ! c'est au ",
    "Sans problème ! c'est à cette adresse : "
]

GRANDPY_STORY = [
    "D'ailleurs je peux même ajouter ceci : ",
    "Tu veux plus d'information ? Et bien sâches que "
]

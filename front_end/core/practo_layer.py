import requests
from bs4 import BeautifulSoup

class PractoLayer:

    def __init__(self, symptom, city_name):
        self.symptom = symptom
        self.city_name = city_name

    def search_doctor(self):

        search_url = "https://www.practo.com/search/"
        q = {
            "word" : self.symptom,
            "autocompleted" : False,
            "category" : "symptom"
        }
        #params = []
        #params.append(q)
        r = requests.get(search_url, q)

        return r
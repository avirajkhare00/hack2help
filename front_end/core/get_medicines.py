import requests
from bs4 import BeautifulSoup
import time

class GetMedicines:

    def __init__(self, medicine_name):
        self.medicine_name = medicine_name

    def search_medicines(self):

        med_plus_url = "http://www.netmeds.com/druginfo"

        params = {
            'q' : self.medicine_name,
            'limit' : 10,
            'time' : time.time(),
            'searchtype' : 'All+Drugs'
        }

        r = requests.get(med_plus_url, params)

        bsObj = BeautifulSoup(r.text)

        medicine_name = {}

        medicine_name['data'] = []

        for medicine in bsObj.findAll("a"):
            medicine_name['data'].append(medicine.get_text().split('Rs.')[0])


        return medicine_name

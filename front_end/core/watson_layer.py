import requests
from bs4 import BeautifulSoup
import json

class WatsonLayer:

    def __init__(self, query):
        self.query = query

    def return_watson_result(self):

        params = {
            'ranker_id' : '1eec7cx29-rank-1395',
            'wt' : 'json',
            'fl' : 'id,disease_name,body',
            'q' : self.query
        }

        watson_api_url = 'https://b263e744-61de-4dbe-8cda-a0615f0948e2:1VMGaAgRzyet@gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/scfc280036_a0e0_4d6b_92a7_9895bf04c6ee/solr/example_collection/fcselect'

        r = requests.get(watson_api_url, params)

        result_list = json.loads(r.text)

        return result_list['response']['docs']
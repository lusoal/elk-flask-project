#!/usr/bin/python
import requests
from datetime import date, timedelta
import datetime

url = "http://it4.brazilsouth.cloudapp.azure.com:9200"

def get_elk_logs(dias):
    d = datetime.datetime.today() - timedelta(days=dias)
    d = d.strftime("%d.%m.%Y")

    response = requests.get(url+"/logger-"+d+"/_search?pretty=true&q=*:*").json()
    
    if "hits" in response:
        for i in response['hits']['hits']:
            print i['_source']['Status'], i['_source']['Ambiente'], i['_source']["Mensagem"] 
    else:
        print "Indice Inexistente"

get_elk_logs(4)

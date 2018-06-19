import requests
from datetime import date, timedelta
import datetime

class Elk():

    cliente = None
    url = None

    def __init__(self, cliente):
        self.cliente = cliente
        self.url = ""
    
    def get_logs_today(self, dias):
        status = []
        mensagem = []

        print self.cliente
        d = datetime.datetime.today() - timedelta(days=dias)
        d = d.strftime("%d.%m.%Y")

        response = requests.get(self.url+"/logger-"+d+"/_search?pretty=true&q=*:*").json()

        print response
        if "hits" in response:
            for i in response['hits']['hits']:
                if self.cliente == i['_source']['Ambiente']:
                    status.append(i['_source']['Status'])
                    mensagem.append(i['_source']["Mensagem"])
                    print i['_source']['Status'], i['_source']["Mensagem"] 
        else:
            print "Indice Inexistente"
        
        return status, mensagem
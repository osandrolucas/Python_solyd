import requests
import json
import datetime
import time

while True:
    requisicao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
    cotacao = json.loads(requisicao.text)

    print('### COTAÇÃO ### ', datetime.datetime.now())
    print('Dólar:', cotacao['valores']['USD']['valor'])
    print('Euro:', cotacao['valores']['EUR']['valor'])
    print('Bitcoin:', cotacao['valores']['BTC']['valor'])
    time.sleep(2) #2 segundos
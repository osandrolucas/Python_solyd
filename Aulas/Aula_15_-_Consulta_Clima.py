import requests
import json
import textblob
from textblob import TextBlob

cidade = input('Informe sua cidade: ')

req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&APPID=574708452380626a25e411bfeab9dd7a')

#print(req.text)

#Transforma em dicionário python
tempo = json.loads(req.text)

#Traduzindo retorno
condicao_us = TextBlob(tempo['weather'][0]['main'])
condicao_us.detect_language()
condicao_traduzida = condicao_us.translate(to="pt_br")

print('Condição do tempo:', condicao_traduzida)
#Convertendo de Kelvin para Celsius
print('Temperatura: ', float(tempo['main']['temp']) - 273.15,'°C')

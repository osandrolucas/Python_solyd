import oauth2
import json

#Consumer API keys

consumer_key = ''
consumer_secret = ''
token_key = ''
token_secret = ''

#Criando objeto consumidor e Token com as duas informações que cada um tem
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)

#Criando cliente, para fazer as requisições
cliente = oauth2.Client(consumer, token)

requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=brasil')

#O retorno é em Bytes, é preciso decodificar

decod = requisicao[1].decode()

objeto = json.loads(decod)

print(objeto)




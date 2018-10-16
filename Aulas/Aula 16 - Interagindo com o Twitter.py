import oauth2
import json

#Consumer API keys

consumer_key = 'wJ2GYSf9nEDCuBEEnb7vKb8yk'
consumer_secret = '5G7KjGOeNd6bYs4pjdy50QnvBcPsVgRjbGpZPzhS32bCynXvpz'
token_key = '236078820-96IlY5TB2S0LTpejyjUJSdH8xEYogoPQyXPtpWHQ'
token_secret = '5rkZ5L7JUgElfgf0JSd0awEznaSp0wE84FONQQR0Ba6zX'

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




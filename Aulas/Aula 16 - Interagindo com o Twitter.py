import oauth2
import json
import urllib.parse
from emoji import emojize
# Enf of imports

# Consumer API keys

#!!!Informe as suas Keys!!!!!
consumer_key = ''
consumer_secret = ''
token_key = ''
token_secret = ''

# Criando objeto consumidor e Token com as duas informações que cada um tem
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)

# Criando cliente, para fazer as requisições
cliente = oauth2.Client(consumer, token)

#Functions
def pesquisa(query):
    # Na linha abaixo, estou transformando em url especial, onde posso usar caracteres especiais
    query_codificada = urllib.parse.quote(query, safe='')
    requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')
    # O retorno é em Bytes, é preciso decodificar
    decod = requisicao[1].decode()
    objeto = json.loads(decod)
    twittes = objeto['statuses']
    for tweet in twittes:
        print('Usuário: @{}'.format(tweet['user']['screen_name']))
        print('Tweet: {}'.format(tweet['text']))
        print()

def tweetar(query):
    # Na linha abaixo, estou transformando em url especial, onde posso usar caracteres especiais
    query_codificada = urllib.parse.quote(query, safe='')
    print(emojize('Twittando :clock12: :clock2: :clock3: :clock4: :clock5: ...',
                  use_aliases=True))
    requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')
    print('\nTweet postado com sucesso!')

#Inicio do Programa
print('\n### INTERAGINDO COM O TWITTER ###')
op = input('\nEscolha uma das opções abaixo...\n1 para Pesquisar\n2 para Tweetar\n3 para Sair\nOpção: ')
if int(op) == 1:
    query = input('Palavras ou Tags para Pesquisar: ')
    pesquisa(query)
if int(op) == 2:
    query = input('Novo Tweet: ')
    tweetar(query)
if int(3) == 3:
    print('\nUm abraço e camigol....\nFim')









import requests
import json
print('''API - application program interface
API usada no exemplo: http://www.omdbapi.com/\n\n''')

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t='+titulo+'&apikey=1b325c5b'+'&type=movie')
        dicio = json.loads(req.text) # Transformando o retorno (JSON) em um dicionário do Python
        return dicio
    except Exception as e:
        print('Erro na Conexão!', e)
        return None

def printar_detalhes(filme): #Função que escreve somente algumas coisas que eu quero mostrar
    print('Nome do Filme: {}'.format(filme['Title']))
    print('Ano: {}'.format(filme['Year']))
    print('Lançamento: {}'.format(filme['Released']))
    print('Duração: {}'.format(filme['Runtime']))
    print('Gênero: {}'.format(filme['Genre']))
    print('Diretor: {}'.format(filme['Director']))
    print('Atores: {}'.format(filme['Actors']))
    print('Nota no IMDB: {}'.format(filme['imdbRating']))
    print('Prêmios: {}'.format(filme['Awards']))
    print('Poster: {}'.format(filme['Poster']))
    print('')

sair = False

while not sair:
    op = input('Informe o nome de um Filme ou SAIR para fechar: ')
    if op == 'SAIR':
        sair = True
        print('Saindo....')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('ERRO: {}!\n'.format(filme))
        else:
            printar_detalhes(filme)
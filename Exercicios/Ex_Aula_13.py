import requests
import json
import time

# Cria lista de Filmes com o Nome e o Ano
def lista_filmes(titulo):
    lista = []
    print('Pesquisando, por favor aguarde...')
    # Busca os filmes até a página 100
    for i in range(1, 101):
        try:
            url = 'http://omdbapi.com/?s=' + titulo + '&apikey=1b325c5b&type=movie&page=' + str(i)
            req = requests.get(url)
            resposta = json.loads(req.text)
            # Se ainda tiver vai acrescentando a lista
            if resposta['Response'] == 'True':
                for filme in resposta['Search']:
                    tit = filme['Title']
                    ano = filme['Year']
                    poster = filme['Poster']
                    string = 'Nome: ' + tit + ' - Ano: (' + ano + ')' + ' - Poster: ' + poster
                    lista.append(string)
            else:
                # Se acabar a lista
                print('\nBusca Finalizada!')
                break
        except Exception as e:
            print('\nERRO:', e)
    return lista


sair = False
while not sair:
    op = input('\nPesquise por um filme (em ingês) ou digite SAIR: ')
    if str.upper(op) == 'SAIR':
        sair = True
        print('\nBye....')
    else:
        lista_de_filmes = lista_filmes(op)
        print('\nFilmes encontrados com o título "{}": {}'.format(str.upper(op),len(lista_de_filmes)))
        for filme in lista_de_filmes:
            print('\n',filme)

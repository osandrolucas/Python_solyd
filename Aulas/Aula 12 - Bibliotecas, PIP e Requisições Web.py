import sys
import time
import requests
#beautiful soup 4 (BS4) para distrinchar uma pagina web, ver tudo direitinho

print('Pip --> Gerenciados de Pacotes do Python')

print('urllib é a biblioteca padrão para requisições do Python')
print('Requests é a mais Pop e a que o professor do curso prefere. É utilizada para requisições WEB')

print('''Requisição WEB, nada mais é do que entrar num site. Como assim? Por exemplo, entrar em google.com é 
fazer uma requisição ao google e ele dá um response com o site''')

print('Dois principais tipos de requisição: GET que é "pegar" informações e POST que geralmente é feito para postar, enviar informações.')

'''
texto = None
try:
    req = requests.get('http://g1.com.com')
    texto = req.text
    print('Texto de resposta da requisição...')
    print(texto)
except Exception as e:
    print('Erro na requisição:', e)

print(type(req), 'Código de resposta: ', req.status_code)
'''

print('\n\nUtilizado o site https://reqres.in/ para criar as requisições. O professor do Curso usou o putsreq mas no dia ele estava indisponivel.')

#Modificando o cabeçalho que passaremos.
cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com', #De onde veio o clique. É como se tivesse visitado o site através do google.
             'CF_IPCOUNTR':''}

#Cookies
meus_cookies = {'Ultima-visita': '10-09-2018'}

dados = {'name': 'sandro',
         'job': 'developer'}

resp1 = None
resp2 = None
try:
    req = requests.get('https://reqres.in/api/users/2')
    req2 = requests.post('https://reqres.in/api/users',
                         headers=cabecalho, #Passando o headers na requisição que é um dos padrões
                         cookies=meus_cookies,
                         data=dados)
    resp1 = req.text
    resp2 = req2.text
    print('\nTexto de resposta da requisição GET...')
    print(resp1)
    print('\nTexto de resposta da requisição POST...')
    print(resp2)
except Exception as e:
    print('Erro na requisição:', e)

print('\n', type(req), 'Código de resposta: ', req.status_code)




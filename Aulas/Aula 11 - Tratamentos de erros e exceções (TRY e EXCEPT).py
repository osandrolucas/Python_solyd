import time

#Sempre que for fazer algo que tenha a possibilidade de dar erro, colocar try exception
try:
    a = 12 / 0
except ZeroDivisionError as erro: #é possivel especificar o erro e dar alias para ele
    print('Não é possível fazer divisão por 0... Erro: {}'.format(erro))
except NameError:
    print('Você digitou algo errado...')

print('E segue a vida normal')

def abre_arquivo():
    try:
        open('Arquivex.txt')
        return True
    except Exception as err:
        print('Ocorreu um erro ao abrir o arquivo... Erro: {}'.format(err))
        return False

while not abre_arquivo(): #Enquanto estiver retornando False, executa de novo.
    print('Tentando abrir o arquivo')
    time.sleep(10) #Tenta de 10 em 10 segundos

print('Consegui abrir o arquivo')
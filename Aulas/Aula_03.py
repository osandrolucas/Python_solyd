#Coleções criadas para facilitar
cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'magenta': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',
         'pretoebranco': '\033[7;30m'
         }

estilos = {
    'none': '\033[m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'negative': '\033[m',
    'limpa': '\033[m'
}

back = {
        'limpa': '\033[m',
        'branco': '\033[40m',
        'vermelho': '\033[41m',
        'verde': '\033[42m',
        'amarelo': '\033[43m',
        'azul': '\033[44m',
        'magenta': '\033[45m',
        'ciano': '\033[46m',
        'cinza': '\033[47m',

}


'''
Aula 3 - Operadores lógicos e estruturas de decisões (IF e ELSE)
'''

var_verdadeiro = True
var_falso = False

if var_verdadeiro == True:
    print('var_verdadeiro é verdadeiro\n')

print('{}###{} {}Operadores{} {}Lógicos e{} {}Aritméticos{} {}###{}'.format(cores['vermelho'], cores['limpa'], cores['verde'], cores['limpa'], cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa'], cores['ciano'], cores['limpa']))
print(' if / elif / else (Se / Senão Se / Senão )')
print(' == (Igual)')
print(' != (Diferente)')
print(' > (Maior)')
print(' < (Menor)')
print(' >= (Maior Igual)')
print(' >= (Menor Igual)')
print('True / False / or / and / not (Operadores Lógicos)')

print('\nOpções:\n1 = Escreve Sandro\n2 = Escreve Lucas\n2 = Azevedo\n4 = Ferreira')
opcao = input('Escolha uma opção: ')

'''
Quando usar o elif termina a execução.
Quando usar o if pode entrar em mais de um.
'''
if opcao == '1':
    print('Sandro')
elif opcao == '2':
    print('Lucas')
elif opcao == '3':
    print('Azevedo')
elif opcao == '4':
    print('Ferreira')
else:
    print('Opção inválida')
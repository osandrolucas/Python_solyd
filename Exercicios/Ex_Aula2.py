'''
Comentário de várias linhas
Exercicio: Faça um formulário que pergunte o nome, CPF, Endereço, idade, altura e telefone
e imprima isso em um relatório organizado.
'''
print('''\nExercicio: Faça um formulário que pergunte o nome, CPF, Endereço, idade, altura e telefone
e imprima isso em um relatório organizado.''')
nome = input('Informe seu nome: ')
CPF = input('Informe seu CPF: ')
endereco = input('Informe seu Endereço: ')
idade = input('Informe sua idade: ')
altura = input('Informe sua altura: ')
telefone = input('Informe sua telefone: ')

print('#' * 3, 'Relatório', '#' * 3)
print('Nome: {}'.format(nome))
print('CPF: {}'.format(CPF))
print('Endereço: {}'.format(endereco))
print('Idade: {}'.format(idade))
print('Altura: {}'.format(altura))
print('Telefone: {}'.format(telefone))

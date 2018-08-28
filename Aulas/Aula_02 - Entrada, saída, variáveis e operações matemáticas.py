print('Hello Word!\nSegundo print com Quebra linha')
print('Hello Word!\tSegundo print com Tab\n')

print('#' * 3, 'Variáveis', '#' * 3)

nome = 'Sandro Lucas'
idade = 23
altura = 1.72

print('A variável NOME tem o valor de {} é do tipo {}'.format(nome, type(idade)))

print('A variável IDADE tem o valor de {} é do tipo {}'.format(idade, type(idade)))

print('A variável ALTURA é do tipo {}'.format(altura, type(altura)))

print('\nConcatenando com "," ...')
print(nome, 'tem', idade, 'anos e', altura, 'm de altura.')

print('\nConcatenando com "+" ...')
print(str(nome) + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' m de altura.')

print(
    '\nEm Python, a convenção para nome de variáveis é deixá-las em minusculo, e se forem grandes, separadas por "_"\n')

print('#'*3 , 'Usando Input' , '#' * 3)
nome2 = input('Escreva seu nome: ')
idade2 = input('Escreva sua idade: ')
altura2 = input('Escreva sua altura: ')
print(nome2, 'tem', idade2, 'anos e', altura2, 'm de altura.')
print(type(nome2), type(idade2), type(altura2))

n1 = 27
n2 = 53
n3 = 74.3
resultado = (n1 + n2) / n3 * 5
print(resultado)
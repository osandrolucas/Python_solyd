print('*    Criando uma lista de nomes')
nomes = ['Sandro', 'Soliman', 'Marcio', 'Fabiana']
palavra = 'Sandro Lucas'

print('*    Imprimindo lista --> {}'.format(nomes))

print('\n*    Imprimindo itens da lista com For:')
for i in nomes:
    print(i)

print('\nCriando lista de números com Range 10 a 20 (2 em 2) ')
lista_numeros = range(10, 20, 2)
print('*    Imprimindo itens da lista de números com For:')
for i in lista_numeros:  # Podemos usar o Range
    print(i)

print('\n*    Imprimindo cada letra do meu nome com For:')
for letra in palavra:
    print(letra)

print('\n*    Iterando i com While:')
i = 1
while i < 10:
    print('i ainda não é 10, ele vale: {}'.format(i))
    i += 1  # Não pode ser i++. Pode ser i = i + 1
print('Acabou o While. i vale: {}'.format(i))

lista_frutas = ['Melancia', 'Goiaba', 'João Bolão', 'Berga', 'Melão']

contador = 0

print('\n*    Imprimindo o número de elementos em uma lista, usando uma variável auxiliar...')
for fruta in lista_frutas:
    contador += 1

print(contador)

print('\n*    Usando Break no While...')
numero = 0
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1

print('Break, chegou em 20. Saiu do While.')


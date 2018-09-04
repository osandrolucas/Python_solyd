print('''Escreva uma função que recebe um objeto de coleção e retorna o valor do maior número dentro da coleção
Faça outra que retorna o menor número dessa coleção
''')

lista = [1,2,3,4,5,6,7]

def maior(a):
    maior = lista[0]
    for i in a:
        if i > maior:
            maior = i
    return maior

def menor(a):
    menor = lista[0]
    for i in a:
        if i < menor:
            menor = i
    return menor


print('Minha lista: {}'.format(lista))
print('Maior item: {}'.format(maior(lista)))
print('Menor item: {}'.format(menor(lista)))

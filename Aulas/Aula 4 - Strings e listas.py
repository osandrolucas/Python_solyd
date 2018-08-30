frase = ('Oi, tudo bem?')
print(frase)

lista_nomes = ['João', 'Maria', 'Guilherme', 'Diego']

print('\n*   Imprimindo lista    ')
print(lista_nomes)
print('\n*   Imprimindo lista com indice...')
print(lista_nomes[-1]) #Passamos o indice. Se passar um indice que não existe, dá erro.

print('\n*    Adicionando um nome na lista, no final dela....')
lista_nomes.append('Geralda')
print('Reimprimindo lista: {}'.format(lista_nomes))

print('\n*    Removendo o João...')
lista_nomes.remove('João')
print('Reimprimindo lista: {}'.format(lista_nomes))

print('\n*    Limpando a lista...')
lista_nomes.clear()
print('Reimprimindo lista, vazia: {}'.format(lista_nomes))

lista_nomes = ['João', 'Maria', 'Guilherme', 'Diego']

print('\n*    Inserindo na lista em determinado local da lista, no caso 1...')
lista_nomes.insert(1,'Cleosvaldo')
print('Reimprimindo lista: {}'.format(lista_nomes))

print('\n*    Transformando o indice 0 em Robervânia...')
lista_nomes[0] = 'Robervânia'
print('Reimprimindo lista: {}'.format(lista_nomes))

print('\n*    Idenrificando quantas vezes aparece Diego...')
contador_diego = lista_nomes.count('Diego')
print(contador_diego)

print('\n*    Usando o Pop, último da lista, função de pilha que limpa o último...')
print('Lista Antes: {}'.format(lista_nomes))
print(lista_nomes.pop())
print('Reimprimindo lista: {}'.format(lista_nomes))

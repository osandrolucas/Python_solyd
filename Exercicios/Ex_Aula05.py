print("""Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
         Após isso, o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados.
         Após isso, irá imprimir todos os nomes da lista\n""")

print('#*#' * 4, 'Controle do Festerê', '#*#' * 4)
qtd = int(input('Quantos convidados irão na sua festa: '))

nome_convidado = []

i = 0

for i in range(qtd):
    nome = input('Nome do convidado {}: '.format(i+1))
    nome_convidado.append(nome)
    i += i

i = 1
print('**** LISTA DE CONVIDADOS ****')
for convidado in nome_convidado:
    i += 1
    print('{}. --> {}'.format(i, convidado))

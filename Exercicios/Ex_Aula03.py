print("""
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela está apta 
a ser do Exército. Para entrar no exército é preciso ter mais de 18 anos, pesar no mínimo 60kg e 
medir no mínimo 1.70 metros.
""")

print('#*#' * 2, 'Teste para Entrar no Exército', '#*#' * 2)
nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('\nParabéns {}, você está apto para entrar no Exército!'.format(str.upper(nome)))
    print('Você tem: {} anos, {}kg e {} de altura.'.format(idade, peso, altura))
else:
    print('\nInfelizmente você não está apto para entrar no Exército')

if idade < 18:
    print('Você não possui a idade mínima que é 18 anos.')
if peso < 60:
    print('Você não possui o peso mínimo que é 60 kg.')
if altura < 1.70:
    print('Você não possui a altura mínima que é 1.70m.')
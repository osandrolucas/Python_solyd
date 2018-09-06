from PythonBasico_oo.veiculo import Veiculo
from PythonBasico_oo.carro import Carro

#Novo Objeto Veiculo

caminhao_rosa = Veiculo('rosa', 6, 'Ford', 10)

print('CAMINHÃO ROSA')
print('Cor: {}'.format(caminhao_rosa.cor))
print('Quantidade de Rodas: {}'.format(caminhao_rosa.rodas))
print('Marca: {}'.format(caminhao_rosa.marca))
print('Tanque: {}l'.format(caminhao_rosa.tanque))

#Novo Objeto Carro
carro_azul = Carro('Azul', 'bmw', 30)

print('CARRO AZUL')
print('\nCor: {}'.format(carro_azul.cor))
print('Quantidade de Rodas: {}'.format(carro_azul.rodas))
print('Marca: {}'.format(carro_azul.marca))
print('Tanque: {}l'.format(carro_azul.tanque))

carro_azul.abastecer(10)

print('Tanque após abastecer mais 10l: {}l'.format(carro_azul.tanque))
print('Tentando incluir mais 70 litros....')
carro_azul.abastecer(70)
print('Tanque: {}l'.format(carro_azul.tanque))

carro_juliano = Carro('ver','ford',30)





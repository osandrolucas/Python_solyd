print('''Crie um Software de gerenciamento bancário. Esse software deverá ser capaz de criar clientes e contas.
Cada cliente possiu nome, cpf, idade.
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo.''')

from Exercicios.Ex_Aula09_cliente import Cliente
from Exercicios.Ex_Aula09_conta import Conta

cliente1 = Cliente('Sandro', '123.456.789-10', 23)

print('\n{}'.format(cliente1))

conta1 = Conta(cliente1, 10.50, 1000)

print(conta1.consultar_saldo())

conta1.depositar(1000.00)

conta1.sacar(2500.00)
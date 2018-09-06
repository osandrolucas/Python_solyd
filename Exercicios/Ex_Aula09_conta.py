class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite #O limite é negativo

    def depositar(self, quant):
        if quant > 0:
            self.saldo += quant
            print('Foi feito um saque de R${}'.format(quant))
            print('Novo Saldo: R${}'.format(self.saldo))
        else:
            print('Erro, valor inferior a 0.')

    def consultar_saldo(self):
        return "Seu Saldo é de: " + str(self.saldo)

    def sacar(self, quant):
        if self.saldo - quant < self.limite:
            print('Saldo insuficiente para este saque!')
        else:
            self.saldo -= quant
            print('Foi sacado R${}'.format(quant))
            print('Novo Saldo: R${}'.format(self.saldo))

from PythonBasico_oo.veiculo import Veiculo

class Carro(Veiculo):


    #Toda vez que iniciar o carro, cria um veiculo
    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)

#Como rodas serão sempre 4, já deixamos o 4 ali.

    def abastecer(self, litros): #Se eu colocar o método abastecer aqui, ele irá sobrescrever o da classe mae
        if self.tanque + litros > 50: #Carro consegue no máximo 50 litros
            print('Erro: Tanque do carro possui capacidade máxima de 50 litros!')
        else:
            self.tanque += litros

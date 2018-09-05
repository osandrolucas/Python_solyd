#Classe geralmente começa com letra maiuscula
class Veiculo:

    #Este é o método construtor. Passa ele mesmo para dentro. Parece o This do Java
    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros
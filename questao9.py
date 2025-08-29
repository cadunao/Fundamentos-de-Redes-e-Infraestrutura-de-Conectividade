class Carro:
    def __init__(self, marca, modelo, cor, ano, valor, consumo):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo
        self.nivel = 0

    def abastecer(self, litros):
        self.nivel += litros

    def andar(self, distancia):
        gasto = distancia / self.consumo
        if self.nivel >= gasto:
            self.nivel -= gasto

    def verificar_nivel(self):
        return self.nivel

    def calcular_imposto(self):
        return self.valor * 0.035
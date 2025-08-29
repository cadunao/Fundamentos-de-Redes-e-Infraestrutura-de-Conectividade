class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def imprimir_raio(self):
        print(self.raio)

    def calcular_area(self):
        return 3.14159 * self.raio ** 2

    def calcular_circunferencia(self):
        return 2 * 3.14159 * self.raio

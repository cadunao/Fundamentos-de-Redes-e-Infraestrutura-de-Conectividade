class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcularPerimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def getMaiorLado(self):
        return max(self.ladoA, self.ladoB, self.ladoC)

    def Equilatero(self):
        return self.ladoA == self.ladoB == self.ladoC

    def Isosceles(self):
        return (self.ladoA == self.ladoB or self.ladoB == self.ladoC or self.ladoA == self.ladoC) and not self.Equilatero()

    def Escaleno(self):
        return self.ladoA != self.ladoB and self.ladoB != self.ladoC and self.ladoA != self.ladoC
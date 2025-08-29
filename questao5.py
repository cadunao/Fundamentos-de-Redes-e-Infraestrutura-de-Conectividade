class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nomeCompleto(self):
        print(f"{self.nome} {self.sobrenome}")

    def calcularSalario(self):
        print(self.horas_trabalhadas * self.valor_hora)

    def incrementarHoras(self, horas):
        self.horas_trabalhadas += horas

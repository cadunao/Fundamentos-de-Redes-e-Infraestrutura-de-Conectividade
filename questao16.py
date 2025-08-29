class FuncionarioBase:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def bater_ponto(self):
        self.pontos.append(1)

class Vendedor(FuncionarioBase):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao

    def bater_meta(self):
        print("Meta batida!")

class Gerente(FuncionarioBase):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha
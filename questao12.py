class PessoaBase:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

class AlunoHeranca(PessoaBase):
    def __init__(self, matricula, nome, idade, notas):
        super().__init__(matricula, nome, idade)
        self.notas = notas
        self.media = sum(notas) / len(notas)

    def calcular_media(self):
        return self.media

    def estudar(self):
        print("Estudando...")

class Professor(PessoaBase):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def lecionar(self):
        print("Lecionando...")

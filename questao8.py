class Aluno_Academia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120.00):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def Calcular_IMC(self):
        return self.peso / (self.altura ** 2)

    def Obter_valor_mensalidade(self):
        if self.idade < 18:
            return self.mensalidade * 0.9
        return self.mensalidade

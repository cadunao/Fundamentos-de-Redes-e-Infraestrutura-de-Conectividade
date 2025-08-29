class Brinquedo:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"Estou brincando com {self.nome}")

class Buzz(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está voando!")

class Woody(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está laçando!")

class Rex(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está rugindo!")

class Jessie(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está pulando!")

class Porquinho(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está economizando moedas!")
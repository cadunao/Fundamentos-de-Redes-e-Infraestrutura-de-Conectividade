class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def getNome(self):
        return self.nome

    def setIdade(self, nova_idade):
        self.idade = nova_idade

    def imprimeEndereco(self):
        print(f"Endereço: {self.endereco}")

p1 = Pessoa("Maria", 30, "Rua das Flores, 123")

print("Nome:", p1.getNome())    
p1.setIdade(31)                   
p1.imprimeEndereco()           
class PessoaSimples:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print("Negociação em andamento...")

class PessoaFisica(PessoaSimples):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

class PessoaJuridica(PessoaSimples):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

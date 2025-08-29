class Conta:
    def __init__(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def Depositar(self, valor):
        self.saldo += valor

    def Sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def Imprimir_saldo(self):
        print(self.saldo)
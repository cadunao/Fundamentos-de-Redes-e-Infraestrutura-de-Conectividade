class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

class ContaCorrente(ContaBancaria):
    pass

class ContaPoupanca(ContaBancaria):
    def render_juros(self, taxa):
        self.saldo += self.saldo * taxa

class FundoInvestimento(ContaBancaria):
    def aplicar_rendimento(self, rendimento):
        self.saldo += rendimento

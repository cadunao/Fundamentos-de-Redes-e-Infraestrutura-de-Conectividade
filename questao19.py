class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        self.valor_total = self.valor + (self.valor * 0.17) + (self.valor * 0.05)
        return self.valor_total

class CompraAvista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def calcular_valor_total(self):
        total = super().calcular_valor_total()
        return total - self.desconto

    def get_desconto(self):
        return self.desconto

    def set_desconto(self, valor):
        self.desconto = valor

class CompraParcelada(Compra):
    def __init__(self, numero, produto, valor):
        super().__init__(numero, produto, valor)

    def simular_numero_de_parcelas(self, parcelas):
        return self.calcular_valor_total() / parcelas
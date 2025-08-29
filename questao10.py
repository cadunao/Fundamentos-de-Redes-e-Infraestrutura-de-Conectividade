class NotaFiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, icms, frete, ipi, valor_produto):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_produto = valor_produto
        self.valor_total = 0

    def obterNumero(self):
        return self.numero

    def obterDataEmissao(self):
        return self.data

    def alterarRazaoSocial(self, nova_razao):
        self.razao_social = nova_razao

    def calcularValorTotal(self):
        self.valor_total = self.valor_produto + self.frete + self.icms + self.ipi
        return self.valor_total

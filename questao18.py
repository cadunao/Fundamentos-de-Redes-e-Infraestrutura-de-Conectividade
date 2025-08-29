class Imovel:
    def __init__(self, inscricao, valor_aluguel, iptu):
        self.inscricao = inscricao
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu

    def obter_parcela_IPTU(self):
        return self.iptu / 12

    def set_valor_aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor

class Casa(Imovel):
    def __init__(self, inscricao, valor_aluguel, iptu, piscina):
        super().__init__(inscricao, valor_aluguel, iptu)
        self.piscina = piscina

class Apartamento(Imovel):
    def __init__(self, inscricao, valor_aluguel, iptu, elevador):
        super().__init__(inscricao, valor_aluguel, iptu)
        self.elevador = elevador

class Terreno(Imovel):
    def __init__(self, inscricao, valor_aluguel, iptu, area_m2):
        super().__init__(inscricao, valor_aluguel, iptu)
        self.area_m2 = area_m2

class Chacara(Imovel):
    def __init__(self, inscricao, valor_aluguel, iptu, churrasqueira):
        super().__init__(inscricao, valor_aluguel, iptu)
        self.churrasqueira = churrasqueira

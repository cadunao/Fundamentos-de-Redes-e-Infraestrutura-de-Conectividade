class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def escolher_assento(self, novo_assento):
        self.assento = novo_assento

class PassagemAviao(Passagem):
    def __init__(self, preco, assento, porta_embarque, checkin):
        super().__init__(preco, assento)
        self.porta_embarque = porta_embarque
        self.checkin = checkin

    def decolar(self):
        print("Avião decolando...")

class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print("Abastecendo ônibus...")
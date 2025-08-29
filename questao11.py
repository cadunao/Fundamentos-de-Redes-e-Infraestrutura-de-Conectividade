class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print(f"Play no filme {self.nome}")


class Acao(Filme):
    def explodir(self):
        print("Explosão em cena!")


class Drama(Filme):
    def chorar(self):
        print("Muita emoção e lágrimas...")


class Suspense(Filme):
    def assustar(self):
        print("Momento de tensão!")
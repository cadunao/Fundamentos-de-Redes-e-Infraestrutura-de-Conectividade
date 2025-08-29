class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def Alterar_editora(self, nova_editora):
        self.editora = nova_editora

    def Listar_qtde_paginas(self):
        return self.paginas

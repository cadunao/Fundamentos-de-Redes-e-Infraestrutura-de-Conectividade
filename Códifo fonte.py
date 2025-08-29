class Paciente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}"


class Prescricao:
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return f"Prescrição: {self.descricao}"


from prescricao import Prescricao

class Consulta:
    def __init__(self, paciente, data, prescricao):
        self.paciente = paciente  # Composição
        self.data = data
        self.prescricao = prescricao

    def __str__(self):
        return f"Consulta de {self.paciente.nome} em {self.data}: {self.prescricao}"


class Clinica:
    def __init__(self):
        self.consultas = []

    def adicionar_consulta(self, consulta):
        self.consultas.append(consulta)

    def listar_consultas(self):
        return [str(consulta) for consulta in self.consultas]


from paciente import Paciente
from prescricao import Prescricao
from consulta import Consulta
from clinica import Clinica

clinica = Clinica()

def salvar_dados(consulta):
    with open('dados.txt', 'a') as arquivo:
        arquivo.write(str(consulta) + '\n')

def menu():
    while True:
        print("\n1 - Cadastrar Consulta")
        print("2 - Listar Consultas")
        print("3 - Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            nome = input("Nome do paciente: ")
            idade = input("Idade: ")
            cpf = input("CPF: ")
            data = input("Data da consulta: ")
            descricao = input("Descrição da prescrição: ")

            paciente = Paciente(nome, idade, cpf)
            prescricao = Prescricao(descricao)
            consulta = Consulta(paciente, data, prescricao)
            clinica.adicionar_consulta(consulta)
            salvar_dados(consulta)
            print("Consulta cadastrada com sucesso!")

        elif opcao == '2':
            for c in clinica.listar_consultas():
                print(c)

        elif opcao == '3':
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()

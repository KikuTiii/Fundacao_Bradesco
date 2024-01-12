# Crie uma classe Estudante que herda da classe Pessoa. Adicione um atributo adicional chamado curso à classe Estudante.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f"Olá, meu nome é " + self.nome)

class Estudante(Pessoa):
    def __init__(self, nome, idade,curso):
        super().__init__(nome, idade)
        self.curso = curso

    def estudar(self):
        print(f"{self.nome} esta estudando {self.curso}")

class Main():
    estudante = Estudante("Kikuti", 19, "Python")
    estudante.cumprimentar()
    estudante.estudar()
    print(estudante.nome)
    print(estudante.idade)
    print(estudante.curso)
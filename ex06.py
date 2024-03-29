# Múltipla Herança:
# Crie uma classe Trabalhador que tenha um atributo cargo. Em seguida, crie uma classe Funcionario que herda tanto de Estudante quanto de Trabalhador.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome}")

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def estudar(self):
        print(f"{self.nome} está estudando {self.curso}")

class Trabalhador(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def trabalhar(self):
        print(f"{self.nome} está trabalhando como {self.cargo}")

class Funcionario(Estudante, Trabalhador):
    def __init__(self, nome, idade, curso, cargo):
        Pessoa.__init__(self, nome, idade)  # Chama o construtor de Pessoa
        self.curso = curso
        self.cargo = cargo

# Exemplo de uso:
funcionario = Funcionario("Kikuti", 19, "Engenharia de software", "Software engineer")
funcionario.cumprimentar()  # Método da classe Pessoa
funcionario.estudar()      # Método da classe Estudante
funcionario.trabalhar()    # Método da classe Trabalhador


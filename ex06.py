# Múltipla Herança:
# Crie uma classe Trabalhador que tenha um atributo cargo. Em seguida, crie uma classe Funcionario que herda tanto de Estudante quanto de Trabalhador.

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome_privado = nome
        self.__idade_privado = idade

    def obter_atributo_privado(self):
        return self.__nome_privado, self.__idade_privado
    
    def modificar_atributo_privado(self, novo_nome, nova_idade):
        self.__nome_privado = novo_nome
        self.__idade_privado = nova_idade

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.__nome_privado}")

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def estudar(self):
        print(f"{self.__nome_privado} está estudando {self.curso}")

class Trabalhador(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

class Funcionario(Estudante, Trabalhador):
    def __init__(self, nome, idade, curso, cargo):
        # Chame os construtores das classes pai corretamente
        Estudante.__init__(self, nome, idade, curso) #construtor sao os metodos __init__ das classes
        Trabalhador.__init__(self, nome, idade, cargo)

        # Utilize os métodos de acesso para atributos privados
        nome, idade = self.obter_atributo_privado()
        print(f"{nome} é um {self.cargo}")

class Main:
    estudante = Estudante("Kikuti", 19, "Python")
    estudante.cumprimentar()
    estudante.estudar()

    funcionario = Funcionario("Kikuti", 19, "Python", "Programador")

    # Acesso aos atributos privados usando os métodos
    nome, idade = estudante.obter_atributo_privado()
    print(nome)
    print(idade)

    # Modificando os atributos privados
    estudante.modificar_atributo_privado("Mathheus Kikuti", 20)
    nome, idade = estudante.obter_atributo_privado()
    print(nome)
    print(idade)

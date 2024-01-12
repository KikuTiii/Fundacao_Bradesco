# Modifique a classe Pessoa para tornar os atributos nome e idade privados e adicione métodos para obter e definir esses atributos de forma segura.

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome_privado = nome #atributo privado criado com __ antes do nome
        self.__idade_privado = idade

    def obter_atributo_privado(self):
        return self.__nome_privado, self.__idade_privado
    
    def modificar_atributo_privado(self, novo_nome, nova_idade):
        self.__nome_privado = novo_nome
        self.__idade_privado = nova_idade

    def cumprimentar(self):
        print(f"Olá, meu nome é " + self.__nome_privado)

class Estudante(Pessoa):
    def __init__(self, nome, idade,curso):
        super().__init__(nome, idade)
        self.curso = curso

    def estudar(self):
        print(f"{self.__nome_privado} esta estudando {self.curso}")

class Main():
    estudante = Estudante("Kikuti", 19, "Python")
    estudante.cumprimentar()
    estudante.estudar()

    #nao da pra printar pois os atributos sao privados, entao usamos o metodo obter_atributo_privado
    nome, idade = estudante.obter_atributo_privado()
    print(nome)
    print(idade)

    #modificando os atributos privados
    estudante.modificar_atributo_privado("Mathheus kikuti", 20)
    nome, idade = estudante.obter_atributo_privado()
    print(nome)
    print(idade)
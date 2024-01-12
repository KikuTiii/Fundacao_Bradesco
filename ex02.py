# 1. Crie uma classe chamada Animal com alguns atributos e métodos relacionados a animais. Em seguida, crie objetos dessa classe para representar diferentes tipos de animais.

class Animal:
    def __init__(self,nome, idade, cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor

    def comer(self):
        print("O animal está comendo")

    def dormir(self):
        print("O animal está dormindo")

    def correr(self):
        print("O animal está correndo")


class main():
    animal = Animal("Cachorro", 3, "Preto")
    print(animal.nome)
    print(animal.idade)
    print(animal.cor)
    animal.comer()
    animal.correr()
    animal.dormir()
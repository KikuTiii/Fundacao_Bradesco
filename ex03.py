# Modele uma classe ContaBancaria com atributos como titular, saldo e métodos como depositar e sacar. Crie instâncias dessa classe e realize operações de depósito e saque.

class ContaBancaria:
    def __init__(self):
        self.titular = ""
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self,valor):
        self.saldo -= valor

class main ():
    conta = ContaBancaria()
    conta.titular = "João"
    conta.saldo = 1000
    print(conta.titular)
    print(conta.saldo)
    conta.depositar(100)
    conta.sacar(50)
    print(conta.saldo)
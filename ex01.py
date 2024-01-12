class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.saldo = 0
        self.numero = numero
        self.titular = titular
        self.limite = limite

class main:
    conta = Conta(123, "João", 100.0, 1000.0)
    print(conta.saldo)
    print(conta.numero)
    print(conta.titular)
    print(conta.limite)


# trabalhando com classes em python
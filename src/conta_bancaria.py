class ContaBancaria:
    def __init__(self, numero_conta, titular, senha, saldo = 0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.senha = senha
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')
        else:
            print('Valor de saque inválido ou saldo insuficiente.')

    def consultar_saldo(self):
        print(f'Saldo da conta {self.numero_conta} de {self.titular}: R${self.saldo}')

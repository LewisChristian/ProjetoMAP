from conta_bancaria import ContaBancaria

from random import randint
from time import sleep
import sys
import os
clear = lambda: os.system('clear')

class SistemaBancario:
    def __init__(self):
        self.contas = []

    def gerar_numero_conta(self):
        numero_conta = randint(1000, 9999)
        while self.conta_existente(numero_conta):
            numero_conta = randint(1000, 9999)
        return numero_conta

    def criar_conta(self):
        titular = input('Digite seu nome: ')
        numero_conta = self.gerar_numero_conta()
        senha = input('Digite a senha da conta: ')
        saldo = 0
        conta = ContaBancaria(numero_conta, titular, senha, saldo)
        self.contas.append(conta)

        clear()
        
        print(f'Conta criada com sucesso!\n{titular}\nConta: {numero_conta}\nSenha: {senha}\nSaldo: {saldo}')

    def conta_existente(self, numero_conta):
        return any(conta.numero_conta == numero_conta for conta in self.contas)

    def acessar_conta(self):
        numero_conta = int(input('Digite o número da conta: '))
        senha = input('Digite a senha da conta: ')

        for conta in self.contas:
            if conta.numero_conta == numero_conta and conta.senha == senha:
                return conta

        print('Conta não encontrada ou senha incorreta.')
        return None

    def menu_conta(self, conta):
        while True:
            print('\n===== Menu da Conta =====')
            print(f'{conta.titular}\nConta: {conta.numero_conta}\nSaldo: {conta.saldo}')
            print('\n1 - Depositar')
            print('2 - Sacar')
            print('3 - Consultar Saldo')
            print('4 - Realizar Transação')
            print('0 - Voltar para o Menu Principal')

            opcao_conta = input('Escolha a opção:\n>> ')

            if opcao_conta == '1':
                valor_deposito = float(input('Digite o valor a depositar:\n>>'))
                conta.depositar(valor_deposito)
            elif opcao_conta == '2':
                valor_saque = float(input('Digite o valor a sacar:\n>>'))
                conta.sacar(valor_saque)
            elif opcao_conta == '3':
                conta.consultar_saldo()
            elif opcao_conta == '4':
                self.realizar_transacao(conta)
            elif opcao_conta == '0':
                break
            else:
                print('Opção inválida. Tente novamente.')

    def realizar_transacao(self, conta_origem):
        numero_conta_destino = int(input('Digite o número da conta de destino: '))

        conta_destino = next((conta for conta in self.contas if conta.numero_conta == numero_conta_destino), None)

        if conta_destino is not None:
            valor_transferencia = float(input('Digite o valor da transferência: '))

            if conta_origem.sacar(valor_transferencia):
                conta_destino.depositar(valor_transferencia)
                print(f'Transferência de R${valor_transferencia} realizada para a conta de {conta_destino.titular}.')
            else:
                print('Transferência não realizada. Saldo insuficiente na conta de origem.')
        else:
            print('Conta de destino não encontrada.')

    def listar_contas(self):
        print("\n===== Contas Cadastradas =====")
        for conta in self.contas:
            print(f"Titular: {conta.titular} - Conta {conta.numero_conta} - Saldo: R${conta.saldo:.2f}")

    def menu_principal(self):

        while True:
            print('\n===== Menu Principal =====')
            print('1 - Criar conta')
            print('2 - Acessar conta')
            print('3 - Listar contas')
            print('4 - Sair')

            escolha = input('Escolha uma opção:\n>> ')

            if escolha == '1':
                clear()
                self.criar_conta()
            elif escolha == '2':
                clear()
                conta = self.acessar_conta()
                if conta:
                    self.menu_conta(conta)
            elif escolha == '3':
                clear()
                self.listar_contas()
            elif escolha == '4':
                print('Saindo do sistema.')
                sleep(2)
                sys.exit()
            else:
                print('Opção inválida. Tente novamente.')
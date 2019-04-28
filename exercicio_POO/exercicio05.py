"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

 >>> conta = ContaCorrente(123456, 'Carlos José',saldo= 1500)
>>> conta.numeroDaConta
123456
>>> conta.nomeDoCorrentista
'Carlos José'
 >>> conta.alterarNome('jose da silva')
>>> conta.nomeDoCorrentista
'jose da silva'
>>> conta.mostrarSaldo()
'saldo disponivel 1500'
>>> conta.déposito(100)
>>> conta.saldo
1600
>>> conta.saque(500)
>>> conta.saldo
Saque Liberado
>>> conta.saque(2000)
>>> conta.saldo
Saldo insuficiente para o valor do saque solcitiado. Saldo disponível para saque é de R$ 1100

"""

class ContaCorrente:
    def __init__(self, numeroDaConta: int,nomeDoCorrentista: str, saldo:int =0):
        self.numeroDaConta = numeroDaConta
        self.nomeDoCorrentista = nomeDoCorrentista
        self.saldo = saldo
        #self.trasacoes = []



    def alterarNome(self, nome ):
            self.nomeDoCorrentista = nome

    def mostrarSaldo(self):
       return f'saldo disponivel {self.saldo}'
    def déposito(self, valor ):
        self.saldo += valor
        #self.trasacoes.append(['deposito'], valor)

    def saque(self, valor):
        if valor > self.saldo:
            return f'Saldo insuficiente para o valor do saque solcitiado. Saldo disponível para saque é de R${self.saldo}'
        else:
            self.saldo -= valor
            return f'Saque Liberado'

    def extrato(self):
        print('-' * 10, 'Extrato financeiro', '-' * 10)
        for op in self.trasacoes:
            print(f'{op[0]}: {op [1]}')
        print(f'Saldo disponivel: {self.saldo}')
if __name__ == "__main__":
    cc =ContaCorrente
    print(cc.saque(500))
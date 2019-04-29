"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

a. Atributos: Nome, Fome, Saúde e Idade
b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

>>> t1= BichinhoVirtual('Jose')
>>> t1.Nome
'Jose'
>>> t1.Fome
0
>>> t1.Saude
0
>>> t1.Idade
0
>>> t1.alterarNome('Joao')
>>> t1.Nome
'Joao'
>>> t1.Fome
0
>>> t1.alterarFome(0)
>>> t1.Fome
3
>>> t1.alterarSaude(5)
>>> t1.Saude
10
>>> t1.humor()
6.5

"""

class BichinhoVirtual:


    def __init__(self, nome_bichinho : str):
        self.Nome = nome_bichinho
        self.Fome = 0
        self.Saude = 0
        self.Idade = 0

    def alterarNome(self,novo_nome):
       self.Nome = novo_nome
    def alterarFome(self, sensacaoFome):
        sensacaoFome += 3
        self.Fome = sensacaoFome

    def alterarSaude(self, estadoSaude):
        estadoSaude += 5
        self.Saude = estadoSaude
    def alterarIdade(self, tempoDeVida):
        tempoDeVida += 1
        self.Idade = tempoDeVida
        pass
    def retornarNome(self):
        print(self.Nome)
    def retornarFome(self):
        return self.Fome
    def retornar_saude(self):
        pass
    def retornar_idade(self):
        pass
    def humor(self):
        indiceHumor = (self.Fome + self.Saude)/2
        return indiceHumor
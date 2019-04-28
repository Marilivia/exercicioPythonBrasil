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
"""
class BichinhoVirtual:
    def __init__(self,nome_bichinho : str):
        self.Nome = nome_bichinho
        self.Fome = 0
        self.Saude = 0
        self.Idade = 0

    def alterarNome(self,novo_nome):
       self.Nome = novo_nome
    def alterarFome(self):
        pass
    def alterarSaude(self):
        pass
    def alterarIdade(self):
        pass
    def retornar_nome(self):
        pass
    def retornar_fome(self):
        pass
    def retornar_saude(self):
        pass
    def retornar_idade(self):
        pass
    def humor(self):
        pass
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
>>> t1.sensacaoFome
Faminto
>>> t1.alterarFome()
>>> t1.sensacaoFome
com muita fome
>>> t1.alterarFome()
>>> t1.sensacaoFome
fome
>>> t1.alterarFome()
>>> t1.sensacaoFome
pensando em comida
>>> t1.alterarFome()
>>> t1.sensacaoFome
com energia suficiente
>>> t1.alterarFome()
>>> t1.sensacaoFome
satisfeito
>>> t1.alterarFome()
>>> t1.sensacaoFome
cheio

>>> t1.retornar_fome()
>>> t1.Fome
7
"""
escalaFome = ['Faminto', ' com muita fome', 'fome', 'Pensando em comida',
                  'com energia suficiente', 'satisfeito', 'cheio']
class BichinhoVirtual:


    def __init__(self, nome_bichinho : str):
        self.Nome = nome_bichinho
        self.Fome = 0
        self.sensacaoFome = escalaFome[self.Fome]
        self.Saude = 0
        self.Idade = 0

    def alterarNome(self,novo_nome):
       self.Nome = novo_nome
    def alterarFome(self):
      self.Fome = (self.Fome + 1)%len(escalaFome)
      self.sensacaoFome = escalaFome[self.Fome]
    def alterarSaude(self):
        pass
    def alterarIdade(self):
        pass
    def retornarNome(self):
        print(self.Nome)
    def retornar_fome(self):
        print(self.Fome)
    def retornar_saude(self):
        pass
    def retornar_idade(self):
        pass
    def humor(self):
        pass
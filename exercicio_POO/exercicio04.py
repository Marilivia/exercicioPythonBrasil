"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

>>> pessoa = Pessoa ()
>>> pessoa.evenlhecer()
>>> pessoa.idade
11
>>> pessoa.altura
1.5
>>> pessoa.engordar()
>>> pessoa.peso
51
>>> pessoa.emagrecer()
>>> pessoa.peso
50
"""

class Pessoa:

    def __init__(self):
        self.nome = ''
        self.idade = 10
        self.peso = 50
        self.altura = 1.0
    def evenlhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5
    def engordar(self):
        self.peso += 1
    def emagrecer(self):
        self.peso -= 1
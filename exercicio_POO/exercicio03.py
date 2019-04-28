"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""

class Retangulo:
    def __init__(self,LadoA = 0, LadoB=0, lag = 0 , h = 0):
        self.base = LadoA
        self.altura = LadoB
        self.largura = lag
        self.h = h
    def mudarValoresLados(self):
        p = input('quer mudar o valor de algum lado[s/n]? ').upper().strip()
        if p == 'S':
            novo_ladoA= float(input('novo valor para lado A: '))
            self.base = novo_ladoA
            novo_ladoB = float(input('novo valor para Lado B: '))
            self.altura = novo_ladoB
    def mostrarValorLados(self):
       print(f'novo valor para cumprimento{self.base}')
       print(f'novo valor para altura {self.altura}')
    def calcularPerimentro(self):
        per = 2*(self.base) + 2*(self.altura)
        return per
    def calcularArea(self):
        A = self.base * self.altura
        return  A
    def calcularAreaLocal(self):
        self.Al = self.largura*self.h
        return self.Al
    #def calculoPiso(self):
       #calc = self.Al/

if __name__ == '__main__':
   r = Retangulo(3,4)
   print(r.mudarValoresLados())
   print(r.mostrarValorLados())
   print(r.calcularArea())
   print(r.calcularPerimentro())
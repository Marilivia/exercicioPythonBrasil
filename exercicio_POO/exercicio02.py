"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado :
    def __init__(self,lado = 0):
        self.lado = lado
    def mudarLado(self):
        mudar = input('deseja mudar o valor da lado[s/n]?').strip().upper()[0]
        if mudar == 'S':
            novo_lado = int(input('informe o novo valor do lado: '))
            self.lado = novo_lado
    def mostraLado(self):
        print(f'valor atribuido ao lado é : {self.lado}')
    def calcularAreaDoQuadrado(self):
        A= self.lado**2
        return A

if __name__ == '__main__':
    q = Quadrado(2)
    print(q.mudarLado())
    print(q.mostraLado())
    print(q.calcularAreaDoQuadrado())
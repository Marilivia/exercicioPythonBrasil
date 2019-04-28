"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""

class Bola:
    Pi = 3.14

    def __init__(self, circunferencia = 0, material= 'unknown',cor= 'unknown'):
        self.cor = cor
        self.circunferencia = circunferencia
        self. material = material
    def trocarCor (self):
        troca_cor = input('deseja trocar a cor da bola [s/n]? ').strip().upper()
        if troca_cor == 'S':
            nova_cor = input('digite a nova cor: ')
            self.cor = nova_cor
        else:
            print(f'cor continua {self.cor}')

    def mostraCor (self):
        print(f'cor alterada para:  {self.cor}')
    def calcularAreaCicunferencia(self):
        calcular = input('deseja calcular area da circunferencia [s/n]? ').upper().strip()
        if calcular == 'S':
            A = (4*Bola.Pi**self.circunferencia)
            return A


if __name__ == '__main__':

    # bola1 = Bola(3,'plástico', 'azul')
    # print(bola1.cor)
    # print(bola1.trocarCor())
    # print(bola1.mostraCor())
    for i in range(2):
        bola2 =Bola(3,'couro','vermelho')
        print(bola2.trocarCor())
print(bola2.mostraCor())
print(bola2.calcularAreaCicunferencia())
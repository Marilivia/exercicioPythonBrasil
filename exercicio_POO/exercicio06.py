"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
>>> tv = Televisao(1,0)
>>> tv.canal
1
>>> tv.volume
0
>>> tv.muda_canal(2)
>>> tv.canal
2
>>> tv.aumenta_volume(10)
>>> tv.volume
10
>>> tv.diminuir_volume(0)
>>> tv.volume
0

"""

class Televisao:
   def __init__(self,canal:int, volume:int):
       """
       atributos d
       :param canal : é inteiro e deve digitado pelo usuário
       :param volume:  é inteiro e deve digitado pelo usuário
       """

       self.canal = canal
       self.volume = volume
       self.canais = [1,2,3,4,5,6,7,8,9,10]
       self.nivel_volume = [0,1,2,3,4,5,6,7,8,9,10]

   def muda_canal(self, novo_canal):
       """
       :param novo_canal: novo valor atribuido pelo usuário
       se o novo_canal estiver dentro da faixa de canais
       self.canal = novo_canal
       :return:
       """
       if novo_canal in self.canais:
           self.canal = novo_canal
       else:
           return f'canal indisponível'

   def aumenta_volume(self,volume_maior):
       """
       funçao para aumentar o volume da tv
       :param volume_maior: aumentar o volume da tv
       :return: caso o valor do informado do volume esteja fora da faixa retorna uma msg volume max é   10
       """
       if volume_maior in self.nivel_volume:
           self.volume = volume_maior
       else:
           return f'volume máximo é 10'
   def diminuir_volume(self,volume_menor):
       if volume_menor in self.nivel_volume:
           self.volume = volume_menor
       else:
           return f' mudo '

   #if __name__ == "__main__":
      # tv = Televisao(1,0)
       #tv.mudarCanal()


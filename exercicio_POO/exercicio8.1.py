
"""
Classe Posto de Gasolina  vai ser responsavel por gerenciar preços dos combustiveis
Classe bomba_de_combustivel gerencia os abastecimentos
>>> posto = PostoDeCombustivel()
>>> posto.abastecimento_com_alcool_litro(20,3.09)
>>> posto.abastecimento_com_alcool_valor(200,3.09)
>>> posto.abastecimento_com_diesel_litro(30,2.89)
>>> posto.abastecimento_com_diesel_valor(100,2.89)
>>> posto.abastecimento_com_gasolina_litro(40,4.09)
>>> posto.abstecimentos_com_gasolina_valor(200,4.09)
>>> posto.totalizador_abasteciemntos_gasolina()
'qtide abastecimentos :2  total de litros:88.90 total em R$: 363.6'
"""





class PostoDeCombustivel():
    def __init__(self):
        self.bombas = Bombas()
        self.combustiveis = Combustiveis()

    def abstecimentos_com_gasolina_valor(self ,vl_abs ,vl_comb):
        self.bombas.abastercer_com_gasolina_por_valor(vl_abs ,vl_comb)


    def abastecimento_com_gasolina_litro(self ,litros ,vl_comb):
        return self.bombas.abastecer_com_gasolina_por_litro(litros ,vl_comb)

    def abastecimento_com_alcool_valor(self ,vl_abs ,vl_comb):
        return self.bombas.abastercer_com_alcool_por_valor(vl_abs ,vl_comb)

    def abastecimento_com_alcool_litro(self ,litros ,vl_comb):
        return self.bombas.abastecer_com_alcool_por_litro(litros ,vl_comb)

    def abastecimento_com_diesel_valor(self ,vl_abs ,vl_comb):
        return self.bombas.abastercer_com_diesel_por_valor(vl_abs ,vl_comb)

    def abastecimento_com_diesel_litro(self ,litros ,vl_comb):
        return self.bombas.abastecer_com_diesel_por_litro(litros ,vl_comb)


    def totalizador_abasteciemntos_gasolina(self):
        return self.bombas.totalizador_abastecimetos_gasolina()

    def totalizador_abastecimentos_alcool(self):
        return self.bombas.totalizador_abastecimnetos_alcool()



import sqlite3

conn = sqlite3.connect('DadosCombustivel.db')
c = conn.cursor()

c.execute('PRAGMA table_info({})'.format('DadosCombustivel.db'))

colunas = [tupla[1] for tupla in c.fetchall()]
print('Colunas:', colunas)
# ou
# for coluna in colunas:
#    print(coluna)

# listando as tabelas do bd

conn.commit()

class Combustiveis():
    pass
class Bombas():
    def __init__(self):
        self.tanque_gasolina = 10000
        self.tanque_alcool = 10000
        self.tanque_diesel = 10000
        self.valor_abastecimento = 0
        self.valor_combustivel = 0
        self.litros = 0
        self.abs = 0
        self._abastecimentos_gasolina = []
        self._abastecimentos_alcool = []
        self._abastecimentos_diesel = []
        self.combustiveis = Combustiveis()


    def abastercer_com_gasolina_por_valor(self ,vl_abst ,vl_comb):
        self.valor_abastecimento = vl_abst
        self.valor_combustivel = vl_comb
        self.abs = self.valor_abastecimento /self.valor_combustivel
        self._abastecimentos_gasolina.append(self.abs)
        self.tanque_gasolina -= self.abs


    def abastecer_com_gasolina_por_litro(self ,litros ,vl_comb):
        self.litros = litros
        self.valor_abastecimento = vl_comb
        self.abs = self.litros *self.valor_combustivel
        self._abastecimentos_gasolina.append(self.litros)
        self.tanque_alcool -= self.abs


    def abastercer_com_alcool_por_valor(self ,vl_abs ,vl_comb):
        self.valor_abastecimento = vl_abs
        self.valor_combustivel = vl_comb
        self.abs = self.valor_abastecimento /self.valor_combustivel
        self._abastecimentos_alcool.append(self.abs)
        self.tanque_alcool -= self.abs


    def abastecer_com_alcool_por_litro(self ,litros ,vl_comb):
        self.litros = litros
        self.valor_abastecimento = vl_comb
        self.abs = self.litros *self.valor_combustivel
        self._abastecimentos_alcool.append(self.litros)
        self.tanque_alcool -= self.abs


    def abastercer_com_diesel_por_valor(self ,vl_abs ,vl_comb):
        self.valor_abastecimento = vl_abs
        self.valor_combustivel = vl_comb
        self.abs = self.valor_abastecimento /self.valor_combustivel
        self._abastecimentos_diesel.append(self.abs)
        self.tanque_diesel -= self.abs


    def abastecer_com_diesel_por_litro(self ,litros ,vl_comb):
        self.litros = litros
        self.valor_abastecimento = vl_comb
        self.abs = self.litros *self.valor_combustivel
        self._abastecimentos_diesel.append(self.litros)
        self.tanque_diesel -= self.abs


    def totalizador_abastecimetos_gasolina(self):
        return f'qtide abastecimentos :{len(self._abastecimentos_gasolina)}  total de litros:{sum(self._abastecimentos_gasolina):.2f} total em R$: {sum(self._abastecimentos_gasolina ) *4.09}'


    def totalizador_abastecimnetos_alcool(self):
        return f'qtide abastecimetentos alcool: {len(self._abastecimentos_alcool)} total de litros:{sum(self._abastecimentos_alcool):.2f} total em R$:{sum(self._abastecimentos_alcool)*3.09} '
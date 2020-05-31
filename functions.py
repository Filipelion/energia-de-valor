from banco import *

class Eletronico:

    def __init__(self, nome, watts):
        self.__nome = nome
        self.__watts = watts
        self.__kwh_preco = 0.77336892

    def getNome(self):
        return self.__nome

    def getWatts(self):
        return self.__watts

    def getKwh_preco(self):
        return self.__kwh_preco

    def setNome(self, nome):
        self.__nome = nome

    def setWatts(self, watts):
        self.__watts = watts

    def setKwh_preco(self, kwh_preco):
        self.__kwh_preco = kwh_preco

    def preco_hora(self):
        aparelho = kwh(self.__watts)
        return aparelho * self.__kwh_preco



def add_aparelho():
    nome_eletronico = input("Digite o nome do equipamento: ")
    equipamento_potencia = float(input("Digite a potência do equipamento: "))

    return Eletronico(nome_eletronico, equipamento_potencia)

def get_preco_atual(obj_aparelho):

    print(f"O preço atual do KMH é de: R${obj_aparelho.getKwh_preco()}")
    alterar_preco_kwh = input("Alterar preço do KWH? [s/n] : ").lower()
    if alterar_preco_kwh == "s":
        kwh_preco = float(input("Digite o preço do kwh: "))
        obj_aparelho.setKwh_preco(kwh_preco)


def colocar_tela(obj_aparelho):
    produto = obj_aparelho.getNome()
    valor_kwh = obj_aparelho.preco_hora()
    return "\n %s - Custa R$ %.2f por hora" % (produto, valor_kwh)

def inicial():
    objt = add_aparelho()
    get_preco_atual(objt)
    tela = colocar_tela(objt)
    print(tela)

kwh = lambda a: a / 1000
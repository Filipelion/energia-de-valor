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


kwh = lambda a: a / 1000
from funcions import *
import sqlite3

nome_eletronico = input("Digite o nome do equipamento: ")
equipamento_potencia = int(input("Digite a potência do equipamento: "))

obj_telefone = Eletronico(nome_eletronico, equipamento_potencia)

alterar_preco_kwh = input("Alterar preço do KWH? [s/n] : ").lower()
if alterar_preco_kwh == "s":
    kwh_preco = float(input("Digite o preço do kwh: "))
    obj_telefone.setKwh_preco(kwh_preco)
else:
    pass

produto = obj_telefone.getNome()
valor_kwh = obj_telefone.preco_hora()
print("\n %s - R$ %.2f/h" %(produto, valor_kwh))

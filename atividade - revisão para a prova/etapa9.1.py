from classes import Banco
banco1 = Banco("Inter")
print(banco1.get_nome())
# testando verificações
print(banco1._Banco__validar_nome("ee"))
print(banco1._Banco__validar_nome("Santander"))
banco1.set_nome("Santander")
print(banco1.get_nome())
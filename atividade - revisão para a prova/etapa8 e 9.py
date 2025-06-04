from classes import Banco
banco1 = Banco("Nubank")
print(banco1.get_nome())
banco1.set_nome("Itaú")
print(banco1.get_nome())

#testando verificação:
banco1.set_nome("   ")
banco1.set_nome(123)
banco1.set_nome("bb")

#se a verificação mudar criamos uma função apenas para validar o novo_nome e utilizamos o set para alterar.
from classes import Banco
santander = Banco("Santander")
#print(santander.__nome)

print(santander._Banco__nome)

#esconder os dados é importante para evitar que partes externas do código alterem informações privadas diretamente (ex: senhas, saldo bancário). Reduz a chance de erros ao modificar o código. Torna o código mais limpo, seguindo os princípios da programação orientada a objetos.
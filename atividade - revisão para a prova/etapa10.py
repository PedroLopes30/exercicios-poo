from classes import Cliente, Conta
cliente1 = Cliente("Demetrios", "123.456.789-10")
cliente2 = Cliente("Carlos", "555.666.777-88")
conta1 = Conta(123, cliente1, 0)
conta2 = Conta(456, cliente2, 0)
conta1.depositar(500)
conta2.depositar(300)

conta1.sacar(100)
conta1.mostrar_saldo()  
conta2.mostrar_saldo()
print(Conta.total_contas) # total de contas 

# os atributos privados evitam alterações diretas nos dados, sendo elas acidentais ou maliciosas, as verificações nos métodos impedem erros (ex: nome inválido, saque maior que o saldo, depositar somente valores positivos ). Cada classe tem uma função clara e sua própria reponsabilidade, Cliente: cuida do nome e CPF; Conta: cuida do dinheiro e das regras bancárias.





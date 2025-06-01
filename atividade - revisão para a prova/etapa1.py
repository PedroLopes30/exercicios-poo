from livro import Livro

livro1 = Livro("A Metamorfose", "Franz Kafka", 1915)
livro2 = Livro("Noites Brancas", "Fiódor Dostoiévski", 1848)


print(f'{livro1.titulo} - {livro1.autor} - {livro1.ano}')
print(f'{livro2.titulo} - {livro2.autor} - {livro2.ano}')

#print(livro1.cor) #quando chamamos um dado que não foi criado, o nosso terminal diz que aos objetos da CLASSE Livro não tem o atributo 'cor', por isso não é possível chamar um dado que não foi criado.

print(id(livro1))
print(id(livro2))

#O computador diferencia os objetos em Python pelo seu ID, que corresponde ao seu endereço de memória. Como podemos ver os objetos tem id diferente. E por mais que eu crie um terceiro livro com o mesmo conteúdo ainda assim teríamos dois objetos diferentes.
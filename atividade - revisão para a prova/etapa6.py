from classes import Livro, Biblioteca
biblioteca = Biblioteca("IFRN")
livro1 = Livro("A Metamorfose", "Franz Kafka", 1915)
livro2 = Livro("Noites Brancas", "Fiódor Dostoiévski", 1848)
livro3 = Livro("1984", "George Orwell", 1949)
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.mostrar_lista()
biblioteca.remover_livro("1984")
biblioteca.mostrar_lista()

print(id(livro3))

variavel = livro3
print(id(variavel))

#sim, o livro pode ser utilizado em outra variavel; o id continua funcionando; um objeto só é apagado quando nenhuma variavel apontar para ele.
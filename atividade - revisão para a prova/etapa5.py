from classes import Livro, Biblioteca
biblioteca = Biblioteca("IFRN")

livro1 = Livro("A Metamorfose", "Franz Kafka", 1915)
print(f'{livro1.titulo} - {livro1.autor} - {livro1.ano}')
print(f"Livro 1 : {id(livro1)}")

biblioteca.adicionar_livro(livro1)
biblioteca.lista[0].autor = "Chico de Lilia"

print(f'{livro1.titulo} - {livro1.autor} - {livro1.ano}')
print(f"Livro 1 : {id(livro1)}")

#isso acontece porque a lista da Biblioteca guarda referências para o objeto livro1, não para alguma cópias dele.

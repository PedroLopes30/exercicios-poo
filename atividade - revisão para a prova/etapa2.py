from livro import Livro

livro1 = Livro("A Metamorfose", "Franz Kafka", 1915)
livro2 = Livro("Noites Brancas", "Fiódor Dostoiévski", 1848)

livro3 = livro1
print(livro1.ano)
print(livro3.ano)
print(f"Livro 1 : {id(livro1)}")
print(f"Livro 3 : {id(livro3)}")
livro3.ano = 2025
print(livro1.ano)
print(livro3.ano)
print(f"Livro 1 : {id(livro1)}")
print(f"Livro 3 : {id(livro3)}")
 
#Ao mudar um dado na variável, também mudamos a outra, porque elas são apenas nomes diferentes para o mesmo objeto. Ou seja, ambas as variáveis fazem referência ao mesmo objeto.
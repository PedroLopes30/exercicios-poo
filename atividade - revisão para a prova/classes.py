class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def mostrar_livro(self, livro):
        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor}")
        print(f"Ano: {livro.ano}")

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.lista = []

    def adicionar_livro(self, livro):
        if not livro in self.lista:
            self.lista.append(livro)
        else:
            print("Livro já está na lista")    

    def procurar_livro(self, livro):
        for i in self.lista:
            if i.titulo == livro.titulo:
                print("O livro já está na lista!") 

            else:
                print("Livro indísponivel")
    
    def remover_livro(self, titulo):
        for livro in self.lista:
            if livro.titulo == titulo:
                self.lista.remove(livro)
                return livro  
            
        print("Livro não encontrado")
        return None
    
    def mostrar_lista(self):
        print("Lista de Livros:")
        for livro in self.lista:
            print(f'{livro.titulo} - {livro.autor} - {livro.ano} - ID: {id(livro)}')
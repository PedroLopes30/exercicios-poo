class Filme:
    
    def __init__(self, titulo, ano, avaliacao):
        self.titulo = titulo
        self.ano = ano
        self.avaliacao = avaliacao

    def dar_nota(self, nova_nota):
        if 0 <= nova_nota <= 5:
            self.avaliacao = nova_nota 

        else:
            print("Nota inválida")       

class Playlist:

    def __init__(self, nome, filmes):
        self.nome = nome
        self.filmes = []

    def adcionar_filme(self, filme):
        self.filmes.append(filme)

    def remover_filme(self, filme):
        self.filmes.remove(filme)     

    def mostrar(self):
        for filme in self.filmes:
            print(f"\nFilme: {filme.titulo}. \nAno: {filme.ano} \nAvaliação: {filme.avaliacao}")        
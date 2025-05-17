from classes import Filme
from classes import Playlist

f1 = Filme("A Lista de Schindler", 1993, 4.8) 
f2 = Filme("Bastardos Inglórios", 2009, 4.6)  

p1 = Playlist("Playlist 1", [])
p2 = Playlist("Playlist 2", [])

p1.adcionar_filme(f1)
p2.adcionar_filme(f1)

f1.dar_nota(4.5)

print("Playlist 1:")
p1.mostrar()
print("--"*50)

print("Playlist 2:")
p2.mostrar()
print("--"*50)

print(id(p1.filmes[0]))
print(id(p1.filmes[0]))
print("--"*50)

p1.remover_filme(f1)

print("Playlist 1:")
p1.mostrar()
print("--"*50)

print("Playlist 2:")
p2.mostrar()
print("--"*50)
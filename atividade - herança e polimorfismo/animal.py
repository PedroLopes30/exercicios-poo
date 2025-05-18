class Animal:

    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cabra(Animal):
    def fazer_som(self):
        return 'Méééé!'
    
class Gato(Animal):
    def fazer_som(self):
        return 'Miau!' 

class Peru(Animal):
    def fazer_som(self):
        return 'Gulu Gulu!'

class Galinha(Animal):
    def fazer_som(self):
        return 'Pó!'

class Pintinho(Animal):
    def fazer_som(self):
        return 'PIUUUU!'   

cabra = Cabra("Mêlita") 
gato = Gato("Alfredo")
peru = Peru("Alisson Ramses Becker")
galinha = Galinha("Vizinha")
pintinho = Pintinho("Exterminador do Teu Furo")


print(cabra.nome + " faz: " + cabra.fazer_som())
print(gato.nome + " faz: " + gato.fazer_som())
print(peru.nome + " faz: " + peru.fazer_som())
print(galinha.nome + " faz: " + galinha.fazer_som())
print(pintinho.nome + " faz: " + pintinho.fazer_som())
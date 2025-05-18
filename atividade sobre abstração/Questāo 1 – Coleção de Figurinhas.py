class Figurinha():
    def __init__(self, numero, tema):
        self.numero = numero
        self.tema = tema

    def mostrar(self):
        print(f'Figurinha {self.numero} - {self.tema}')

class Pacotinho():
    def __init__(self):
        self.figurinhas = []

    def adicionar_figurinha(self, figurinha):
        self.figurinhas.append(figurinha)

    def listar(self):
        print("Figurinhas no pacotinho:")
        print("----------------------------")

        for figurinha in self.figurinhas:
            figurinha.mostrar() 
            print("----------------------------")

class MinhaColecao():
    def __init__(self):
        self.colecao = []
    def colar(self, pacotinho):
        for figurinha in pacotinho.figurinhas:
            if not any(f.numero == figurinha.numero for f in self.colecao):
                self.colecao.append(figurinha)
                print(f"Figurinha {figurinha.numero} foi colada na coleção!")
            else:
                print(f"Figurinha {figurinha.numero} já está na coleção. Ignorada.")
        print("----------------------------")            

    def faltantes(self):
        numeros_colados = []
        for figurinha in self.colecao:
            if figurinha.numero not in numeros_colados:
                numeros_colados.append(figurinha.numero)

        faltando = []
        for numero in range(1, 11):
            if numero not in numeros_colados:
                faltando.append(numero)

        if not faltando:
            print("Parabéns! Todas as figurinhas foram coladas no álbum.")
        else:
            print(f"Faltam {len(faltando)} figurinhas para completar o álbum: {faltando}")        
        print("----------------------------")

#Criando o PACOTINHO DE POKEMONS e a COLECAO do usuário

pacotinho_pokemon = Pacotinho()
minha_colecao = MinhaColecao()

#Criando as figurinhas disponíveis

fig1 = Figurinha(1, "Charizard")
fig2 = Figurinha(2, "Mewtwo")
fig3 = Figurinha(3, "Pikachu")
fig4 = Figurinha(4, "Rayquaza")
fig5 = Figurinha(5, "Garmchomp")
fig6 = Figurinha(6, "Sceptile")
fig7 = Figurinha(7, "Greninja")
fig8 = Figurinha(8, "Blastoise")
fig9 = Figurinha(9, "Venusaur")
fig10 = Figurinha(10, "Gengar")

#Adicionando as figurinhas que vão estar no PACOTINHO

pacotinho_pokemon.adicionar_figurinha(fig1)
pacotinho_pokemon.adicionar_figurinha(fig4)
pacotinho_pokemon.adicionar_figurinha(fig5)
pacotinho_pokemon.adicionar_figurinha(fig6)
pacotinho_pokemon.adicionar_figurinha(fig7)

#Listando as figurinhas do PACOTINHO

pacotinho_pokemon.listar()

#Mostrando quantas figurinhas faltam antes de COLAR na COLECAO

minha_colecao.faltantes()


#--------------------------------------
minha_colecao.colar(pacotinho_pokemon)

#Mostrando as figurinhas após COLAR na COLECAO

minha_colecao.faltantes()
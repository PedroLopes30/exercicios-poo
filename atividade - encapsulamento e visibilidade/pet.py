class Pet:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def imprimir_pet(self):
        print(f"Nome do pet:", self.nome)
        print(f"Peso do pet:" , self.peso)


    def alimentar_pet(self, comida):
        self.peso + comida 

#------------------------
class Abrigo:
    __catalogo = []

    def adicionar_pet(self, pet):
        self.__catalogo.append(pet)   

    def imprimir_abrigo(self):
        print("pets no abrigo:")
        print("-----------")

        for pet in self.__catalogo:
            pet.imprimir_pet()
            print("-----------")                    
#------------------------

abrigo = Abrigo()

pet = Pet("Cuscuz", 10)
abrigo.adicionar_pet(pet)

pet = Pet("Carlinhos", 100)
abrigo.adicionar_pet(pet)

abrigo.imprimir_abrigo()

abrigo.catalogo = []

abrigo.imprimir_abrigo()
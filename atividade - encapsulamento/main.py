class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.__tipoCombustivel = tipoCombustivel
        self.__valorLitro = valorLitro
        self.__quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros = valor/self.__valorLitro
        print(f"Você abasteceu R${valor:.2f}, o que equivale a {litros:.2f} litros.")
        self.__quantidadeCombustivel -= litros
        return litros
    
    def abastecerPorLitro(self, litros):
        valor = self.__valorLitro * litros
        print(f"Você abasteceu R$'{valor:.2f}, o que equivale a {litros} litros.")
        self.__quantidadeCombustivel -= litros
        return valor
    
    def get_tipoCombustivel(self):
        return self.__tipoCombustivel
    
    def get_valorLitro(self):
        return self.__valorLitro
    
    def get_quantidadeCombustivel(self):
        return self.__quantidadeCombustivel
    
    def set_alterarValor(self, valor):
        self.__valorLitro = valor

    def set_alterarCombustivel(self, combustivel):
        self.__tipoCombustivel = combustivel

    def set_alterarQuantidadeCombustivel(self, quantidade):
        self.__quantidadeCombustivel = quantidade 
           

ipiranga = bombaCombustivel("comum", 6.3, 1000)

print(ipiranga.get_quantidadeCombustivel())
print(ipiranga.get_tipoCombustivel())
print(ipiranga.get_valorLitro())
ipiranga.abastecerPorLitro(5)
ipiranga.abastecerPorValor(50)
print(ipiranga.get_quantidadeCombustivel())
print(ipiranga.get_tipoCombustivel())
print(ipiranga.get_valorLitro())
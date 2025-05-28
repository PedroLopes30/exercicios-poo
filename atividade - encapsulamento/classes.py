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


class Veiculo:
    def __init__(self, modelo, tipoCombustivelVeiculo, capacidadeTanque):
      self.__modelo = modelo
      self.__tipoCombustivelVeiculo = tipoCombustivelVeiculo
      self.__capacidadeTanque = capacidadeTanque
      self.nivelCombustivel = 0

    def abastecerVeiculoPL(self, bomba, litros):
        if self.__tipoCombustivelVeiculo != bomba.get_tipoCombustivel():
            print(f"Erro: O veículo {self.modelo} não aceita {bomba.get_tipoCombustivel()}.")
            return
        
        if litros > bomba.get_quantidadeCombustivel():
            print(f"Erro: Não há combustível suficiente na bomba. Disponível: {bomba.get_quantidadeCombustivel()} litros.")
            return
        if self.nivelCombustivel + litros > self.__capacidadeTanque:
            litros = self.__capacidadeTanque - self.nivelCombustivel
            print(f"Tanque cheio. Abastecendo apenas {litros:.2f} litros.")

        litros_fornecidos = bomba.abastecerPorLitro(litros)/bomba.get_valorLitro()
        self.nivelCombustivel += litros_fornecidos

        print(f"Abastecido {litros_fornecidos:.2f} litros no veículo {self.__modelo}.")

    def abastecerVeiculoPV(self, bomba, valor):
        if self.__tipoCombustivelVeiculo != bomba.get_tipoCombustivel():
            print(f"Erro: O veículo {self.__modelo} não aceita {bomba.get_tipoCombustivel()}.")
            return
        
        litros_fornecidos = bomba.abastecerPorValor(valor)
        if litros_fornecidos > bomba.get_quantidadeCombustivel():
            print(f"Erro: Não há combustível suficiente na bomba. Disponível: {bomba.get_quantidadeCombustivel()} litros.")
            return
        if self.nivelCombustivel + litros_fornecidos > self.__capacidadeTanque:
            litros_fornecidos = self.__capacidadeTanque - self.nivelCombustivel
            print(f"Tanque cheio. Abastecendo apenas {litros_fornecidos:.2f} litros.")

        self.nivelCombustivel += litros_fornecidos
        print(f"Abastecido {litros_fornecidos:.2f} litros no veículo {self.__modelo}.")
from classes import bombaCombustivel, Veiculo

print("Testando Bomba de Combustível e Veículo")
bomba = bombaCombustivel("Gasolina", 5.50, 200)
veiculo = Veiculo("Fusca", "Gasolina", 50)
# combustivel disponivel na bomba
print(f"Combustível disponível na bomba: {bomba.get_quantidadeCombustivel()} litros")
# Abastecendo por valor
veiculo.abastecerVeiculoPV(bomba, 100)
print(f"Combustível no veículo após abastecimento por valor: {veiculo.nivelCombustivel:.2f} litros")
print(f"Combustível restante na bomba: {bomba.get_quantidadeCombustivel():.2f} litros")
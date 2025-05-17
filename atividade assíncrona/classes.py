class Vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas >= meta:
            return f"{self.nome} bateu a meta!"
        else:
            return f"{self.nome} não bateu a meta."
        
    def bonus(self, meta):
        if self.vendas >= meta:
            bonus = (self.vendas * 10)/100
            return f"Bônus: {bonus}\n"
        else:
            return f"Bônus: 0\n"
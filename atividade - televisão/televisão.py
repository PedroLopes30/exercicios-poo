class Televisão:
    def __init__(self):
        self.canal = 1
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100
        self.canal_min = 1
        self.canal_max = 99
        self.ligada = False

    def ligar(self):
        self.ligada = True
    
    def desligar(self):
        self.ligada = False

    def mudar_canal_para_cima(self):
        if not self.ligada:
            return
        elif self.canal < self.canal_max:
            self.canal += 1

    def mudar_canal_para_baixo(self):
        if not self.ligada:
            return
        elif self.canal > self.canal_min:
            self.canal -= 1

    def aumentar_volume(self):
        if not self.ligada:
            return
        elif self.volume < self.volume_max:
            self.volume +=5

    def reduzir_volume(self):
        if not self.ligada: 
            return
        elif self. volume > self.volume_min:
            self.volume -= 5 

    def __str__(self):
        return f'Televisão - Está ligada = {self.ligada} - Canal: {self.canal} - Volume: {self.volume} '

#--------------------------------------------------------------------------------

# Testando os métodos LIGAR e DESLIGAR 

tv_teste = Televisão()
print(tv_teste)

print("A TV está ligada?", tv_teste.ligada)
tv_teste.ligar()
print("A TV está ligada?", tv_teste.ligada)
tv_teste.desligar()
print("A TV está ligada?", tv_teste.ligada)

# Testando os métodos MUDAR CANAL
tv_teste.ligar()
print("Qual é o CANAL da TV agora?", tv_teste.canal)
tv_teste.mudar_canal_para_cima()
print("Qual é o CANAL da TV agora?", tv_teste.canal)
tv_teste.mudar_canal_para_baixo()
print("Qual é o CANAL da TV agora?", tv_teste.canal)

# Testando os métodos AUMENTAR/ REDUZIR volume

print("Qual é o volume da TV agora:" , tv_teste.volume)
tv_teste.aumentar_volume()
print("Qual é o volume da TV agora:" , tv_teste.volume)
tv_teste.reduzir_volume()
print("Qual é o volume da TV agora:" , tv_teste.volume)
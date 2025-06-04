class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def mostrar_livro(self, livro):
        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor}")
        print(f"Ano: {livro.ano}")

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.lista = []

    def adicionar_livro(self, livro):
        if not livro in self.lista:
            self.lista.append(livro)
        else:
            print("Livro já está na lista")    

    def procurar_livro(self, livro):
        for i in self.lista:
            if i.titulo == livro.titulo:
                print("O livro já está na lista!") 

            else:
                print("Livro indísponivel")
    
    def remover_livro(self, titulo):
        for livro in self.lista:
            if livro.titulo == titulo:
                self.lista.remove(livro)
                return livro  
            
        print("Livro não encontrado")
        return None
    
    def mostrar_lista(self):
        print("Lista de Livros:")
        for livro in self.lista:
            print(f'{livro.titulo} - {livro.autor} - {livro.ano} - ID: {id(livro)}')

class Banco:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        if self.__validar_nome(novo_nome):
            self.__nome = novo_nome.strip()

        else:
            print("Nome inválido!")    

    def __validar_nome(self, nome):
        nome = nome.strip()
        return type(nome) == str and len(nome.strip()) >= 3 
            
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        if type(novo_nome) == str and len(novo_nome.strip()) >= 3:
            self.__nome = novo_nome.strip()  

    def get_cpf(self):
        return self.__cpf  

class Conta:
    total_contas = 0

    def __init__(self, numero, cliente, saldo):
        self.__numero = numero
        self.__dono = cliente
        self.__saldo = saldo
        Conta.total_contas += 1

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__registrar_operacao("Depósito", valor)
        else:
            print("Valor inválido!")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            self.__registrar_operacao("Saque", valor)
        else:
            print("Saldo insuficiente ou valor inválido.")             

    def mostrar_saldo(self):
        print(f"Saldo: R$ {self.__saldo:.2f}")

    def __registrar_operacao(self, tipo, valor):
        print(f"{tipo} de R$ {valor:.2f} realizado com sucesso.")    
        